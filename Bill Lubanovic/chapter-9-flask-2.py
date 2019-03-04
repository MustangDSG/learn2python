from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')

def home():
	arg1 = request.args.get("arg1")
	arg2 = request.args.get("arg2")
	arg3 = request.args.get("arg2")
	return render_template('home.html', thing = arg1, height = arg2, color = arg3)

app.run(port=5000, debug=True)

# I'm of course referring to box, which is 10 feet tall and green.
# http://localhost:5000/?arg1=box&arg2=10&arg3=green

