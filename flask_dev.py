from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    from test_app import test_app

    return render_template('home.html', **locals())

if __name__ == '__main__':
    app.run()
