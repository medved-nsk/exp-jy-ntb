from flask import Flask, render_template

app=Flask(__name__)

conf = {
    'SERVER': '0.0.0.0',
    'PORT': 5001
}


@app.route('/')
def home():
    return render_template('home.html') #'pkfs under construction'

@app.route('/about/')
def about():
    return 'About'

if __name__ == '__main__':
    #app.run()
    app.run(host=conf['SERVER'], port=conf['PORT'], debug=True)
