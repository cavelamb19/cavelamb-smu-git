import unittest
from app import Employee, Learner


class TestEmployee(unittest.TestCase):
    def testemployee(self):
        employee = Employee(StaffID = 1, Name = 'Phris Coskitt', Username = 'csok', Email = 'csoki@gmail.com', 
        CurrentDesignation = 'administrator', Department ='hr', ContactNo = '90227823')
        self.assertEqual(employee.to_dict(), {
            'StaffID' : 1,
            'Name' : 'Phris Coskitt',
            'Username' : 'csok',
            'Email' : 'csoki@gmail.com',
            'CurrentDesignation' : 'administrator',
            'Department' : 'hr',
            'ContactNo' : '90227823'
        })

class Testlearner(unittest.TestCase):
    def testlearner(self):
        learner = Learner(StaffID = 3, Name = 'Constance Wilkinson', Username = 'cons', Email = 'cons@gmail.com',
        CurrentDesignation = 'learner', Department = 'Learning', ContactNo = '92130843', CoursesTaking = 'IS212', CompletedCourses = 'IS214')
        self.assertEqual(learner.to_dict(), {
            'StaffID' : 3,
            'id' : None,
            'Name' : 'Constance Wilkinson',
            'Username' : 'cons',
            'Email' : 'cons@gmail.com',
            'CurrentDesignation' : 'learner',
            'Department': 'Learning',
            'ContactNo' : '92130843',
            'CoursesTaking' : 'IS212',
            'CompletedCourses' : 'IS214'
            
        })



    
        
    
