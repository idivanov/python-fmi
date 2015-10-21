import unittest
import solution


class PowerOfTwoTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(solution.powers_of_two_remain([]))

    def test_single_number_in_list_should_always_be_true(self):
        self.assertTrue(solution.powers_of_two_remain([8]))

    def test_multiple_numbers_in_list_true11(self):
        self.assertTrue(solution.powers_of_two_remain([7, 8]))

    def test_multiple_numbers_in_list_false11(self):
        self.assertFalse(solution.powers_of_two_remain([4, 8, 12]))

    def test_random_numbers_in_list_true11(self):
        self.assertTrue(solution.powers_of_two_remain([34, 78, 54]))

    def test_random_numbers_in_list_false11(self):
        self.assertFalse(solution.powers_of_two_remain([8, 16, 24]))

    def test_simple(self):
        self.assertEqual(solution.powers_of_two_remain([]), False)
        self.assertEqual(solution.powers_of_two_remain([7, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8, 12]), False)
        self.assertEqual(solution.powers_of_two_remain([10, 10]), False)
        self.assertEqual(solution.powers_of_two_remain([10, 10, 10]), True)

    def test_powers_of_two(self):
        self.assertEqual(solution.powers_of_two_remain([4]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8, 16]), True)
        self.assertEqual(solution.powers_of_two_remain([32, 16, 2]), True)

    def test_true(self):
        self.assertEqual(solution.powers_of_two_remain([10, 1, 3, 5, 6]), True)
        self.assertEqual(solution.powers_of_two_remain([6, 12, 24]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([6, 12, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([10, 12, 6, 2]), True)
        self.assertEqual(solution.powers_of_two_remain([14, 6]), True)
        self.assertEqual(solution.powers_of_two_remain([6, 10, 8, 3, 3]), True)

    def test_false(self):
        self.assertEqual(solution.powers_of_two_remain([10, 12, 6, 10, 12, 6]),
                         False)
        self.assertEqual(solution.powers_of_two_remain([10, 12, 6]), False)
        self.assertEqual(solution.powers_of_two_remain([16, 18, 2]), False)
        self.assertEqual(solution.powers_of_two_remain([14, 6, 8]), False)

    def test_empty_list(self):
        self.assertFalse(solution.powers_of_two_remain([]))
 
    def test_multiple_numbers_in_list_true22(self):
        self.assertTrue(solution.powers_of_two_remain([7, 8]))
 
    def test_multiple_numbers_in_list_true22(self):
        self.assertTrue(solution.powers_of_two_remain([2, 6, 8, 10]))

    def test_multiple_numbers_in_list_false222(self):
        self.assertFalse(solution.powers_of_two_remain([4, 8, 12]))
  
    def test_multiple_numbers_in_list_true222(self):
        self.assertTrue(solution.powers_of_two_remain([1, 7, 5, 11]))

    def test_multiple_numbers_in_list_false2222(self):
        self.assertFalse(solution.powers_of_two_remain([6, 5, 3, 10, 8, 2]))
  
    def test_multiple_numbers_in_list_false22222(self):
        self.assertFalse(solution.powers_of_two_remain([1, 2, 4, 5, 7, 8, 13]))
  
    def test_multiple_numbers_in_list_false222222(self):
        self.assertFalse(solution.powers_of_two_remain([1, 2, 4, 7]))
  
    def test_multiple_numbers_in_list_true2222(self):
        self.assertTrue(solution.powers_of_two_remain([10, 8, 2, 12]))

    def test_multiple_numbers_in_list_true22222(self):
        self.assertTrue(solution.powers_of_two_remain([1, 2, 3, 4, 5, 6, 7, 8]))

    def test_multiple_numbers_in_list_false2222323(self):
        self.assertFalse(solution.powers_of_two_remain([1, 1, 2, 2, 4, 4]))

    def test_multiple_numbers_in_list_true22222222(self):
        self.assertTrue(solution.powers_of_two_remain([7,4,16,8,4,8])) 

if __name__ == '__main__':
    unittest.main()
