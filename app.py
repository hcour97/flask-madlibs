from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

@app.route("/")
def index():
    '''Homepage, where user is asked questions for madlibs'''

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)

@app.route("/story") 
def write_story():
    '''Displays mad lib story with user's inputs'''

    text = story.generate(request.args)
    return render_template("stories.html", text=text)