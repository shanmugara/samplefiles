package main

import (
	"encoding/base64"
	"fmt"
	"log"
	"net/http"
	"time"
)

// Constants for header names
const (
	UsernameHeader = "X-IPM-Username"
	PasswordHeader = "X-IPM-Password"
)

func (h *headerTransport) RoundTrip(req *http.Request) (*http.Response, error) {
	userEncode := base64.StdEncoding.EncodeToString([]byte(h.userid))
	passwordEncode := base64.StdEncoding.EncodeToString([]byte(h.password))

	// Add headers to the request
	req.Header.Add(UsernameHeader, userEncode)
	req.Header.Add(PasswordHeader, passwordEncode)

	var resp *http.Response
	var err error

	// Number of retries
	maxRetries := 3

	for attempt := 1; attempt <= maxRetries; attempt++ {
		resp, err = http.DefaultTransport.RoundTrip(req)
		if err == nil && resp.StatusCode == http.StatusOK {
			break
		}

		log.Printf("Attempt %d failed: %v\n", attempt, err)

		// Sleep before the next attempt (you can use a more sophisticated backoff strategy)
		time.Sleep(time.Second)
	}

	if err != nil {
		log.Printf("Error: %v\n", err)
	}

	return resp, err
}

type headerTransport struct {
	userid   string
	password string
}

func main() {
	client := &http.Client{
		Transport: &headerTransport{userid: "user", password: "pass"},
	}

	req, _ := http.NewRequest("GET", "http://example.com", nil)
	client.Do(req)
}
