import smtplib
from email.mime.text import MIMEText #Allows us to send html text emails


def send_mail(customer, dealer, rating, comments):
	#set by mailtrap.io
	port=2525
	smtp_server = 'smtp.mailtrap.io'
	user = '495e5fe88cde55'
	password = '393dbe5ec8aca0'
	message = f"<h3>New Feedback Submition</h3>\
	<ul>\
	<li>Customer: {customer}</li>\
	<li>Dealer: {dealer}</li>\
	<li>Rating: {rating}</li>\
	<li>Comments: {comments}</li>\
	</ul>"

	sender_email = 'sender@example.com'
	receiver_email = 'receiver@gmail.com'
	msg = MIMEText(message, 'html')
	msg['Subject'] = 'Lexus Feedback'
	msg['From'] = sender_email
	msg['To'] =receiver_email
    
	#Send email
	with smtplib.SMTP(smtp_server, port) as server:
		server.login(user, password)
		server.sendmail(sender_email, receiver_email, msg.as_string())