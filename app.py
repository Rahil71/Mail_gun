from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from time import time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rahilss2003@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('gmail_password')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user_email = request.form.get('email')
        user_subject = request.form.get('subject')
        user_body = request.form.get('body')
        # print(user_email, " ", user_subject, " ", user_body)
        msg = Message(user_subject, sender='rahilss2003@gmail.com', recipients=[user_email])
        msg.body = user_body
        mail.send(msg)
        return render_template('index.html',current_time=time)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
