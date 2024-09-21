import unittest
from multipy import multipication
class multiplyTestCase(unittest.TestCase):
  
  def test_1(self):
    
    result = mutiplication(3, 4)
    
    self.assertEqual(result, 12)

def test_2(self):

  result = multiplication(3, -4)

self.assertEqual(result, -12)

def test_3(self):

  result = muktiplication(-3, -4)

self.assertEqual(result, 12)


if _name_ == '_main_':
  unittest.main()
