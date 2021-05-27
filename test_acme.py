import unittest

from acme import Employee

class TestAcme(unittest.TestCase):
    
    def test_rene(self):
        """Test Rene payment
        """
        input_data = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        employee = Employee(input_data)
        self.assertEqual(employee.pay(), "The amount to pay RENE is: 215 USD")

    def test_astrid(self):
        """Test Astrid payment
        """
        input_data = "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
        employee = Employee(input_data)
        self.assertEqual(employee.pay(), "The amount to pay ASTRID is: 85 USD")

    def test_night_owl(self):
        """Test Night Owl payment
        """
        input_data = "NIGHTOWL=MO23:00-00:00,SU23:00-00:00"
        employee = Employee(input_data)
        self.assertEqual(employee.pay(), "The amount to pay NIGHTOWL is: 45 USD")

    def test_coffee_lover(self):
        """Test Coffee Lover payment
        """
        input_data = "COFFEELOVER=MO08:00-19:00,SA00:01-00:00"
        employee = Employee(input_data)
        self.assertEqual(employee.pay(), "The amount to pay COFFEELOVER is: 780 USD")
    
    def test_new_employee(self):
        """Test New Employee payment
        """
        input_data = "NEWEMPLOYEE=MO03:00-23:00,SA02:00-19:00"
        employee = Employee(input_data)
        self.assertEqual(employee.pay(), "The amount to pay NEWEMPLOYEE is: 20 USD")


if __name__ == '__main__':
    unittest.main()