"""
catchpycli.client
---------------------
Defines the main API client class
"""

import os
import json
import requests
from urllib.parse import urljoin

####################
# set django context
#
import django
from django.conf import settings
from dotenv import load_dotenv

# if dotenv file, load it
dotenv_path = os.environ.get('CATCHPY_DOTENV_PATH', None)
if dotenv_path:
    load_dotenv(dotenv_path)

# define settings if not in environment
if os.environ.get("DJANGO_SETTINGS_MODULE", None) is None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catchpy.settings.dev")

django.setup()
#
####################

#
# now we can import django app modules
#
from consumer.catchjwt import encode_catchjwt

from .utils import default_useragent


_default_timeout = 5


class CatchpyCli(object):

    def __init__(self, base_url, api_key, secret_key,
                 timeout=None, skip_ssl=False):
        self.url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.timeout = timeout or _default_timeout
        self.verify_ssl = not skip_ssl
        self.default_headers = {
            'User-Agent': default_useragent(),
            'Accept': 'Application/json',
            'Content-Type': 'Application/json',
        }


    def make_authorization_token(self, user):
        jwt = encode_catchjwt(
            apikey=self.api_key, secret=self.secret_key, user=user)
        return jwt.decode('utf-8')


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
            url, params=params, headers=headers, timeout=self.timeout,
            verify=self.verify_ssl)

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
                url, data=json.dumps(data), headers=headers,
                timeout=self.timeout, verify=self.verify_ssl)

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



