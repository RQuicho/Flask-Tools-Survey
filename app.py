from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET KEY'] = "my-secret-key"

responses = []

@app.route('/')
def home_page():
	"""Shows home page displaying user, title of the survey, instructions, and a button to start survey."""
	title = satisfaction_survey.title
	instructions = satisfaction_survey.instructions

	return render_template('home_page.html', title=title, instructions=instructions)


