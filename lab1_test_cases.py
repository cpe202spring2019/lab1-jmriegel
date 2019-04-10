import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """testing that max_list_iter returns 3 as the max of the list [1,2,3]"""
        my_list1 = [1,2,3]
        self.assertEqual(max_list_iter(my_list1), 3)
        """testing that max_list_iter returns None when called on an empty list"""
        my_list2 = []
        self.assertEqual(max_list_iter(my_list2), None)
        """testing that max_list_iter raises a ValueError when called on a list that is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
           max_list_iter(tlist)

    def test_reverse_rec(self):
        """testing that reverse_rec returns [3,2,1] as the reverse of the list [1,2,3]"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        """testing that reverse_rec returns [0,0,0] as the reverse of the list [0,0,0]"""
        self.assertEqual(reverse_rec([0,0,0]), [0,0,0])
        """testing that reverse_rec raises a ValueError when called on a list that is None"""
        my_list = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(my_list)


    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        """testing that bin_search returns 4 when called on list_val =[0,1,2,3,4,7,8,9,10], with target = 4"""
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        """testing that bin_search returns 2 when called on list_val =[0,1,2,3,4,7,8,9,10], with target = 2"""
        self.assertEqual(bin_search(2, low, high, list_val), 2)
        """testing that bin_search returns None when called on list_val =[0,1,2,3,4,7,8,9,10], with target = 6"""
        self.assertEqual(bin_search(6, low, high, list_val), None)
        """testing that bin_search returns 7 when called on list_val =[0,1,2,3,4,7,8,9,10], with target = 9"""
        self.assertEqual(bin_search(9, 0, len(list_val) - 1, list_val), 7)
        """testing that bin_search raises a ValueError when called on a list that is None"""
        my_list = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(9, low, high, my_list)


if __name__ == "__main__":
        unittest.main()
