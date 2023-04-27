from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import SourceForm
from app.models import Source

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
