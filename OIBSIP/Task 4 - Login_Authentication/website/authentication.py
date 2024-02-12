from flask import Blueprint ,flash, render_template ,redirect,url_for,request
from . import db
from .models import User
from flask_login import login_user,logout_user,login_required , current_user
from werkzeug.security import generate_password_hash,check_password_hash
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
authentication = Blueprint("authentication",__name__)
@authentication.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email") 
        password = request.form.get("password") 
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Log In Successfully','success')
                login_user(user,remember=True)
                return redirect(url_for('view.home'))
            else:
                flash('Incorrect Password','error')
        else:
            flash('Email does not exists','error')
    # print(email)
    # print(password)
    return render_template("login.html",user=current_user)
@authentication.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email") 
        username = request.form.get("username") 
        password1 = request.form.get("password1") 
        password2 = request.form.get("password2") 
    # print(email,username,password1,password2)
        exists1 = User.query.filter_by(email = email).first()
        exists2 = User.query.filter_by(username=username).first()
        if exists1:
            flash('Email already exists','error')
        elif exists2:
            flash('Username is  already used . Please try another username','error')
        elif not (re.fullmatch(regex, email)):
            flash('Enter a valid Email address','error')
        elif password1 != password2:
            flash('Password doesn\'t match','error')
        elif len(password1) < 6:
            flash('Password contains minimum of 6 characters','error')
        else:
            user = User(email=email,username=username,password=generate_password_hash(password1,method='md5'))
            db.session.add(user)
            db.session.commit()
            flash('User account created',"success")
            return redirect(url_for('authentication.login'))
    return render_template("signup.html")
@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("view.home"))
