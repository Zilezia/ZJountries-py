import json
import unittest

from src.ZJountries import get_place

data_path = "./src/test_data.json"
# data_path = "./src/data3.json"

with open(data_path) as file:
    data = json.load(file)

class TestZJ(unittest.TestCase):
	def test_module(self):
		self.assertEqual(get_place(), data)

class TestField(unittest.TestCase):
	def test_module(self):
		self.assertEqual(get_place(fields='id'), [{'id': 1}, {'id': 2}])

class TestBy(unittest.TestCase):
	def test_module(self):
		self.assertEqual(get_place(by='name'), [{'id': 1, 'name': 'first'}])



if __name__ == '__main__':
    unittest.main()