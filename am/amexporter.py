import requests
import urllib3
import logging
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import http.cookiejar

logging.basicConfig(level=logging.DEBUG)


class InvalidArgs(Exception):
    pass


class ApiException(Exception):
    pass


class AmExpoort(object):
    def __init__(self, source, target, proxy=None):
        if not all([source, target]):
            logging.error("source and target must be provided")
            raise InvalidArgs
        self.src_url = source.strip("/")
        self.tgt_url = target.strip("/")
        self.src_active = []
        self.src_expired = []
        self.tgt_active = []
        self.tgt_expired = []

        self.session = requests.Session()
        if proxy is not None:
            self.session.proxies = proxy
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        self.session.mount("http://", HTTPAdapter(max_retries=retries))
        self.session.mount("https://", HTTPAdapter(max_retries=retries))
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers = {"Content-Type": "application/json"}


    def get_silences(self, am_url, active, expired):
        try:
            url = f"{am_url}/api/v2/silences"
            resp = self.session.get(url=url, headers=self.headers)
            resp.raise_for_status()
            silences = resp.json()
            # self.active = []
            # self.expired = []
            for s in silences:
                if s['status']['state'] == 'active':
                    active.append(s)
                else:
                    expired.append(s)
        except Exception as e:
            raise ApiException(e)

    def get_all_silences(self):
        self.get_silences(self.src_url, self.src_active, self.src_expired)
        self.get_silences(self.tgt_url, self.tgt_active, self.tgt_expired)

    def add_silence(self, t_url, silence):
        t_url = t_url.strip("/")
        try:
            url = f"{t_url}/api/v2/silences"
            resp = self.session.post(url=url, headers=self.headers, json=silence)
            resp.raise_for_status()
        except Exception as e:
            raise ApiException(e)

    def delete_silence(self, t_url, silence):
        url = f"{t_url.strip('/')}/api/v2/silence/{silence['id']}"
        try:
            resp = self.session.delete(url, headers=self.headers)
            resp.raise_for_status()
        except Exception as e:
            raise ApiException(e)

    def add_silnces_to_tgt(self):
        for s in self.src_active:
            self.add_silence(self.tgt_url, s)

    def del_dup_silences(self):
        for s in self.tgt_active:
            self.delete_silence(self.tgt_url, s)

    def sync(self):
        self.get_all_silences()
        self.add_silnces_to_tgt()
        self.del_dup_silences()
