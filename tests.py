import unittest
import requests

class TestReverseAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5000/reverse"

    def test_reverse_words(self):
        test_cases = {
            "Hello": "olleH",
            "world": "dlrow",
            "hello world!": "!dlrow olleh",
            "Python": "nohtyP",
            "12345": "54321"
        }

        for word, expected in test_cases.items():
            with self.subTest(word=word):
                response = requests.post(self.BASE_URL, json={"word": word})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json().get("reversed"), expected)

    def test_missing_word(self):
        response = requests.post(self.BASE_URL, json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

if __name__ == "__main__":
    unittest.main()

