#!/usr/bin/python3
import requests
import socket
import datetime
import time


def runtest():
    res = requests.post("http://prom-alertmanager.omegaworld.net/api/v2/silences", json={
        "matchers": [
            {"name": "alertname", "value": "InstanceDown", "isRegex": False},
        ],
        "startsAt": datetime.datetime.utcfromtimestamp(time.time()).isoformat(),
        "endsAt": datetime.datetime.utcfromtimestamp(time.time() + 4 * 3600).isoformat(),
        "comment": "Backups on {}".format(socket.gethostname()),
        "createdBy": "My backup script",
    },
                        )
    res.raise_for_status()
    silenceId = res.json()["silenceID"]
    print(silenceId)

def runtest2():
    res = requests.post("http://prom-alertmanager.omegaworld.net/api/v2/silences", json={
        "matchers": [
            {
                "name": "alertname",
                "value": "InstanceDown",
                "isRegex": False
            }
        ],
        "startsAt": "2023-08-25T22:12:33.533330795Z",
        "endsAt": "2023-10-25T23:11:44.603Z",
        "createdBy": "api",
        "comment": "Silence",
        "status": {
            "state": "active"
        },
    }
                        )
    res.raise_for_status()
    silenceId = res.json()["silenceID"]
    print(silenceId)