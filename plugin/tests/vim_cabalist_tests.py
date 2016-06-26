import unittest
import vim_cabalist as sut


@unittest.skip("Don't forget to test!")
class VimCabalistTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_cabalist_example()
        self.assertEqual("Happy Hacking", result)
