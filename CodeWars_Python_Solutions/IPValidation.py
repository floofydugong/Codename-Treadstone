import re
import unittest

def is_valid_IP(string):
    if re.match(r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]0|[1-9]{2}|[1-9])\.(25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[1-9]0\.|[1-9]{2}\.|[0-9]\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]0|[1-9]{2}|[0-9])$',string):
        return(True)
    else:
        return(False)

is_valid_IP('105.255.255.255')

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_valid_IP('12.255.56.1'),True)
        self.assertEqual(is_valid_IP(''), False)
        self.assertEqual(is_valid_IP('abc.def.ghi.jkl'),False)
        self.assertEqual(is_valid_IP('123.456.789.0'),  False)
        self.assertEqual(is_valid_IP('12.34.56'),       False)
        self.assertEqual(is_valid_IP('12.34.56 .1'),    False)
        self.assertEqual(is_valid_IP('12.34.56.-1'),    False)
        self.assertEqual(is_valid_IP('123.045.067.089'),False)
        self.assertEqual(is_valid_IP('240.0.72.150'),True)

if __name__ == '__main__':
    unittest.main()
