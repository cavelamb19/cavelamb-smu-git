import unittest
from app import Administrator, Employee, Learner, Trainer, Course, Classes, Lesson


class TestEmployee(unittest.TestCase):
    def testemployee(self):
        employee = Employee(StaffID = 1, Name = 'Henry loh', Username = 'hen', Email = 'henlow@gmail.com', 
        CurrentDesignation = 'Hr', Department ='hr', ContactNo = '90227823', Role = 'Administrator')
        self.assertEqual(employee.to_dict(), {
            'StaffID' : 1,
            'Name' : 'Henry loh',
            'Username' : 'hen',
            'Email' : 'henlow@gmail.com',
            'CurrentDesignation' : 'Hr',
            'Department' : 'hr',
            'ContactNo' : '90227823',
            'Role' : 'Administrator'
        })
        

        

class TestLearner(unittest.TestCase):
    def testlearner(self):
        learner = Learner(StaffID = 3, Name = 'Constance Tan', Username = 'cons', Email = 'constan@gmail.com',
        CurrentDesignation = 'Engineer', Department = 'Learning', ContactNo = '92130843',CompletedCourses = 'IS214')
        self.assertEqual(learner.to_dict(), {
            'StaffID' : 3,
            'id' : None,
            'Name' : 'Constance Tan',
            'Username' : 'cons',
            'Email' : 'constan@gmail.com',
            'CurrentDesignation' : 'Engineer',
            'Department': 'Learning',
            'ContactNo' : '92130843',
            'CompletedCourses' : 'IS214',
            'CoursesAssigned': None,
            'CoursesEnrolled': None,
            'Role': None
                       
        })

class TestTrainer(unittest.TestCase):
    def testtrainer(self):
        trainer = Trainer(StaffID = 2, Name = 'Roger Ng', Username = 'Rog', Email = 'Rogng@gmail.com',
        CurrentDesignation = 'Senior Engineer', Department = 'Training', ContactNo = '82329832', coursesTeaching = 'IS212 Software Project Management G2')
        self.assertEqual(trainer.to_dict(), {
            'StaffID' : 2,
            'id' : None,
            'Name' : 'Roger Ng',
            'Username' : 'Rog',
            'Email' : 'Rogng@gmail.com',
            'CurrentDesignation' : 'Senior Engineer',
            'Department': 'Training',
            'ContactNo' : '82329832',
            'coursesTeaching' : 'IS212 Software Project Management G2',
            'Role': None
        })

class TestCourse(unittest.TestCase):
    def testcourse(self):
        course = Course(courseID = 1, courseName = 'Software Project Management', courseDesc = 'agile methods',
        preRequisites = 'NULL' ,classesID = 1)
        self.assertEqual(course.json(), {
            'courseID' : 1,
            'courseName' : 'Software Project Management',
            'courseDesc' : 'agile methods',
            'preRequisites' : 'NULL',
            'classesID' : 1
        })

class Testclasses(unittest.TestCase):
    def testclasses(self):
        classes= Classes(classesID= 1, startDate="August 18 2021", startTime="8am", 
        endDate="November 5 2021", endTime="12pm", classesSize= 40, trainerAssigned="Roger Ng", currentEnrolled=0)
        self.assertEqual(classes.json(), {
            'classesID' : 1,
            'startDate' : 'August 18 2021',
            'startTime' : '8am',
            'endDate' : 'November 5 2021',
            "endTime" : '12pm',
            "classesSize" : 40,
            "trainerAssigned" : 'Roger Ng',
            "currentEnrolled" : 0
        })

class Testclassessize(unittest.TestCase):
    def increaseclasssize(self):
        classes= Classes(classesID= 1, startDate="August 18 2021", startTime="8am", 
        endDate="November 5 2021", endTime="12pm", classesSize= 40, trainerAssigned="Roger Ng", currentEnrolled=0)
    
        self.assertEqual(classes.json(), {
            'classesID' : 1,
            'startDate' : 'August 18 2021',
            'startTime' : '8am',
            'endDate' : 'November 5 2021',
            "endTime" : '12pm',
            "classesSize" : 40,
            "trainerAssigned" : 'Roger Ng',
            "currentEnrolled" : 0
        })

        size = classes.increaseclasssize(1)
        self.assertEqual(classes.currentEnrolled, 1)
        #self.assertEqual(size, 4)
