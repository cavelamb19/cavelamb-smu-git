import unittest
import flask_testing
import json
from app import app, db, Trainer, Learner, Administrator, Course, Classes, Lesson, Quiz, Quizscore, QuestionTrueFalse


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
        
        
class TestCreateTrueFalseQuestion(TestApp):
      
      def test_create_True_False_question(self):
        
          q1 = QuestionTrueFalse(
              qnID=None, qn="Software Project Management module will teach you about agile process",
              ans="True", quizID=1)
          
          
          db.session.add(q1)
          db.session.commit()
          
          request_body = {
              'question': q1.qn,
              'answer': q1.ans,
              'lessonID': q1.quizID,
              
          }
          
          response = self.client.post("/addquestiontruefalse",
                                      data=json.dumps(request_body),
                                    content_type='application/json')
          
          self.assertEqual(response.status_code, 200)
         
         
