from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')

def home():
	return render_template('home.html', thing = 'box', height = '10', color = 'green')

app.run(port=5000, debug=True)
