from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author': 'Dipak',
		'title' : 'Docker in Nutshell',
		'content': 'A container technology.',
		'date_posted': 'March 20 2019'
	},
	{
		'author': 'Tandel',
		'title' : 'Static code analysis using Jenkins',
		'content': 'Static code analysis is used to find issues in the code whicj are known.',
		'date_posted': 'March 20 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')


if __name__ == '__main__':
	app.run()
