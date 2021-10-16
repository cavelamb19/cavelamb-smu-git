import unittest

from app import Employee, Learner


class TestEmployee(unittest.TestCase):
    def test_to_dict(self):

        e1 = Employee(StaffID = 3, Name = 'Constance Wilkinson', Username = 'cons', Email = 'cons@gmail.com',
        CurrentDesignation = 'learner', Department = 'Learning', ContactNo = '92130843')
        self.assertEqual(e1.to_dict(), {
            'StaffID' : 3,
            'Name' : 'Constance Wilkinson',
            'Username' : 'cons',
            'Email' : 'cons@gmail.com',
            'CurrentDesignation' : 'learner',
            'Department': 'Learning',
            'ContactNo' : '92130843'}
        )


class TestLearner(unittest.TestCase):
    def test_to_dict(self):
        l1 = Learner(StaffID = 3, Name = 'Constance Wilkinson', Username = 'cons', Email = 'cons@gmail.com',
        CurrentDesignation = 'learner', Department = 'Learning', ContactNo = '92130843', CoursesTaking = 'IS212', CompletedCourses = 'IS214')

        self.assertEqual(l1.to_dict(), {
            'StaffID' : 3,
            'id' : None,
            'Name' : 'Constance Wilkinson',
            'Username' : 'cons',
            'Email' : 'cons@gmail.com',
            'CurrentDesignation' : 'learner',
            'Department': 'Learning',
            'ContactNo' : '92130843',
            'CoursesTaking' : 'IS212',
            'CompletedCourses' : 'IS214'}
        )

if __name__ == "__main__":
    unittest.main()
