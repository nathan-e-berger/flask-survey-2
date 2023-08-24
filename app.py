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
    #q_num = 0
    #question = survey.questions[q_num]
    # q_num = request.args["q_num"]
    redirect("/questions/0")
   # q_num+=1

    return render_template("question.html")

@app.post("/questions/<int:q_num>")