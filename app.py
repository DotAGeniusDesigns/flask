from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def index():
    """HTML form to get the words"""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route('/story')
def generate_story():
    """Generates the story with the given words"""
    answers = request.args
    result_story = story.generate(answers)
    return render_template("story.html", story=result_story)

if __name__ == '__main__':
    app.run(debug=True)