from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('home.html')

if __ __name__ == '__main__':
    app.run(debug = True)
    
