import unittest
from src.oxy_score import score
import os

class Test_Oxy_Score(unittest.TestCase):

	def test_score(self):
		base = os.getcwd()
		fixtures_path = os.path.join(base, 'test/fixtures/partial_data.csv')

		results = score(fixtures_path)
		expected = [{
				'id'   : 'HCOT-30',
				'awr'  : 6,
				'cog'  : 3,
				'com'  : 5,
				'mot'  : 0,
				'rrb'  : 5,
				'sci'  : 14,
				'srs2' : 19
			},
			{
				'id'   : 'HCOT-31',
				'awr'  : 5,
				'cog'  : 1,
				'com'  : 1,
				'mot'  : 3,
				'rrb'  : 1,
				'sci'  : 10,
				'srs2' : 11
			}]

		self.assertEqual(results[1], expected[1])
		self.assertEqual(results[0], expected[0])
