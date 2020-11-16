import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_1970(self):
        self.assertequal(entero_a_romano(1970), 'MCMLZZ')


if __name__ == '__main__':
    unittest.main()
