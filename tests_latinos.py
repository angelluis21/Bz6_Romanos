import unittest
from romanos import *
import unittest


class RomanosTest(unittest.TestCase):

    def test_1970(self):
        self.assertEqual(entero_a_romano(1970), 'MCMLXX')


if __name__ == '__main__':
    unittest.main()    

