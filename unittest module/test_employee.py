import unittest
from employee import Employee


class testEmployee(unittest.TestCase):

    # setUpClass : its code run at very begining of the test file
    @classmethod
    def setUpClass(cls):
        print('setUpClass\n')


    # tearDownClass : its cleanup code runs after all the test have been run
    # Run once before anything
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    # setUp : run its code before ever single test
    # Run once after everything 
    def setUp(self):
        print('SetUp')
        self.emp1 = Employee('Nikita', 'Patil', 50000)
        self.emp2 = Employee('Rohan', 'More', 60000)
    
    # tearDown : run its code after every single test
    def tearDown(self):
        print('tearDown\n')   

    def test_email(self):
        print('email')
        self.assertEqual(self.emp1.email,'Nikita.Patil@email.com')
        self.assertEqual(self.emp2.email,'Rohan.More@email.com')

        self.emp1.first = 'XYZ'
        self.emp1.last = 'AAA'

        self.assertEqual(self.emp1.email,'XYZ.AAA@email.com')
   

    def test_fullName(self):
        print('fullName')
        self.assertEqual(self.emp1.fullname,'Nikita Patil')
        self.assertEqual(self.emp2.fullname,'Rohan More')


    def test_apply_raise(self):
        print('apply_raise')
        self.assertEqual(self.emp1.pay,50000)
        self.assertEqual(self.emp2.pay,60000)


if __name__ == '__main__':
    unittest.main()