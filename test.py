import unittest
import main

class TestMain(unittest.TestCase):
    def test1(self):
        test_param = 1
        result = main.guess_number(test_param,1)
        self.assertEqual(result, True)




    print('ran this bitch')
    unittest.main()
