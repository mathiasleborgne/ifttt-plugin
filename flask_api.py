from flask import Flask, url_for
name_app = __name__
app = Flask(name_app)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    print "running app {}".format(name_app)
    app.run()

# Run: (cf http://flask.pocoo.org/docs/0.11/deploying/uwsgi/)
# uwsgi -s /tmp/uwsgi.sock --manage-script-name --mount /=flask_api:app --http :9090