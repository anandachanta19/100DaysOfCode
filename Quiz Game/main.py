from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random


question_bank = []
for element in question_data:
    question_bank.append(Question(element["text"], element["answer"]))

random.shuffle(question_bank)

quiz = QuizBrain(question_bank)
decision = input("Do you wanna play the quiz? (Type yes/no): ")

while decision == "yes":
    eligible = True
    while eligible:
        eligible = quiz.next_question()
    decision = "no"

print("You have Completed the quiz!")