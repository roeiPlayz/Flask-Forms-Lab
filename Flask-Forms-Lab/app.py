from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


#username = "roeireem"
#password = "roei123"
#facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	username = "roeireem"
	password = "roei123"
	facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

	if request.method == 'POST':
		if username == request.form['username'] and password == request.form['password']:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')
  

@app.route('/home')
def home():
	facebook_friends=["Mom","Dad","Grandma", "Friend 1", "Friend 2", "Friend 3"]
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:friend>', methods = ['GET', 'POST'])
def friend_exists(friend):
	facebook_friends=["Mom","Dad","Grandma", "Friend 1", "Friend 2", "Friend 3"]
	return render_template('friend_exists.html',friends = facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)