import os
from flask import Flask, request, redirect, url_for, send_file, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/input/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('vrun'))
    return render_template('index.html')


@app.route('/click')
def run_click():
    os.system("python static/scripts/action_item.py")
    return render_template('click.html')


@app.route('/dl_click')
def run_dl_click():
    return send_file('templates\\action_item.html',
                     mimetype='text/html',
                     attachment_filename='bbc_data_action_item.html',
                     as_attachment=True)


@app.route('/stats')
def run_stats():
    os.system("python static/scripts/create_stats.py")
    return render_template('stats.html')


@app.route('/dl_stats_csv')
def run_dl_stats_csv():
    return send_file('static\output\\stats\\bbc_data_stats.csv',
                     mimetype='text/csv',
                     attachment_filename='bbc_data_stats.csv',
                     as_attachment=True)


@app.route('/dl_stats_html')
def run_dl_stats_html():
    return send_file('templates\\bbc_data_stats.html',
                     mimetype='text/html',
                     attachment_filename='bbc_data_stats.html',
                     as_attachment=True)


if __name__ == '__main__':
    app.run()
