from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from keywoo import app, db
from keywoo.models.sites import Site
from keywoo.models.users import User


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name=name).first()
        if user:
            flash('このユーザは既に登録済みです。他のユーザ名で登録してください。')
            return redirect(url_for('signup'))
        if not name or not password:
            flash('お名前とパスワードを入力してください。')
            return redirect(url_for('signup'))

        new_user = User(name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(name=name).first()
        if not user or not check_password_hash(user.password, password):
            flash('ユーザ名かパスワードが間違っています。')
            return redirect(url_for('login'))
        login_user(user, remember=remember)
        return redirect(url_for('index'))
    return render_template('/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/', methods=['GET','POST'])
def index():
    user = current_user.name if current_user.is_authenticated else None
    if request.method == "POST":
        if request.form["radio"] == "add":
            name = request.form.get('name')
            url = request.form.get('url')

            registrated = Site.query.filter_by(name=name,user=user).first()
            if registrated:
                flash('この名前は既に登録済みです。')
                return redirect(url_for('index'))

            new_site = Site(name=name, url=url, user=user)
            db.session.add(new_site)
            db.session.commit()

        if request.form["radio"] == "delete":
            del_sites = request.form.getlist("check")
            for del_site in del_sites:
                site = Site.query.filter_by(name=del_site,user=user).first()
                db.session.delete(site)
                db.session.commit()

    sites = Site.query.filter_by(user=user)
    return render_template("index.html", sites = sites)

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.form["search"]:
        search_text = str(request.form["search"])
        search_list = search_text.splitlines()
        flash('Result Pages')
        user = current_user.name if current_user.is_authenticated else None
        sites = Site.query.filter_by(user=user)
        return render_template("result.html", search_list = search_list, sites = sites)
    else:
        flash('failed')
        return redirect(url_for('index'))