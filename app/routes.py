from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simplified login logic
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return "Welcome to your dashboard!"

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
