from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import SourceForm
from app.models import Source
from flask import session, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/sources', methods=['GET', 'POST'])
def sources():
    form = SourceForm()
    if form.validate_on_submit():
        source = Source(url=form.url.data, name=form.name.data, city=form.city.data, postal_code=form.postal_code.data)
        db.session.add(source)
        db.session.commit()
        flash('Source added successfully.')
        return redirect(url_for('sources'))

    sources = Source.query.all()
    return render_template('sources.html', sources=sources, form=form)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if 'admin_logged_in' in session and session['admin_logged_in']:
        return redirect(url_for('users'))

    form = AdminLoginForm()
    if form.validate_on_submit():
        master_password = app.config.get('MASTER_PASSWORD')
        if check_password_hash(generate_password_hash(master_password), form.master_password.data):
            session['admin_logged_in'] = True
            return redirect(url_for('users'))
        else:
            flash('Invalid master password.')

    return render_template('admin_login.html', form=form)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin_login'))

    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        user.is_admin = form.is_admin.data
        db.session.add(user)
        db.session.commit()
        flash('User added successfully.')
        return redirect(url_for('users'))

    users = User.query.all()
    return render_template('users.html', users=users, form=form)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))
