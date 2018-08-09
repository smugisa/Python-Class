import unittest
from sign_up import *
    
    
class Tests(unittest.TestCase):

    def setUp(self):
        self.one = SignUP('stephen', 'mugisa', 'smugisa3@gmail.com')

    def test_full_name(self):
        self.assertEqual(self.one.full_name(), 'stephen mugisa')

    def test_submit(self):
        SignUP.submit(self.one)
        self.assertEqual(SignUP.users[0], ['stephen', 'mugisa', 'smugisa3@gmail.com'])

    def test_validate_email(self):
        self.assertTrue(validate_email('se@gmail.com'))

    def test_invalidate_email(self):
        self.assertFalse(validate_email('segmail.com'))
        

if __name__ == '__main__':
    unittest.main()


        


