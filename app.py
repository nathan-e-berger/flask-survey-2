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
    #title = survey[]
    return render_template("survey_start.html")

@app.post("/begin")
def show_question():
    responses = []

    question = survey.questions[0]
    redirect("/questions/0")

    return render_template("question.html", question=question)


@app.get("/questions/<int:q_num>")
def show_next_question(q_num):
    q_num+=1
    question = survey.questions[q_num]
    return render_template("question.html", question = question)

@app.post("/answer")
def save_answer():
    response = request.form.get("answer")
    responses.append(response)

    return redirect(f"/questions/{len(responses)}")

