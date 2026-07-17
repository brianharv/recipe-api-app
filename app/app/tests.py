from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
	def test_add_two_numbers(self):
		res = calc.add(4, 7)
    
		self.assertEqual(res, 11)

	def test_subtract_numbers(self):
		res = calc.subtract(10, 15)

		self.assertEqual(res, 5)