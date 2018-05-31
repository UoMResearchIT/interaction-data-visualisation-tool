# OBM Data Visualisation Tool (Working Title)
 
A web based data visualisation tool for the initial 
analysis of low level interaction data taken from object based user experiences. 

It takes the data and creates a set of visualisations that visualise the type and density 
of clicks, as well as summary statistics such as total number of clicks, average number of
clicks per second and total time taken.

## Installation

### Requirements

#####Windows

    Python 3.6 +
    virtualenv
    Git Bash
    Command Line Interface
    Python IDE / Text editor 

    NOTE: All commands that use "git" are done in Git Bash. It lets you use MinGW/Linux tools with Git at the command line. 

#####Linux 

    Python 3.6+
    virtualenv
    Git
    Command Line Interface
    Python IDE / Text editor
 
 ###Clone Repo 
 
 `git clone https://github.com/UoMResearchIT/bbc_data_flask_app.git`
 
 ### Install Packages
 
#####Windows

`$ virtualenv <virtualenv_name>`

`$ <virtualenv_name>\Scripts\activate`

`$ pip install -r requirements.txt`

#####Linux 

`$ virtualenv <virtualenv_name>`

`$ source <virtualenv_name>/bin/activate`

`$ pip install -r requirements.txt`

Latest requirements can be viewed [here](https://github.com/UoMResearchIT/bbc_data_flask_app/blob/master/requirements.txt)
 
### Run Flask App on Development Server 

#####Windows

`$ C:\path\to\app>set FLASK_APP=app.py`

`$ flask run`
 
#####Linux 
 
`$ export FLASK_APP=hello.py`

`$ flask run`

### External Deployment Options

[Refer to Flask Documentation ](http://flask.pocoo.org/docs/1.0/deploying/)
 
## Usage

### Preparing Data before entry (Columns and their names)

### Known Issues / Put in the Issues on GitHub
 
 Run Analysis (Large DataSet Warning)
 
 ### Results
 - Filtering the plots, by user, zooming in etc 
 - Can be downloaded - PNG or HTML, Stats in CSV
 
 ## License 
 
 