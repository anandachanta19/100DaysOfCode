class QuizBrain:

    def __init__(self, qlist):
        self.question_number = 0
        self.score = 0
        self.question_list = qlist

    def next_question(self):
        if self.question_number == len(self.question_list) and self.score == self.question_number+1:
            print("Wow! You are a genius..")
            return False
        answer = input(f"Q.{self.question_number + 1} {self.question_list[self.question_number].question} (True/False): ")
        if answer == self.question_list[self.question_number].answer:
            self.score += 1
            print(f"That's Correct! Your Score is {self.score}/{self.question_number + 1}")
            self.question_number += 1
            print("Heading towards the next question.")
            return True
        else:
            print("uh uh! Its a wrong one... ")
            print(f"The correct answer is {self.question_list[self.question_number].answer}")
            print("Your Score is {self.score}/{self.question_number + 1}")

