from quizz import question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for Question in question_data:
    question_text = Question["text"]
    question_answer = Question["answer"]
    new_question = question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizzBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()