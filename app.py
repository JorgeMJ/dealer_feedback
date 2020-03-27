from flask import Flask, render_template, request	
from flask_sqlalchemy import SQLAlchemy #For the DB
from send_mail import send_mail


#Initialize the app
app = Flask(__name__)

#Define DB localion (URI). TO Conect to the DB
ENV = 'prod'
#ENV = 'dev'

if ENV == 'dev':
	#We work on DEVELOPMENT database
	#Because we are in DEVELOPMENT we want the server to keep reloadiing
	app.debug = True
	#Set the URI for the database.
	#{Found in the SQLAlchemy documentation}
	#'postgresql://[DB_OWNER_IN pgAdmin]:[PASSWORD_OF SUPERUSER]@localhost/[DB_NAME]'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/lexus'
else:
	#Because we are in PRODUCTION we want the server to keep reloadiing
	app.debug = False
    #We work on PRODUCTION database 
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oubzhlrizhkwuh:8b0c613182c398a513a3b83934b7cf80689664d10435980cef790243f8fcf698@ec2-23-22-156-110.compute-1.amazonaws.com:5432/dfvah62ttr9emo'

#To avoid a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#Create the DB object to play with it
db = SQLAlchemy(app)

#To play with the DB we do it via Models. This are classes
class Feedback(db.Model):
	__tablename__ = 'feedback'
	#define the fields of the table
	id = db.Column(db.Integer, primary_key=True)
	customer = db.Column(db.String(200), unique=True)
	dealer = db.Column(db.String(200))
	rating = db.Column(db.Integer)
	comments = db.Column(db.Text())

	#Constructor: Sets the initial value of the instance variables 
	def __init__(self, customer, dealer, rating, comments):
		self.customer = customer
		self.dealer = dealer
		self.rating = rating
		self.comments = comments

#Create a route from the homepage (which is /)
@app.route('/')
#Render our template
def index():
	return render_template('index.html')

#Handle the submition of the form (in index.html '<form>' has the action 'submit' via the method 'POST')
@app.route('/submit', methods=['POST', 'GET'])
def submit():
	#Makes sure this action append under the POST request
	if request.method == 'POST':
		#Gathers info form the form (checks the fields with the 'names' specified below)
		customer = request.form['customer']
		dealer = request.form['dealer']
		rating = request.form['rating']
		comments = request.form['comments']
		#if info is not complete
		if customer == '' or dealer == '':
			#Creates and renders 'message'. 
			return render_template('index.html', message = '***Please enter the required fields.***')
		
		#Checks the same customer doesn't submit more than one feddback.
		if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
			data = Feedback(customer, dealer, rating, comments)
			db.session.add(data)
			db.session.commit()
			send_mail(customer, dealer, rating, comments)
			return render_template('success.html')
		return render_template('index.html', message = 'You have already submitted feedback.')

	elif request.method == 'GET':
		listComments = Feedback.query.all()
		return render_template('list_comments.html', comments = listComments)

if __name__ == "__main__":
	#Run server
	app.run()