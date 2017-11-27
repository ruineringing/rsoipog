from django.test import TestCase
from django.test.client import Client

class Tests(TestCase):
	def setUp(self):
		self.client = Client()

	def testok(self):
		response = self.client.get('/index.html')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('')
		self.assertEqual(response.status_code, 200)

	def testnotfound(self):
		response = self.client.get('/a.html')
		self.assertEqual(response.status_code, 404)
