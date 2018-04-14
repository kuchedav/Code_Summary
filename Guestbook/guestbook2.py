from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>He There</h1>'


@app.route('/homeParam/<place>')
def homeParam(place):
	return '<h1>you are on the '+ place +' Homepage</h1>'


@app.route('/home', methods = ['GET'])
def home():
	links = ["https://www.youtube.com","https://www.google.com"]
	return render_template('example.html', myvar = "WayneTest", links = links)


@app.route('/wayne', methods = ['GET'])
def wayne():
	return render_template('Test 2/index.html')

if __name__=='__main__':
	app.run(debug=True)