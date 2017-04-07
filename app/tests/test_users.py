from flask import url_for
from .test_base import BaseTest


class UserTestCase(BaseTest):

    def test_user_index(self):
        user = self.register_user(1)
        token = self.token_for_user(user)
        res = self.client.get(url_for('user.index'),
                              headers=self.get_api_headers(token))
        self.assertEqual(res.status_code, 200)
