import unittest
from Employee_Class import Employee

class Test_employee(unittest.TestCase) :

    def setUp(self) :
        self.new_worker = Employee("Tom", "Thumb", 50000)

    def test_give_default_raise (self) :
        self.new_worker.give_raise()
        result = self.new_worker.get_salary()
        self.assertEqual(result,51000)

    def test_give_custom_raise (self) :
        self.new_worker.give_raise(0.05)
        result = self.new_worker.get_salary()
        self.assertEqual(result,52500)

unittest.main()
