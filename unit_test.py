import unittest
from app import Administrator, Employee, Learner, Trainer, Course, Classes 


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

class TestLearner(unittest.TestCase):
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

class TestTrainer(unittest.TestCase):
    def testtrainer(self):
        trainer = Trainer(StaffID = 2, Name = 'Arnold de Mari', Username = 'Dr', Email = 'Dr@gmail.com',
        CurrentDesignation = 'trainer', Department = 'Training', ContactNo = '82329832', coursesTeaching = 'IS212')
        self.assertEqual(trainer.to_dict(), {
            'StaffID' : 2,
            'id' : None,
            'Name' : 'Arnold de Mari',
            'Username' : 'Dr',
            'Email' : 'Dr@gmail.com',
            'CurrentDesignation' : 'trainer',
            'Department': 'Training',
            'ContactNo' : '82329832',
            'coursesTeaching' : 'IS212'
        })

class TestCourse(unittest.TestCase):
    def testcourse(self):
        course = Course(courseID = 1, courseName = 'Software Project Management', courseDesc = 'agile methods',
        preRequisites = 'NULL' ,classesID = '1')
        self.assertEqual(course.json(), {
            'courseID' : 1,
            'courseName' : 'Software Project Management',
            'courseDesc' : 'agile methods',
            'preRequisites' : 'NULL',
            'classesID' : 1
        })

class Testclasses(unittest.TestCase):
      def testclasses(self):
          classes= Classes(classesID= 1, startDate="2021-10-18", startTime="2021-10-18 06:30:00", 
          endDate="2021-11-18", endTime="2021-11-18 06:30:00", classesSize= 50, trainerAssigned="Arnold de Mari")
          self.assertEqual(classes.json(), {
              'classesID' : 1,
              'startDate' : '2021-10-18',
              'startTime' : '2021-10-18 06:30:00',
              'endDate' : '2021-11-18',
              "endTime" : '2021-11-18 06:30:00',
              "classesSize" : 50,
              "trainerAssigned" : 'Arnold de Mari',
          })


    
        
    
