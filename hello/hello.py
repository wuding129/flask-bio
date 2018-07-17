from flask import Flask, render_template
# from flask_script import Manager
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap()
moment = Moment()
# manage = Manager(app)


@app.route('/')
def index():
    return render_template('index.html', name='wu', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    comments = ('one', 'two', '123')
    return render_template('user.html', name=name, comments=comments)
    # return '<h1>hello %s!</h1>' % name


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


bootstrap.init_app(app)
moment.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
