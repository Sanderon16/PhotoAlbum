"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PhotoAlbum import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/PhotoAlbum')
def PhotoAlbum():
    """Renders the Photo Album page."""
    return render_template(
        'PhotoAlbum.html',
        title='Photo Album Of Counting',
        year=datetime.now().year,
        message='An image documentary of different hands lifting varying amounts of fingers simulating a count '
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
