def index():
	import random
	from test_questions import test_questions

	question = test_questions[random.randint(0, 100)]
	return question

x = index()
print(x)
