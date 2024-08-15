import unittest
from app/server.py import app

class FlaskTestCase(unittest.TestCase):
def test_index(self):
	tester = app.testx_client(self)
	response = tester.get('/')
	self.assertEqual(response.status_code, 200)
	self.assertEqual(response.data, b'Hello, Jenkins!')

if __name__ == '__main__':
	unittest.main()
