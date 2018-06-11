# Python Tests README

## Directories

#### data/

Data required for running scripts

#### results/

Results from the scripts

    read_bbc_data/                # Plots created by scripts in src/read_bbc_data/
    read_bbc_data_click_stats/    # Plots created by scripts in src/read_bbc_data_click_stats/
    technical_diff/               # Plots created by scripts in src/technical_diff/

#### src/

Scripts used to create plots, Dash apps and statistics for statistical analysis.

      dash_app/                     # Dash applications
      read_bbc_data/                # Initial analysis
      read_bbc_data_click_stats/    # Plots the statistics
      technical_diff/               # Filters participants by technical difficulties
      write_bbc_data_click_stats    # Creates statistics
      split_CAKE_particpants.py     # Splits participant data by condition  

## Viewing plots

All HTML plots can be downloaded and opened in browser.

To view the [Dash](https://dash.plot.ly/) examples in [documentation\tests\python\src\dash_app](documentation\tests\python\src\dash_app), follow Installation instructions.

### Installation

#### Requirements

###### Windows

    - Python 3.6 +
    - virtualenv
    - Git Bash
    - Command Line Interface
    - Python IDE / Text editor

    NOTE: All commands that use "git" are done in Git Bash. It lets you use MinGW/Linux tools with Git at the command line.


###### Linux

    - Python 3.6 +
    - virtualenv
    - Git
    - Command Line Interface
    - Python IDE / Text editor

 ### Clone Repo

 `git clone https://github.com/UoMResearchIT/bbc_data_flask_app.git`

' cd documentation\tests\python '

 ### Install Packages

###### Windows

```
$ virtualenv <virtualenv_name>
$ <virtualenv_name>\Scripts\activate
$ pip install -r requirements.txt
```
###### Linux

```
$ virtualenv <virtualenv_name>
$ source <virtualenv_name>/bin/activate
$ pip install -r requirements.txt
```

Latest requirements can be viewed [here](https://github.com/UoMResearchIT/bbc_data_flask_app/blob/master/requirements.txt)

#### Run Flask App on Development Server

###### Windows

```
$ C:\path\to\app>set FLASK_APP=app.py
$ flask run
```

###### Linux

 ```
$ export FLASK_APP=app.py
$ flask run
```
