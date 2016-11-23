from blog_flask import app
from flask import render_template,redirect,flash,url_for
from blog.form import SetupForm
from blog_flask import db
from author.models import Author
from blog.models import Blog

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Halo halo</h1>'
    
@app.route('/admin')
def admin():
    blogs = Blog.query.count()
    print(blogs)
    if blogs == 0:
        return redirect(url_for('setup'))
    return render_template('blog/admin.html')
    
@app.route('/setup')
def setup():
    form = SetupForm()
    return render_template('blog/setup.html',form=form)