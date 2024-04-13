from flask import Flask, render_template, request
import re 



from database import connect_db
conn = connect_db()

from student_blueprint import student_bp
from table_create_blueprint import tables_bp

app = Flask(__name__) 
app.secret_key = 'your secret key'

#register or access the blueprints
app.register_blueprint(student_bp)
app.register_blueprint(tables_bp)


#load the home or index page
@app.route('/home') 
@app.route('/') 
def home(): 
  return render_template('index.html') 




if __name__ == '__main__': 
       app.run(debug=True)    