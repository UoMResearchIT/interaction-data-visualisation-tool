
# Interaction Data Visualisation Tool (IDVT)


## Introduction

Interaction data is messy, there is a lot of it; complicated, it is challenging to read;
and difficult to work with due to the number of unique features.

However, interaction data has the potential to be a great resource in identifying
audience behaviour (ref Measuring Behaviours paper?, see other refs used to see if
applicable).

I've created a web based data visualisation tool for the initial analysis of low level interaction data taken from user experiences. It provides a way to create abstractions and visualisations of the data to inform a feature selection process that can tease out audience behaviours.  

## Problem

The original goal was to create visualisations from interaction data from
[CAKE](https://www.bbc.co.uk/taster/pilots/cook-along-kitchen-experience)
(Cook-Along Kitchen Experience). An OBM (Object Based Media) experience from the BBC. Over that time the potential was seen in a generalised tool that could be used for future experiences to speed up the reading of audience behaviour.


Initial visualisations were done using [R](https://www.r-project.org/) and the [tidyverse](https://www.tidyverse.org/) package. R is a language designed for statistical computing and data visualisation so it was quick and easy to use for pre processing the data and for initial analysis.

![Density of Clicks](/tests/r/results/1_first_visualisations/2e_sixty_minutes.png)

The problem was that the graphs aren't interactive, which makes it easier to explore the data without having to constantly writing new scripts to make a new plot based on a feature or data point that you wanted a closer look at. Shiny, an R package that can build interactive plots that could be deployed to the web app seemed like a logical option. Unfortunately the plots couldn't be shared easily as they required the recipient to have R and [RStudio](https://www.rstudio.com/) installed, and the it couldn't give the flexibility needed to deploy on our own servers.

It was necessary to look outside the R ecosystem. After looking at different languages and data visualisation frameworks, Python seemed the most obvious solution. I had prior knowledge using it with Django and Wagtail which would be useful for deployment and Python also offered a much bigger range of data visualisation packages to choose from. Of those, [Plotly for Python](https://plot.ly/d3-js-for-python-and-pandas-charts/), was the strongest candidate because it creates interactive plots by default, the output is an HTML file serialised with JSON, so are lightweight and easily shareable, and could be embedded in web pages.

(example images, some description of interactivity)![]()

[Dash](https://plot.ly/products/dash/), produced by the same team behind Plotly uses [Flask](http://flask.pocoo.org/) to create a dashboard interface that provides more user control over interactivity; allowing for written user input, dropdown controls and the like; as well the layout such as multiple plots on a single page and providing space to add Markdown for descriptive text.  

(example gif?) ![]()   

> The scripts for testing packages can be found in the [Repositories](#repositories) section.

## Solution

To build the web app I used Flask. It's lightweight and I already had some indirect experience with it using Dash. Django and Wagtail were also considered but were a bit heavy for what would be a two page web app.

In the end Dash wasn't used as while it has many advantages as detailed earlier, it doesn't have a method for downloading a PNG or an interactive HTML file. These are important if they are to be included in research papers or easily shared with others.  

## What Does The Tool Do?

The IDVT takes the interaction data and creates a set of plots that visualise the type and density of clicks, as well as summary statistics such as total number of clicks, average number of clicks per second and total time taken.

The tool is designed to take a CSV file with comma separated values as an input.
It then runs a Python script to pre process the data to clean up and infinite or NAN values as well as making sure it contains the columns needed to create the visualisations, and, if not, generating the columns. Another two scripts construct
the visualisations, one that reveals the type of button clicks on a timeline
([action_item.py](https://github.com/UoMResearchIT/bbc_data_flask_app/blob/master/static/scripts/action_item.py))
and another that plots the density of button clicks in each five minute interval of the experience
([click_density.py](https://github.com/UoMResearchIT/bbc_data_flask_app/blob/master/static/scripts/click_density.py)).

Once those scripts have finished running an additional three scripts will run. [create_stats.py](https://github.com/UoMResearchIT/bbc_data_flask_app/blob/master/static/scripts/create_stats.py) creates the statistics such as click count, time taken in secs and mins, clicks per second/minute, and clicks per second/minute. These are saved in to a CSV file that three histograms will be created.


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

* `create_stats.py`- creates a CSV of the statistical data such as click count, time taken in minutes/seconds, clicks per minute/second, minutes/secs per click.
this is then used to create histograms.

* `histogram_click_count.py`, `histogram_clicks_per_min.py` and `histogram_time_taken.py` create histograms based on the click count, clicks per minute and time taken.

Each data file uploaded by the user will create its own directory in `static/output` to store the relevant outputs.

All plots and an HTML version of the stats are also saved in `templates/` to be rendered by the `vis.html` template.

## What Can Be Gained from this Tool?

Insight into which features are important,

clicks - colour coding
density - see when most of the clicks are happening

histograms - can see patterns of time, clicks, clicks per minute. Why are these important?

## Applications?

Speed up initial analysis and features to look out for.


## Limitations

Large Data Sets = takes longer to get the data needed for plots, lots of statistical noise.

## Repositories

* BBC-CAKE-data-analysis - R scripts for initial analysis and testing
* bbc_data_plotly - Python scripts for Plotly and Dash  
