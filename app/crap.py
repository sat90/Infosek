# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     form = IndexForm()
    
#     if form.login.validate_on_submit() and form.login.submit.data:
#         user = query_db('SELECT * FROM Users WHERE username="{}";'.format(form.login.username.data), one=True)
#         if user == None:
#             flash('Sorry, this user does not exist!')
#         elif user['password'] == form.login.password.data:
#             return redirect(url_for('stream', username=form.login.username.data))
#         else:
#             flash('Sorry, wrong password!')
#     elif form.register.validate_on_submit() and form.register.submit.data:
#         query_db('INSERT INTO Users (username, first_name, last_name, password) VALUES("{}", "{}", "{}", "{}");'.format(form.register.username.data, form.register.first_name.data,
#         form.register.last_name.data, form.register.password.data))
#         return redirect(url_for('index'))
#     return render_template('index.html', title='Welcome', form=form)



                    