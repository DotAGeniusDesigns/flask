from flask import Flask, render_template, redirect, request, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"
toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_survey_start():
    """Shows the survey start page"""
    session['responses'] = []
    return render_template("survey_start.html", survey=surveys['satisfaction'])

@app.route('/begin', methods=["POST"])
def start_survey():
    """Clears responses and goes back to beginning"""
    session['responses'] = []
    return redirect("/questions/0")

@app.route('/questions/<int:qid>')
def show_question(qid):
    """Shows the current question"""
    responses = session.get("responses", [])

    if qid != len(responses):
        flash("Invalid question.", "error")
        return redirect(f"/questions/{len(responses)}")
    
    question = surveys['satisfaction'].questions[qid]
    return render_template("question.html", question_num=qid, question=question)

@app.route('/answer', methods=["POST"])
def handle_answer():
    """Saves responses and moves on to next question"""
    answer = request.form.get('answer')
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses
    
    if len(responses) == len(surveys['satisfaction'].questions):
        return redirect("/thankyou")
    else:
        return redirect(f"/questions/{len(responses)}")
    
@app.route('/thankyou')
def show_thankyou():
    """Shows the thank you page"""
    return render_template("thankyou.html")

if __name__ == '__main__':
    app.run(debug=True)
