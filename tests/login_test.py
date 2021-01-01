import unittest
from fastLearner import createApp
import json

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = createApp("test")
        self.client = self.app.test_client()
    def test_normal_login(self):
        resp = self.client.post("/login", data='{"name": "admin", "pwd": "123456"}', content_type='application/json')
        data=json.loads(resp.data)
        print(data)
        self.assertEqual(data["payload"]["id"],1)
        self.assertEqual(data["code"], 200)
        self.assertEqual(resp.mimetype, "application/json")
        