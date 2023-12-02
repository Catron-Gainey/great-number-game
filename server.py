from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

@app.route('/index')
def show_main_page():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_action():
    random_number = random.randint(1, 100)
    changed_random_number = int(request.form['typed_guess'])
    # if request.form['typed_guess'] < random_number:
    if changed_random_number < random_number:
        return redirect('/after/guess/low')
    # if request.form['typed_guess'] > random_number:
    if changed_random_number > random_number:
        return redirect('/after/guess/high')

@app.route('/after/guess/low')
def after_guess_action_low():
    return render_template('after_guess_low.html')

@app.route('/after/guess/high')
def after_guess_action_high():
    return render_template('after_guess_high.html')

if __name__ == "__main__":
    app.run(debug=True)

