# Interaction Data Visualisation Tool (IDVT)

- [Interaction Data Visualisation Tool (IDVT)](#interaction-data-visualisation-tool-idvt)
	- [Installation](#installation)
		- [Requirements](#requirements)
				- [Windows](#windows)
				- [Linux](#linux)
		- [Run Flask App on Development Server](#run-flask-app-on-development-server)
		- [External Deployment Options](#external-deployment-options)
	- [Usage](#usage)
		- [Essential Columns](#essential-columns)
		- [Run Analysis](#run-analysis)
		- [Results](#results)
	- [License](#license)


![index.html](documentation/screenshots/index.png)

A web based data visualisation tool for the initial
analysis of low level interaction data taken from object based user experiences.

The IDVT takes the data and creates a set of plots that visualise the type and density
of clicks, as well as summary statistics such as total number of clicks, average number of clicks per second and total time taken.

## Installation

### Requirements

##### Windows

    - Python 3.6 +
    - virtualenv
    - Git Bash
    - Command Line Interface
    - Python IDE / Text editor

    NOTE: All commands that use "git" are done in Git Bash. It lets you use MinGW/Linux tools with Git at the command line.


##### Linux

    - Python 3.6 +
    - virtualenv
    - Git
    - Command Line Interface
    - Python IDE / Text editor

 ### Clone Repo

 `git clone https://github.com/UoMResearchIT/bbc_data_flask_app.git`

 ### Install Packages

##### Windows

```
$ virtualenv <virtualenv_name>
$ <virtualenv_name>\Scripts\activate
$ pip install -r requirements.txt
```
##### Linux

```
$ virtualenv <virtualenv_name>
$ source <virtualenv_name>/bin/activate
$ pip install -r requirements.txt
```

Latest requirements can be viewed [here](https://github.com/UoMResearchIT/bbc_data_flask_app/blob/master/requirements.txt)

### Run Flask App on Development Server

##### Windows

```
$ C:\path\to\app>set FLASK_APP=app.py
$ flask run
```

##### Linux

 ```
$ export FLASK_APP=app.py
$ flask run
```

### External Deployment

This section will run through deploying the app on a Ubuntu Virtual Machine. For other option refer to [Flask Documentation ](http://flask.pocoo.org/docs/1.0/deploying/)


#### Install Requirements

We need to create a new user with 'sudo' privileges

```
$ adduser newuser
$ adduser newuser sudo

```
SSH into the server with the new user and update packages on the VM.

```
$ sudo apt-get update
$ sudo apt-get install -y python3 python-pip python-venv nginx gunicorn  nano git build-essential libssl-dev libffi-dev python3-dev

```
Check that Python 3 is installed

```
$ python3 -V
```

Create a new directory to store the project

```
$ sudo mkdir /home/www && cd /home/www

```
In the directory we'll fetch the repo holding the project, then checkout the deployment branch

```
$ sudo git clone <repo URL>
$ cd <repo_name>
$ sudo git checkout deployment

```

Create a virtual environment

```
$ sudo python3 -m venv <name_of_virtual_environment>
```

Activate via -

```
$ source <name_of_virtual_environment>/bin/activate

```
When activated your prompt will be prefixed with the name of your environment. Install project requirements.


```
$ sudo pip install -r requirements.txt

```

That's the initial set-up complete.

#### Configure nginx and gunicorn

nginx and gunicorn will allow the app to run continuously.

We need to start nginx -

```
$ sudo /etc/init.d/nginx start
```
then remove the default configuration, and create a new config file which nginx will load on startup:


```
$ sudo rm /etc/nginx/sites-enabled/default
$ sudo touch /etc/nginx/sites-available/bbc_data_flask_app
$ sudo ln -s /etc/nginx/sites-available/bbc_data_flask_app /etc/nginx/sites-enabled/bbc_data_flask_app
```
To add the config setting we'll use nano

```
$ sudo nano /etc/nginx/sites-enabled/bbc_data_flask_app

```
and add -

```text

server {
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    location /static {
        alias  /home/www/bbc_data_flask_app/static/;
    }
}

```

Restart nginx and then run project -
```
$ sudo /etc/init.d/nginx restart
$ cd /home/www/bbc_data_flask_app/
$ gunicorn app:app -b localhost:8000

```
Open browser and navigate to your domain name or IP address. You will be greeted by -

![index.html](documentation/screenshots/index.png)

#### Configure Supervisor

If forking IDVT and working on new features you may want to set-up [Supervisor](http://supervisord.org/index.html) so don't need to manually start and restart gunicorn each time changes are made to the app.

1) Install Supervisor:

```
$ sudo apt-get install -y supervisor

```
2) Create configuration file:

```
$ sudo nano /etc/supervisor/conf.d/bbc_data_flask_app.conf
```

3) Add the following to the config file:

```
[program:flask_project]
command = gunicorn app:app -b localhost:8000
directory = /home/www/flask_project
user = newuser

```

4) Stop gunicorn:

```
$ sudo pkill gunicorn
```

5) Start gunicorn with Supervisor:

```
$ sudo supervisorctl reread
$ sudo supervisorctl update
$ sudo supervisorctl start bbc_data_flask_app
```

## Usage

The Web App is designed to take a CSV file with comma separated values as input then runs Python scripts that will output various visualisations.

### Essential Columns

* **participant_id** - that refers to the individual users of the interactive experience.
* **timestamp** - point in time when the event occurred, in datetime format eg (2017-08-17 19:41:09)
* **item** - button participant has clicked on e.g. play button
* **action** - the result of clicking button e.g. play, pause etc.

All other columns needed will be generated by either `data_pre_pro.py` or `create_stats.py`

### Run Analysis

Clicking Run Analysis will take the CSV file uploaded by the user and create visualisations using the open source
[Plotly for Python](https://github.com/plotly/plotly.py)

It will run the following scripts -

* `data_pre_pro.py` - pre processes the data to get rid of inf, and NAN values.
Will also create the 'time_diff' and 'action_item' columns needed for the plots.

* `action_item.py` - takes the processed data and plots the type of clicks (i.e action_item) across time.

* `click_density.py` - plots the density of clicks across a 300 second (5 minute intervals)

* `create_stats.py`- creates a CSV of the statistical data such as click count,time taken in minutes/seconds, clicks per minute/second, minutes/secs per click.
this is then used to create histograms.

* `histogram_click_count.py`, `histogram_clicks_per_min.py` and `histogram_time_taken.py` create histograms based on the click count, clicks per minute and time taken.

Each data file uploaded by the user will create its own directory in `static/output` to store the relevant outputs.

All plots and an HTML version of the stats are also saved in `templates/` to be rendered by the `vis.html` template.

### Results

Once the scripts have finished running the results are displayed using the `vis.html` template. Each is interactive with controls such as zoom in/out, pan, select etc in the Plotly toolbar.

The results are displayed in the following order -

1. **Click Type** - Hovering over will display the Participant ID, Action Item and Time (in Minutes). Action Item can be filtered on the right to narrow down the type of click a user wants displayed.
The "compare data on hover" option in the Plotly toolbar is useful if want to see all the types of clicks at a particular time.
2. **Click Density** - Hovering over will display the Participant ID, Interval time and Number of events in that interval. Participants can be filtered on the right.
3. **Click Count** - Hovering over will display the number of participants and the bin size (automatically set depending on data)
4. **Clicks Per Minute** - Hovering over will display the number of participants and the bin size (automatically set depending on data)
5. **Time Taken (in Minutes)** - Hovering over will display the number of participants and the bin size (automatically set depending on data)
6. **Table of Stats** - A table of the stats generated by `create_stats.py`.

Each plot can be downloaded as a HTML by clicking the 'Download .... as HTML' button, or as PNG by clicking the camera icon that is part of the Plotly toolbar.

A CSV of Table of Stats can be downloaded via the 'Download as CSV' button.  

## License
