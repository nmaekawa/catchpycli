"""
catchpycli.client
---------------------
Defines the main API client class
"""

import os
import requests

from consumer.catchjwt import encode_catchjwt

from .utils import default_useragent


_default_timeout = 5


class CatchpyCli(object):

    def __init__(self, base_url, api_key, secret_key, timeout=None):
        self.url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.timeout = timeout or _default_timeout
        self.default_headers = {
            'User-Agent': default_useragent(),
            'Accept': 'Application/json',
            'Content-Type': 'Application/json',
        }


    def make_authorization_header(self, user):
        jwt = encode_catchjwt(
            apikey=self.api_key, secret=self.secret_key, user=user)
        return 'token {}'.format(jwt)


    def request_no_body(
            self, path, method, params=None, extra_headers=None):
        if params is None:
            params = {}
        if extra_headers is None:
            extra_headers = {}
        headers = self.default_headers.copy()
        headers.update(extra_headers)

        url = urljoin(self.url, path)
        resp = getattr(requests, method)(
            url, params=params, headers=headers, timeout=self.timeout)

        resp.raise_for_status()
        return resp


    def request_with_body(
        self, path, method, data=None, extra_headers=None):
        if data is None:
            data = {}
        if extra_headers is None:
            extra_headers = {}
        headers = self.default_headers.copy()
        headers.update(extra_headers)

        url = urljoin(self.url, path)
        resp = getattr(requests, method)(
                url, data=data, headers=headers, timeout=self.timeout)

        resp.raise_for_status()
        return resp


    def get(self, path, params=None, extra_headers=None):
        return self.request_no_body(
            path, method='get', params=params, extra_headers=extra_headers)


    def delete(self, path, params={}, extra_headers={}):
        return self.request_no_body(
            path=path, method='delete', params=params,
            extra_headers=extra_headers)


    def post(self, path, data=None, extra_headers=None):
        return self.request_with_body(
            path=path, method='post', data=data, extra_headers=extra_headers)


    def put(self, path, data={}, extra_headers={}):
        return self.request_with_body(
            path=path, method='put', data=data, extra_headers=extra_headers)



