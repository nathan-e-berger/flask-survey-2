from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get("/")
def show_homepage():
    survey_title = survey.title
    return render_template("survey_start.html", survey_title=survey_title)

@app.post("/begin")
def show_question():
    responses.clear()
    return redirect("/questions/0")


@app.get("/questions/<int:q_num>")
def show_next_question(q_num):
    question = survey.questions[q_num]
    return render_template("question.html", question = question)

@app.post("/answer")
def save_answer():
    response = request.form.get("answer")
    responses.append(response)

    if len(responses) == len(survey.questions):
        return redirect("/completion")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.get("/completion")
def show_completion():
    questions = survey.questions
    qa_dict = {}
    for i in range(len(responses)):
        qa_dict[questions[i]] = responses[i]

    return render_template("completion.html", qa_dict=qa_dict)
