from question_model import Question
from data import *
from quiz_brain import QuizBrain
from ui import *

q = Question_data().question_data


# question_bank = []
# for question in q:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)
screen_UI = QuizInterface()


