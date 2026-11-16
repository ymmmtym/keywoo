import unittest
from unittest.mock import patch
from urllib.parse import urlparse

from flask.config import Config

original_from_object = Config.from_object


def apply_test_config(config, obj):
    original_from_object(config, obj)
    config.update(SQLALCHEMY_DATABASE_URI='sqlite://', TESTING=True)


with patch.object(Config, 'from_object', apply_test_config):
    from keywoo import app, db
    from keywoo.models.sites import Site
    from keywoo.models.users import User


def redirect_path(response):
    return urlparse(response.location).path


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.context = app.app_context()
        self.context.push()
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def signup(self, name='alice', password='secret'):
        return self.client.post('/signup', data={'name': name, 'password': password})

    def login(self, name='alice', password='secret'):
        return self.client.post('/login', data={'name': name, 'password': password})

    def add_site(self, name='example', url='https://example.com'):
        return self.client.post('/', data={'radio': 'add', 'name': name, 'url': url})

    def test_signup_creates_user_with_pbkdf2_hash(self):
        response = self.signup()
        self.assertEqual(redirect_path(response), '/login')
        user = User.query.filter_by(name='alice').one()
        self.assertTrue(user.password.startswith('pbkdf2:sha256:'))
        self.assertLessEqual(len(user.password), 100)

    def test_signup_rejects_duplicate_user(self):
        self.signup()
        response = self.signup()
        self.assertEqual(redirect_path(response), '/signup')
        self.assertEqual(User.query.count(), 1)

    def test_signup_requires_name_and_password(self):
        response = self.client.post('/signup', data={'name': '', 'password': ''})
        self.assertEqual(redirect_path(response), '/signup')
        self.assertEqual(User.query.count(), 0)

    def test_login_with_valid_credentials(self):
        self.signup()
        self.assertEqual(redirect_path(self.login()), '/')

    def test_login_with_wrong_password(self):
        self.signup()
        self.assertEqual(redirect_path(self.login(password='wrong')), '/login')

    def test_login_with_unknown_user(self):
        self.assertEqual(redirect_path(self.login(name='nobody')), '/login')

    def test_index_add_site(self):
        self.signup()
        self.login()
        response = self.add_site()
        self.assertEqual(response.status_code, 200)
        site = Site.query.filter_by(name='example').one()
        self.assertEqual(site.url, 'https://example.com')
        self.assertEqual(site.user, 'alice')

    def test_index_rejects_invalid_url(self):
        self.signup()
        self.login()
        self.assertEqual(redirect_path(self.add_site(name='bad', url='not-a-url')), '/')
        self.assertEqual(Site.query.count(), 0)

    def test_index_delete_site(self):
        self.signup()
        self.login()
        self.add_site()
        response = self.client.post('/', data={'radio': 'delete', 'check': ['example']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Site.query.count(), 0)

    def test_result_page(self):
        self.signup()
        self.login()
        response = self.client.post('/result', data={'search': 'https://example.com'})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
