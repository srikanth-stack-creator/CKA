from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('survey_questions.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Assuming some validation is done here before saving questions

    # Create an array to store survey questions
    survey_questions = {
        'question1': request.form['question1'],
        'question2': request.form['question2'],
        'question3': request.form['question3']
        # Add more questions as needed
    }

    # Convert the dictionary to JSON
    survey_questions_json = json.dumps(survey_questions, indent=2)

    # Save survey questions to a file in the container
    with open('/app/survey_questions.json', 'w') as file:
        file.write(survey_questions_json)

    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

