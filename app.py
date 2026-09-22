from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "Which language is used to structure a webpage?",
        "options": ["css", "html", "javascript", "python"],
        "answer": "html"
    },

    {
        "question": "Which language is used to style the webpage?",
        "options": ["html", "css", "javascript", "python"],
        "answer": "css"
    },

    {
        "question": "Which language is mainly used to make webpage interactive?",
        "options": ["html", "css", "javascript", "python"],
        "answer": "javascript"
    },

    {
        "question": "Which framework is used in the project?",
        "options": ["java", "Flask", "flask", "python"],
        "answer": "Flask"
    },

    {
        "question": "Which method is commonly used to send form data to a Flask server?",
        "options": ["GET", "POST", "PUSH", "SEND"],
        "answer": "POST"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    score = 0

    for i, question in enumerate(questions):
        user_answer = request.form.get(f"questions{i}")

        if user_answer == question["answer"]:
            score += 1

    total = len(questions)

    percentage = (score / total) * 100

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage
    )


if __name__ == "__main__":
    app.run(debug=True)