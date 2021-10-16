import unittest
from app import Employee, Learner


class TestEmployee(unittest.TestCase):
    def testemployee(self):
        employee = Employee(staffID = 1, Name = 'Phris Coskitt', Username = 'csok', Email = 'csoki@gmail.com', 
        CurrentDesignation = 'administrator', Department ='hr', ContactNo = '90227823')
        self.assertEqual(employee.to_dict(), {
            'staffID' : 1,
            'Name' : 'Phris Coskitt',
            'Username' : 'csok',
            'Email' : 'csoki@gmail.com',
            'CurrentDesignation' : 'administrator',
            'Department' : 'hr',
            'ContactNo' : '90227823'
        })

class Testlearner(unittest.TestCase):
    def testlearner(self):
        learner = Learner(Name = 'Constance Wilkinson', CoursesTaking = 'IS212', CompletedCourses = 'IS214')
        self.assertEqual(learner.to_dict(), {
            'Name' : 'Constance Wilkinson',
            'CoursesTaking' : 'IS212',
            'CompletedCourses' : 'IS214'
        })



    
        
    
