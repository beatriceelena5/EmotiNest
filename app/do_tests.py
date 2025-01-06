from flask import Blueprint, render_template, request, flash, redirect, url_for

# Definește blueprint-ul do_tests
do_tests = Blueprint('do_tests', __name__)

@do_tests.route('/')
def index():
	return render_template('do_tests/index.html')

@do_tests.route('/adhd')
def adhd_test():
	return render_template('do_tests/adhd_test.html')

@do_tests.route('/depression')
def depression_test():
	return render_template('do_tests/depression_test.html')

@do_tests.route('/anxiety')
def anxiety_test():
	return render_template('do_tests/anxiety_test.html')

@do_tests.route('/burnout')
def burnout_test():
	return render_template('do_tests/burnout_test.html')

@do_tests.route('/submit_adhd_test', methods=['POST'])
def submit_adhd_test():
	question1 = request.form.get('question1')
	question2 = request.form.get('question2')
	question3 = request.form.get('question3')
	question4 = request.form.get('question4')
	question5 = request.form.get('question5')
	# Adaugă mai multe întrebări aici

	flash('Your ADHD test has been submitted successfully. Please consult a specialist for further evaluation.', 'success')
	return redirect(url_for('do_tests.adhd_test'))

@do_tests.route('/submit_depression_test', methods=['POST'])
def submit_depression_test():
	# Logic similar pentru testul de depresie
	question1 = request.form.get('question1')
	question2 = request.form.get('question2')
	question3 = request.form.get('question3')
	question4 = request.form.get('question4')
	question5 = request.form.get('question5')

	flash('Your Depression test has been submitted successfully.', 'success')
	return redirect(url_for('do_tests.depression_test'))

@do_tests.route('/submit_anxiety_test', methods=['POST'])
def submit_anxiety_test():
	# Logic similar pentru testul de anxietate
	question1 = request.form.get('question1')
	question2 = request.form.get('question2')
	question3 = request.form.get('question3')
	question4 = request.form.get('question4')
	question5 = request.form.get('question5')

	flash('Your Anxiety test has been submitted successfully.', 'success')
	return redirect(url_for('do_tests.anxiety_test'))

@do_tests.route('/submit_burnout_test', methods=['POST'])
def submit_burnout_test():
	question1 = request.form.get('question1')
	question2 = request.form.get('question2')
	question3 = request.form.get('question3')
	question4 = request.form.get('question4')

	# Logic similar pentru testul de burnout
	flash('Your Job Burnout test has been submitted successfully.', 'success')
	return redirect(url_for('do_tests.burnout_test'))
