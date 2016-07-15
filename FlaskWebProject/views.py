"""
Routes and views for the flask application.
"""

import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from FlaskWebProject import app
from werkzeug import secure_filename


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/robot_say')
def robot_say():
    print "Banged robot_say API"
    return "Banged robot_say API"


# File transfert, see:
# http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python

# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded


# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "db"])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/transfert')
def transfert():
    return render_template('transfert.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file_upload = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file_upload and allowed_file(file_upload.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file_upload.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        path_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print "path_file", path_file
        file_upload.save(path_file)
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
