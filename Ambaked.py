from flask import Blueprint, render_template

als = Blueprint('als', __name__)

@als.route('/login')
def home():
	return render_template("login.html")
	
	@als.route('/logout')
def home():
	return render_template("logout.html")
	
	@als.route('/signup')
def home():
	return render_template("signup.html")