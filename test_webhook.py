import json
import unittest
from flask import Flask
from app import create_app

class WebhookTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_push_event(self):
        # Simulate a push event payload
        payload = {
            "ref": "refs/heads/main",
            "after": "abc123",
            "pusher": {"name": "Travis"},
            "before": "xyz789"
        }
        response = self.client.post('/webhook/receiver', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_pull_request_event(self):
        # Simulate a pull request event payload
        payload = {
            "action": "opened",
            "pull_request": {
                "id": 1,
                "user": {"login": "Travis"},
                "head": {"ref": "feature-branch"},
                "base": {"ref": "main"}
            }
        }
        response = self.client.post('/webhook/receiver', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_merge_event(self):
        # Simulate a merge event payload
        payload = {
            "action": "closed",
            "pull_request": {
                "merged": True,
                "id": 1,
                "user": {"login": "Travis"},
                "head": {"ref": "feature-branch"},
                "base": {"ref": "main"}
            }
        }
        response = self.client.post('/webhook/receiver', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_invalid_event(self):
        # Simulate an invalid event payload
        payload = {}
        response = self.client.post('/webhook/receiver', json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'error', response.data)

if __name__ == '__main__':
    unittest.main()
