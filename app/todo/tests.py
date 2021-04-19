import json

from django.test import (
    TestCase,
    Client
)


class TodoListTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_todolist_get_success(self):
        client = Client()

        response = client.get('/todos/api/')
        self.assertEqual(response.status_code, 200)
