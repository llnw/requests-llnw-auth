import sys
import os
import time
import hmac
import hashlib
import binascii
import requests

class LLNWAuth(requests.auth.AuthBase):
    def __init__(self, api_user, api_key):
        self.api_user = api_user
        self.api_key = api_key

    def __call__(self, r):
        url = r.url
        method = r.method.upper()
        request_body = r.body
        auth_headers = self._build_auth_headers(url, method, request_body)
        for key in auth_headers:
            r.headers[key] = auth_headers[key]
        return r

    def _build_auth_headers(self, url, method, request_body):
        partitioned_url = url.partition('?')
        auth_url = partitioned_url[0]
        query_string = partitioned_url[2]
        timestamp = str(int(round(time.time() * 1000)))
        if request_body == None:
            request_body = ''
        data = f'{method}{auth_url}{query_string}{timestamp}{request_body}'
        token = hmac.new(binascii.unhexlify(self.api_key), msg = data.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()

        return {
            'X-LLNW-Security-Principal' : self.api_user,
            'X-LLNW-Security-Timestamp' : timestamp,
            'X-LLNW-Security-Token' : token
        }
