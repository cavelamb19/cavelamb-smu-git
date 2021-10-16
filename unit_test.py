import unittest
from app import Employee


class TestEmployee(unittest.TestCase):
    def testemployee(self):
        employee = Employee(staffID = 1, Name = 'Phris Coskitt', Username = 'csok', Email = 'csoki@gmail.com', 
        CurrentDesignation = 'administrator', Department ='hr', ContactNo = '90227823')
        self.assertEqual(employee.json(), {
            'staffID' : 1,
            'Name' : 'Phris Coskitt',
            'Username' : 'csok',
            'Email' : 'csoki@gmail.com',
            'CurrentDesignation' : 'administrator',
            'Department' : 'hr',
            'ContactNo' : '90227823'
        })

    
        
    
