from flask import Flask, request , redirect
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(50), nullable=False, unique=True)
	password = db.Column(db.String(150),nullable=False)

db.create_all()

@app.route('/', methods=['GET'])
def index():
	return'''
 <!DOCTYPE html>   
    <html>   
    <head>  
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title> Index</title> 

    </head>
    <body>	
		<h1>Praca dom nr.4  :)</h1>
		<a href="http://127.0.0.1:9999/login">Login</a></br>
		<a href="http://127.0.0.1:9999/register">Register</a>
    </body>
    </html>    
	'''

@app.route('/login', methods=['GET'])
def login_page():
	return '''
    <!DOCTYPE html>   
    <html>   
    <head>  
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title> Login Page </title>  
    <style>   
    Body {  
      font-family: Calibri, Helvetica, sans-serif;  
      background-color: pink;  
    }  
    button {   
           background-color: black;   
           width: 100%;  
            color: orange;   
            padding: 15px;   
            margin: 10px 0px;   
            border: none;   
            cursor: pointer;   
             }   
     form {   
            border: 3px solid #f1f1f1;   
        }   
     input[type=text], input[type=password] {   
            width: 100%;   
            margin: 8px 0;  
            padding: 12px 20px;   
            display: inline-block;   
            border: 2px solid green;   
            box-sizing: border-box;   
        }  
     button:hover {   
            opacity: 0.7;   
        }   
      .cancelbtn {   
            width: auto;   
            padding: 10px 18px;  
            margin: 10px 5px;  
        }   
            
         
     .container {   
            padding: 25px;   
            background-color: lightblue;  
        }   
    </style>   
    </head>    
    <body>    
        <center> <h1> Student Login Form </h1> </center>   
        <form action="/login" method="POST">  
            <div class="container">   
                <label for="login">Username : </label>   
                <input type="text" name="login" id="login" placeholder="Enter Username" required>  
                <label for="password">Password : </label>   
                <input type="password" name="password" id="password" placeholder="Enter Password" required>  
                <button type="submit">Login</button>   
                <input type="checkbox" checked="checked"> Remember me   
                <button type="button" class="cancelbtn"> Cancel</button>   
                Forgot <a href="https://www.techadvisor.com/how-to/security/how-use-password-manager-3787399/"> password? </a>   
            </div>   
        </form>     
    </body>     
    </html>  
	'''
@app.route('/login', methods=['POST'])
def login():
	login = request.form.get('login')
	password = request.form.get('password')
	user = User.query.filter_by(login=login, password=password).first()

	if user:
		return f'{user.login} is logged in'
	return 'Invalid credentials'


@app.route('/register', methods=['GET'])

def register_page():
	return '''
<!DOCTYPE html>   
    <html>   
    <head>  
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title> Register page </title>  
    <style>   
    Body {  
      font-family: Calibri, Helvetica, sans-serif;  
      background-color: pink;  
    }  
    button {   
           background-color: black;   
           width: 100%;  
            color: orange;   
            padding: 15px;   
            margin: 10px 0px;   
            border: none;   
            cursor: pointer;   
             }   
     form {   
            border: 3px solid #f1f1f1;   
        }   
     input[type=text], input[type=password] {   
            width: 100%;   
            margin: 8px 0;  
            padding: 12px 20px;   
            display: inline-block;   
            border: 2px solid green;   
            box-sizing: border-box;   
        }  
     button:hover {   
            opacity: 0.7;   
        }   
      .cancelbtn {   
            width: auto;   
            padding: 10px 18px;  
            margin: 10px 5px;  
        }   
            
         
     .container {   
            padding: 25px;   
            background-color: lightblue;  
        }   
    </style>   
    </head>    
    <body>    
        <center> <h1> Register </h1> </center>   
        <form action="/register" method="POST">  
            <div class="container">   
                <label for="login">Username : </label>   
                <input type="text" id="login" name="login" placeholder="Enter Username" required>  
                <label for="password">Password : </label>   
                <input type="password" id="password" name="password" placeholder="Enter Password" required>  
                <button type="submit">Register !</button>   
                <input type="checkbox" checked="checked"> Remember me   
                <button type="button" class="cancelbtn"> Cancel</button>     
            </div>   
        </form>     
    </body>     
    </html>  
	'''
	
@app.route('/register', methods=['POST'])
def register():
	login = request.form.get('login')
	password = request.form.get('password')
	print(login)
	user = User(login=login, password=password)
	db.session.add(user)
	db.session.commit()
	if db.session.commit:
		return "Registration completed" and redirect('http://127.0.0.1:9999/login', code=302)	
	else:
		return "failed"	

if __name__ == "__main__":
	app.run('127.0.0.1', '9999')