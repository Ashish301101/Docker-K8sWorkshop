from flask import Flask
# Add mysql.connector and json
import mysql.connector
import json

app = Flask(__name__)

# Add function to fetch all subject names from the db
def get_subjects():
   config = {
      'user':'root',
      'password': 'root',
      'host': 'db',
      'port': '3306',
      'database': 'subjects'
   }
   connection = mysql.connector.connect(**config)
   cursor = connection.cursor()
   cursor.execute('SELECT * FROM my_subjects')
   results = [{code: name} for (name, code) in cursor]
   cursor.close()
   connection.close()
   return results

@app.route('/subjects')
def subjects():
   return json.dumps({'subjects': get_subjects()})

@app.route('/')
def hello():
	return "Welcome to Your Flask App!"


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5000, debug = False)
