# sync code space is very high risk, sometimes fail

from flask import Flask
from flask import render_template, request
import textblob
import google.generativeai as genai

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
	return (render_template("index.html"))


@app.route("/main", methods=["GET", "POST"])
def main():
	name = request.form.get("q")
	return (render_template("main.html"))


@app.route("/SA", methods=["GET", "POST"])
def SA():
	return (render_template("SA.html"))


@app.route("/SA_result", methods=["GET", "POST"])
def SA_result():
	q = request.form.get("q")
	r = textblob.TextBlob(q).sentiment
	return (render_template("SA_result.html", r=(r)))


@app.route("/genAI", methods=["GET", "POST"])
def genAI():
	return (render_template("genAI.html"))


@app.route("/genAI_result", methods=["GET", "POST"])
def genAI_result():
	q = request.form.get("q")
	r = ask_gemini(q)
	return (render_template("genAI_result.html", r=(r)))


def ask_gemini(q):
	global model
	r = model.generate_content(q)
	text = r.candidates[0].content.parts[0].text
	return text


if __name__ == "__main__":
	genai.configure(api_key="AIzaSyArko3Tohgwb8plR3FLFvos9RHxFS0cGv0")
	model = genai.GenerativeModel("gemini-1.5-flash")
	app.run(port=1111)