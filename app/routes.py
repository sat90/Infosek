from flask import render_template, flash, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, query_db
from app.forms import PostForm, FriendsForm, ProfileForm, CommentsForm, RegisterForm, LoginForm, IndexForm
from datetime import datetime
from passlib.hash import pbkdf2_sha256

import os

# this file contains all the different routes, and the logic for communicating with the database

# home page/login/registration
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if "user" in session.keys():
        if session["user"]:
            return redirect(url_for('stream', username=session["user"],sessionuser=session["user"]))
    else:
        session["user"] = None

    form = IndexForm()

    #flash(form.errors)
    if form.login.validate_on_submit():
        username_entered = form.login.username.data
        password_entered = form.login.password.data

        query = ('SELECT * FROM Users WHERE username=?;', (username_entered,))
        user = query_db(query, one=True)
        if user == None:
            flash("Username or password incorrect")
        elif not pbkdf2_sha256.verify(password_entered, user['password']):
            flash("Username or password incorrect")
        elif pbkdf2_sha256.verify(password_entered, user['password']):
            session["user"] = form.login.username.data
            return redirect(url_for('stream', username=username_entered,sessionuser=session["user"]))
    elif form.register.validate_on_submit():
        username = form.register.username.data
        password = form.register.password.data

        encrypt_pswd = pbkdf2_sha256.hash(password) #Hashes and adds a 16byte salt, by default adds 29000 iterations.
        query = 'SELECT * FROM Users WHERE username=?;', (username,)
        user = query_db(query, one=True)
        if user == None:
            query = 'INSERT INTO Users (username, first_name, last_name, password) VALUES(?, ?, ?, ?);', (form.register.username.data, form.register.first_name.data, form.register.last_name.data, encrypt_pswd)
            query_db(query, one=True)
            return redirect(url_for('index')), flash('New user registered!')
        else:
            flash('Username already exists.')

    return render_template('index.html', title='Welcome', form=form)


# content stream page
@app.route('/stream/<username>', methods=['GET', 'POST'])
def stream(username):
    if username != session["user"]:
        session["err"]="trying to get into another stream"
        return redirect(url_for('error'))
    form = PostForm()
    query = ('SELECT * FROM Users WHERE username=?;', (username,))
    user = query_db(query, one=True)
    if form.is_submitted():
        if form.image.data:

            filename=  form.image.data.filename
            if filename == "":
                session["err"]="no filename"
                return redirect(url_for('error'))
            if not legalimg(filename):
                session["err"]="illegal filetype"
                return redirect(url_for('error'))


            path = os.path.join(app.config['UPLOAD_PATH'], form.image.data.filename)
            form.image.data.save(path)


        query = ('INSERT INTO Posts (u_id, content, image, creation_time) VALUES(?, ?, ?, ?);', (user['id'], form.content.data, form.image.data.filename, datetime.now()))
        query_db(query)
        return redirect(url_for('stream', username=username))

    query = ('SELECT p.*, u.*, (SELECT COUNT(*) FROM Comments WHERE p_id=p.id) AS cc FROM Posts AS p JOIN Users AS u ON u.id=p.u_id WHERE p.u_id IN (SELECT u_id FROM Friends WHERE f_id=?) OR p.u_id IN (SELECT f_id FROM Friends WHERE u_id=?) OR p.u_id=? ORDER BY p.creation_time DESC;', (user['id'], user['id'], user['id']))
    posts = query_db(query)
    return render_template('stream.html', title='Stream', username=username,sessionuser=session["user"], form=form, posts=posts)


def legalimg(filename):
    if not "." in filename:
        return False
    filtyp = filename.rsplit(".", 1)[1]
    if filtyp.lower() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


# comment page for a given post and user.
@app.route('/comments/<username>/<int:p_id>', methods=['GET', 'POST'])
def comments(username, p_id):
    form = CommentsForm()
    if form.is_submitted():
        query = ('SELECT * FROM Users WHERE username=?;', (username,))
        user = query_db(query, one=True)
        query = ('INSERT INTO Comments (p_id, u_id, comment, creation_time) VALUES(?, ?, ?, \'?\');', (p_id, user['id'], form.comment.data, datetime.now()))
        query_db(query)

    query = ('SELECT * FROM Posts WHERE id=?;', (p_id,))
    post = query_db(query, one=True)
    query = ('SELECT DISTINCT * FROM Comments AS c JOIN Users AS u ON c.u_id=u.id WHERE c.p_id=? ORDER BY c.creation_time DESC;', (p_id,))
    all_comments = query_db(query)
    return render_template('comments.html', title='Comments', username=username,sessionuser=session["user"], form=form, post=post, comments=all_comments)


# page for seeing and adding friends
@app.route('/friends/<username>', methods=['GET', 'POST'])
def friends(username):
    if username != session["user"]:
        session["err"]="trying to get into anothers friendlist"
        return redirect(url_for('error'))
    form = FriendsForm()
    query = ('SELECT * FROM Users WHERE username=?;', (username,))
    user = query_db(query, one=True)
    if form.is_submitted():
        query = ('SELECT * FROM Users WHERE username=?;', (form.username.data,))
        friend = query_db(query, one=True)
        if friend is None:
            flash('User does not exist')
        else:
            query = ('INSERT INTO Friends (u_id, f_id) VALUES(?, ?);', (user['id'], friend['id']))
            query_db(query)

    query = ('SELECT * FROM Friends AS f JOIN Users as u ON f.f_id=u.id WHERE f.u_id=? AND f.f_id!=? ;', (user['id'], user['id']))
    all_friends = query_db(query)
    return render_template('friends.html', title='Friends', username=username, friends=all_friends,sessionuser=session["user"], form=form)


# see and edit detailed profile information of a user
@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    form = ProfileForm()
    if form.is_submitted():
        if username==session['user']:
            query = ('UPDATE Users SET education=?, employment=?, music=?, movie=?, nationality=?, birthday=? WHERE username=? ;', (
                form.education.data, form.employment.data, form.music.data, form.movie.data, form.nationality.data, form.birthday.data, username
                ))
            query_db(query)
        else:
            session["err"]="trying to edit someone elses profile"
            return redirect(url_for('error'))

        return redirect(url_for('profile', username=username))

    query = ('SELECT * FROM Users WHERE username=?;', (username,))
    user = query_db(query, one=True)
    return render_template('profile.html', title='profile', username=username, user=user, sessionuser=session["user"], form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session["user"] = None
    return redirect(url_for('index'))


@app.route('/error', methods=['GET', 'POST'])
def error():
    return render_template('noaccess.html', username=session["user"], err = session["err"],sessionuser=session["user"])
