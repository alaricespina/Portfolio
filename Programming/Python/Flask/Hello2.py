from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return 'Hello World 2'

@app.route('/hatdog')
def hakdug():
	return 'nyahahahahaah'

if __name__ == '__main__':
   app.run()