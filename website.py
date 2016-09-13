from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://preverdiau:user@0.0.0.0/sandbox'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://preverdi:admin@preverdi.mysql.pythonanywhere-services.com/preverdi$sandbox'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    countryname = db.Column(db.String(80), unique=True)

    def __init__(self, countryname):
        self.countryname = countryname

    def __repr__(self):
        return '<Country %r>' % self.countryname

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.form.get('action') == "add":
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            try:
                user = User(username, email)
                db.session.add(user)
                db.session.commit()
            except:
                pass

    if request.form.get('action') == "remove":
        User.query.delete()
        db.session.commit()

    users = User.query.all()
    return render_template('index.html', users = users)

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://preverdiau:user@0.0.0.0/sandbox'
    app.run(host="0.0.0.0", port=5003, debug = True)