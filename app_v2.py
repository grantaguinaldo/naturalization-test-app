from flask import Flask
app = Flask(__name__)

@app.route("/")

def test():

	import random
	from test_questions import test_questions
	
	num = random.randint(0, 100)
	question = test_questions[num]
	
	return question

if __name__ == "__main__":
	app.run()
