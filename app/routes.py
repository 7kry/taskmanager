from flask import current_app as app
from flask import render_template, flash, redirect, url_for, request, jsonify
from app import db
from app.models import User, TaskType, Company, Task, Notification
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash
from app.forms import TaskForm, TaskTypeForm, CompanyForm
from datetime import datetime

@app.route('/')
@app.route('/index')
@login_required
def index():
  return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=True)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('index')
    return redirect(next_page)
  return render_template('login.html', title='Sign In')

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/mypage')
@login_required
def mypage():
  return render_template('mypage.html', title='My Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register')

@app.route('/@<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('user.html', user=user)

@app.route('/autocomplete', methods=['GET'])
@login_required
def autocomplete():
  search = request.args.get('q')
  query = User.query.filter(User.username.like(f'%{search}%')).all()
  results = [user.username for user in query]
  return jsonify(results)

@app.route('/check_task_type', methods=['GET'])
@login_required
def check_task_type():
  search = request.args.get('q')
  task_type = TaskType.query.filter(TaskType.name.like(f'%{search}%')).all()
  if task_type:
    return jsonify({"exists": True, "results": [t.name for t in task_type]})
  return jsonify({"exists": False})

@app.route('/check_company', methods=['GET'])
@login_required
def check_company():
  search = request.args.get('q')
  companies = Company.query.filter(Company.name.like(f'%{search}%')).all()
  if companies:
    return jsonify({"exists": True, "results": [c.name for c in companies]})
  return jsonify({"exists": False})

@app.route('/check_user', methods=['GET'])
@login_required
def check_user():
  search = request.args.get('q')
  user = User.query.filter(User.username.like(f'%{search}%')).all()
  if user:
    return jsonify({"exists": True, "results": [u.username for u in user]})
  return jsonify({"exists": False})

@app.route('/set_language', methods=['POST'])
@login_required
def set_language():
  language = request.form.get('language')
  if language not in ['ja', 'en']:
    flash('Invalid language selection')
    return redirect(url_for('preferences'))
  current_user.language = language
  db.session.commit()
  flash('Language preference updated')
  return redirect(url_for('preferences'))

@app.route('/preferences')
@login_required
def preferences():
  return render_template('preferences.html', title='Preferences')

@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
  form = TaskForm()
  if form.validate_on_submit():
    task_type = TaskType.query.filter_by(name=form.task_type.data).first()
    if not task_type:
      task_type = TaskType(name=form.task_type.data)
      db.session.add(task_type)
    companies = form.companies.data.split(', ')
    companies_objs = []
    for company in companies:
      company_obj = Company.query.filter_by(name=company).first()
      if not company_obj:
        company_obj = Company(name=company)
        db.session.add(company_obj)
      companies_objs.append(company_obj)
    order_to = User.query.filter_by(username=form.order_to.data).first()
    if not order_to:
      flash('Order to user not found')
      return render_template('tasks.html', title='Tasks', form=form)
    ordered_by = current_user
    if form.delegation.data:
      ordered_by = User.query.filter_by(username=form.ordered_by.data).first()
      if not ordered_by:
        flash('Ordered by user not found')
        return render_template('tasks.html', title='Tasks', form=form)
    task = Task(
      task_type_id=task_type.id,
      task_detail=form.task_detail.data,
      companies=companies_objs,
      required_time=form.required_time.data,
      ordered_by_id=ordered_by.id,
      order_to_id=order_to.id,
      message=form.message.data
    )
    db.session.add(task)
    db.session.commit()
    
    # Create notification for the user
    notification = Notification(
      user_id=order_to.id,
      message=f"You have a new task assigned by {ordered_by.username}",
      timestamp=datetime.utcnow()
    )
    db.session.add(notification)
    db.session.commit()
    
    flash('Task created successfully')
    return redirect(url_for('tasks'))
  return render_template('tasks.html', title='Tasks', form=form)

@app.route('/task_types', methods=['GET', 'POST'])
@login_required
def task_types():
  form = TaskTypeForm()
  if form.validate_on_submit():
    task_type = TaskType(name=form.name.data)
    db.session.add(task_type)
    db.session.commit()
    flash('Task type added successfully')
    return redirect(url_for('task_types'))
  return render_template('task_types.html', title='Task Types', form=form)

@app.route('/companies', methods=['GET', 'POST'])
@login_required
def companies():
  form = CompanyForm()
  if form.validate_on_submit():
    company = Company(name=form.name.data)
    db.session.add(company)
    db.session.commit()
    flash('Company added successfully')
    return redirect(url_for('companies'))
  return render_template('companies.html', title='Companies', form=form)

@app.route('/notifications')
@login_required
def notifications():
  notifications = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.timestamp.desc()).all()
  return render_template('notifications.html', title='Notifications', notifications=notifications)

@app.route('/check_notifications')
@login_required
def check_notifications():
  notifications = Notification.query.filter_by(user_id=current_user.id, read=False).order_by(Notification.timestamp.desc()).all()
  notifications_list = [{'message': notification.message, 'timestamp': notification.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for notification in notifications]
  # Mark notifications as read
  for notification in notifications:
    notification.read = True
  db.session.commit()
  return jsonify(notifications_list)

# vim:ts=2:sts=2:sw=2:et
