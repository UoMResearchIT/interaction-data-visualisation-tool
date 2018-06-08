import os
from flask import Flask, request, redirect, url_for, send_file, render_template
from werkzeug.utils import secure_filename

# name the upload/input folder
UPLOAD_FOLDER = 'static/input/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# check to see if file is allowed.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# file upload on index page.
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    x = os.listdir('static/input')
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
            return redirect(url_for('run_vis', filename=filename))
    return render_template('index.html', value=x)


#  VIS - Runs the scripts necessary to produce the plots, histograms and stats table.

@app.route('/vis', methods=['GET'])
def run_vis():
    # Get variable for filename via POST and/or GET
    # put it in as system argument ie python arg1(script_name) arg2(filename)

    # GET filename and its file path
    file_name = str(request.args.get('filename'))
    input_filepath = 'static/input/' + file_name

    # MAKE DIRECTORIES

    # make a main directory to store output from scripts
    split_filename = os.path.splitext(file_name)[0]
    main_directory = r'static/output/' + split_filename
    os.makedirs(main_directory)

    # make click data directory
    click_directory = main_directory + '/click_plots'
    os.makedirs(click_directory)

    # make stats data directory
    stats_directory = main_directory + '/stats'
    os.makedirs(stats_directory)

    # name and path for the stats csv file
    csv_name = split_filename + '_stats.csv'
    csv_path = stats_directory + '/' + csv_name

    # RUN SCRIPTS

    # pre process the data. checks that data has the correct columns necessary to create the plots,
    # histograms and stats data
    os.system("python static/scripts/data_pre_pro.py " + input_filepath)

    # create click plots
    os.system("python static/scripts/action_item.py " + input_filepath + ' ' + split_filename)
    os.system("python static/scripts/click_density.py " + input_filepath + ' ' + split_filename)

    # create the stats file and histograms
    os.system("python static/scripts/create_stats.py " + input_filepath + ' ' + split_filename + ' ' + stats_directory)
    os.system("python static/scripts/histogram_click_count.py " + csv_path + ' ' + split_filename)
    os.system("python static/scripts/histogram_clicks_per_min.py " + csv_path + ' ' + split_filename)
    os.system("python static/scripts/histogram_time_taken.py " + csv_path + ' ' + split_filename)

    # load template with plots and stats data.
    return render_template('vis.html')


# HTML and CSV DOWNLOADS
# Each route downloads the HTML version of each plot,
# and the CSV version of the stats data.

# Download action_item plot
@app.route('/dl_click', methods=['GET'])
def run_dl_click():
    return send_file('templates//bbc_data_action_item.html',
                     mimetype='text/html',
                     as_attachment=True)


# Download click density plot
@app.route('/dl_click_density')
def run_dl_click_density():
    return send_file('templates//bbc_data_click_density.html',
                     mimetype='text/html',
                     attachment_filename='bbc_data_click_density.html',
                     as_attachment=True)


# Download Click Count Histogram
@app.route('/dl_click_count_html')
def run_dl_click_count():
    return send_file('templates//bbc_data_histogram_click_count.html',
                     mimetype='text/csv',
                     attachment_filename='bbc_data_histogram_click_count.html',
                     as_attachment=True)


# Download Clicks Per Min Histogram
@app.route('/dl_clicks_per_minute_html')
def run_dl_clicks_per_minute():
    return send_file('templates//bbc_data_histogram_clicks_per_minute.html',
                     mimetype='text/csv',
                     attachment_filename='bbc_data_histogram_clicks_per_minute.html',
                     as_attachment=True)


# Download Time Taken Histogram
@app.route('/dl_time_taken_html')
def run_dl_time_taken():
    return send_file('templates//bbc_data_histogram_time_taken_mins.html',
                     mimetype='text/csv',
                     attachment_filename='bbc_data_histogram_time_taken_mins.html',
                     as_attachment=True)


# Download the stats data as a CSV
@app.route('/dl_stats_csv')
def run_dl_stats_csv():
    return send_file('templates//bbc_data_stats.csv',
                     mimetype='text/csv',
                     attachment_filename='bbc_data_stats.csv',
                     as_attachment=True)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()