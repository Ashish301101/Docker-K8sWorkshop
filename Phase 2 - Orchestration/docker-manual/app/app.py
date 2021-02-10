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
      # 'host': 'localhost',
      # 'port': '32000',
      # Uncomment the above lines for testing without docker
      'host': '172.17.0.3', # needs to be replaced by the IP of your db container.
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
