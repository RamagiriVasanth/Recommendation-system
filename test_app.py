# test_app.py
import unittest
from app import app

class TestRecommendationSystem(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_recommendations(self):
        response = self.app.get('/recommendations?user_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommended_products', response.json)

if __name__ == '__main__':
    unittest.main()
