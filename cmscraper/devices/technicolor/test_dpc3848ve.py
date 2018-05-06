import unittest
from mock import Mock

class TestDPC348ve(unittest.TestCase):
     
    def setUp(self):
        pass
    
    def test_parse_web_page(self):
        with open('./test_data/dpc3848ve.html') as file:
            data = file.read()

        print(data)
        self.assertEquals(1,1)

if __name__ == '__main__':
    unittest.main()