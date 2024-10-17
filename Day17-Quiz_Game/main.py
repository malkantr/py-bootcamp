from question_model_trivia import Question
from data_trivia import question_data
from quiz_brain import QuizBrain

question_text_static = "text"
question_answer_static = "answer"

triviadb_url = "opentdb.com"
question_text_trivia = "question"
question_answer_trivia = "correct_answer"

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")