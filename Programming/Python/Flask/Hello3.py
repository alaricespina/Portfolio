from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s! You are currently on the hello page which uses your name to display Hello <name>' % name

@app.route('/blog/<int:age>')
def show_blog(age):
   return 'Your Current age is %d' % age

@app.route('/rev/<float:randomf>')
def revision(randomf):
   return 'You typed in a random floating number %f' % randomf

if __name__ == '__main__':
   app.run(debug = True)