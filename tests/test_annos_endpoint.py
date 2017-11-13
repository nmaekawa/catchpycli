
from unittest.mock import patch

from catchpycli.client import CatchpyCli


base_url = 'http://fake.com'
api_key = 'api_key'
secret_key = 'secret_key'
user = 'user'


class TestAnnoEndpoint(object):

    def setup(self):
        self.cli = CatchpyCli(
            base_url=base_url,
            api_key=api_key,
            secret_key=secret_key,
        )

    def test_create_ok(self):
        pass

    def test_read_ok(self):
        pass

    def test_update_ok(self):
        pass

    def test_delete_ok(self):
        pass

