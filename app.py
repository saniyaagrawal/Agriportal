from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

class farmer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    contactno = db.Column(db.Integer)
    Email = db.Column(db.String(20))
    Password = db.Column(db.String(20))
    state = db.Column(db.String(20))
    city = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)

    def _repr_(self) :
        return 'farmer ' + str(self.id)

@app.route('/login',methods=['GET','POST'])
def register():
    if request.method=='post':
        login_id=request.form['id']
        login_Email=request.form['Email']
        login_Password=request.form['Password']
        login_name=request.form['name']
        login_contactno=request.form['contactno']
        login_state=request.form['state']
        login_city=request.form['city']
        login_date_posted=request.form['date_posted']
        new_login=farmer(Email =login_Email, Password = login_Password ,date_posted=login_date_posted,city=login_city,state=login_state,contactno=login_contactno,name=login_name,id=login_id)
        db.session.add(new_login)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('login.html')


# class goods(db.Model):
#     id2 = db.Column(db.Integer,nullable=False)
#     product = db.Column(db.String(20),nullable=False)
#     quantity = db.Column(db.Integer,nullable=False)
#     date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
#
#     def _repr_(self) :
#         return 'good ' + str(self.product)
#
# item add karne k liye naya page banaya
# @app.route('/new_item',methods=['GET','POST'])
# def add_item():
#     if request.method=='post':
#         post_product=request.form['Product']
#         post_quantity=request.form['Quantity']
#         new_post good(Email =post_Email,Password = post_Password )
#         db.session.add(new_post)
#         db.session.commit()
#         return redirect('/profile')
#     else:
#         return render_template('login.html')

#profile page
@app.route('/profile')
def myprofile():
    return render_template('profile.html')

@app.route('/searchResult')
def searchResult():
    return render_template('searchResult.html')


if __name__ == '__main__':
    app.run(debug=True)