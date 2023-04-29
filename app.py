from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secret-key"

responses = []

@app.route('/')
def home_page():
	"""Shows home page displaying user, title of the survey, instructions, and a button to start survey."""
	title = satisfaction_survey.title
	instructions = satisfaction_survey.instructions
	
	return render_template('home_page.html', title=title, instructions=instructions)

@app.route('/questions/<int:id>')
def show_question(id):
	"""Shows a form asking current question and listing choices"""
	
	question = satisfaction_survey.questions[id].question
	choices = satisfaction_survey.questions[id].choices

	return render_template('question.html', question=question, choices=choices, id=id)


@app.route('/answer', methods=["POST"])
def show_answer():
	"""Shows answer that the use selected."""
	answer = request.form['answer'] #stores value of selected radio button (i.e. Yes)
	responses.append(answer)

	return redirect(f'/questions/{len(responses)}')





# @app.route('/questions/<int:id>', methods=["POST"])
# def show_answer(id):
# 	"""Shows answer that the use selected."""
# 	answer = request.form['answer'] #stores value of selected radio button (i.e. Yes)
# 	responses.append(answer)

# 	# return redirect('questions/<int:id> + 1')

# 	return f"""
# 		<p>your saved answer is {answer}</p>
# 	"""

	
	



