from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open("web_server/database.csv", mode='a', newline='') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(f'{email}, {subject}, {message}')
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank you.html')
        except:
            return 'didn\'t save to database'
    else:
    	return 'Something went wrong.'
