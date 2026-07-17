# test_app.py from mlh task 1

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, mydb, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    # implementing tearDown class to delete all timeline posts after each test
    # prevents test data from leaking into next test
    def tearDown(self):
        TimelinePost.delete().execute()

    # implementing tearDownClass to close the database connection after all tests have run
    # prevents unclosed connection warning
    @classmethod
    def tearDownClass(cls):
        if not mydb.is_closed():
            mydb.close()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # TO DO: add more tests relating to the home page
        assert "Experience" in html or "Education" in html or "About" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        assert response.get_json()["timeline_posts"] == []

        # TO DO: more tests relating to the /api/timeline_post GET and POST apis
        post_response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert post_response.status_code == 200
        assert post_response.is_json
        json = post_response.get_json()
        assert json["name"] == "John Doe"
        assert json["email"] == "john@example.com"
        assert json["content"] == "Hello world, I'm John!"

        get_response = self.client.get("/api/timeline_post")
        assert get_response.status_code == 200
        posts = get_response.get_json()["timeline_posts"]
        assert len(posts) == 1
        assert posts[0]["name"] == "John Doe"
        assert posts[0]["email"] == "john@example.com"
        assert posts[0]["content"] == "Hello world, I'm John!"

        # more tests relating to the timeline page
        timeline_page = self.client.get("/timeline")
        assert timeline_page.status_code == 200
        html = timeline_page.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert "John Doe" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
