import unittest
from src.helpers.helpers import rescale
from src.helpers.helpers import row_select_reduce

class Test_Helpers(unittest.TestCase):

    def test_no_rev(self):
        rev_list = []
        non_zero_medians = {}
        raw_data = {
            'X1': 1,
            'X2': 2,
            'X3': 4,
            'X4': 3,
            'X5': 2
            }
        expected = {
            'X1': 0,
            'X2': 1,
            'X3': 3,
            'X4': 2,
            'X5': 1
            }
        result = rescale(raw_data, rev_list, non_zero_medians)
        self.assertEqual(result, expected)

    def test_rev(self):
        rev_list = ['X1','X2','X3','X4','X5']
        non_zero_medians = {}
        raw_data = {
            'X1': 1,
            'X2': 2,
            'X3': 4,
            'X4': 3,
            'X5': 2
        }
        expected = {
            'X1': 3,
            'X2': 2,
            'X3': 0,
            'X4': 1,
            'X5': 2
        }
        result = rescale(raw_data, rev_list, non_zero_medians)
        self.assertEqual(result, expected)

    def test_rescale_zero_blanks(self):
        rev_list = []
        non_zero_medians = {
            'X1': 1,
            'X3': 1
        }
        raw_data = {
            'X1': 1,
            'X2': 2,
            'X3': 3,
            'X4': 5,
            'X5': 'BLANK'
        }
        expected = {
            'X1': 0,
            'X2': 1,
            'X3': 2,
            'X4': 4,
            'X5': 0
        }
        result = rescale(raw_data, rev_list, non_zero_medians)
        self.assertEqual(result, expected)

    def test_rescale_nonzero_blanks(self):
        rev_list = []
        non_zero_medians = {
            'X1': 1,
            'X3': 1
        }
        raw_data = {
            'X1': 1,
            'X2': 'BLANK',
            'X3': 'BLANK',
            'X4': 5,
            'X5': 4
        }
        expected = {
            'X1': 0,
            'X2': 0,
            'X3': 1,
            'X4': 4,
            'X5': 3
        }
        result = rescale(raw_data, rev_list, non_zero_medians)
        self.assertEqual(result, expected)        
        
    def test_reduce_all(self):
        question_set = ['X1','X2','X3','X4','X5']
        raw_data = {
            'X1': 1,
            'X2': 2,
            'X3': 3,
            'X4': 4,
            'X5': 5
        }
        self.assertEqual(row_select_reduce(raw_data, question_set), 15)
        
    def test_reduce_some(self):
         question_set = ['X1','X5']
         raw_data = {
             'X1': 1,
             'X2': 2,
             'X3': 3,
             'X4': 4,
             'X5': 5
         }
         self.assertEqual(row_select_reduce(raw_data, question_set), 6)
