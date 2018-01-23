def test_app():
	import random
	from test_questions import test_questions
    num = random.randint(0, 101)
    question = test_questions[num]

    return question
