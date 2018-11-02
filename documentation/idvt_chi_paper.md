# Interaction Data Visualisation Tool (IDVT)

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Interaction Data Visualisation Tool (IDVT)](#interaction-data-visualisation-tool-idvt)
	- [Introduction](#introduction)
	- [Problem](#problem)
	- [IDVT](#idvt)
		- [Raw Data](#raw-data)
		- [Visualisations / Summary Statistics](#visualisations--summary-statistics)
- [IDVT Use Case](#idvt-use-case)
	- [Future Use / Applications](#future-use--applications)
	- [Furthur Development](#furthur-development)
	- [Acknowledgements](#acknowledgements)
	- [Papers](#papers)


<!-- /TOC -->

## Introduction

Click data is messy, there is a lot of it, it is often labelled idiosyncratically; making it is challenging to read and difficult to work with due to the number of unique features.

Typically a project will use specific scripts to process and analyse the click data. This means that the scripts aren't reusable on other projects that deal with same or similar types of data.

I created a web based data visualisation tool for the initial analysis of click data. It provides a way to create abstractions and visualisations of the data to inform furthur analysis. 

## Problem

Two different papers "Identifying Latent Indicators of Technical Difficulties from Interaction Data" (Jonathan Carlton, Joshua Woodcock, Andy J Brown, John Keane, Caroline Jay) and Using Low-Level Interaction Data to Explore User Behaviour in Interactive-Media Experiences (Jonathan Carlton, Andy J Brown, Caroline Jay, John Keane) relied on static black and white data visualisations that were achieved by writing scripts specific to the dataset. Any changes to parameters had to be done manually, the script re-run, and the resulting image saved.  

This is an inefficient pipeline; making changes manually leads to more errors, and creates issues keeping track of changes to scripts and how they are used. 

There is a need to improve the Data Science pipeline by creating a generalised tool that would eliminate the need to write scripts specfic to the dataset and also create interactive data visualisations that would make data exploration and comparison quicker and easier.

The soloution was the Interactive Data Visualisation Tool (IDVT).

## IDVT

The Interactive Data Visualisation Tool (IDVT) is a web app that takes raw click data, pre processes it, and then creates a series of plots that visualises the type and density of clicks, as well as a set of summary statistics such as total number of clicks, average number of clicks per second and total time taken.

As it is web application it is easily shared and updated.

### Raw Data

The click data only needs to have four parameters.   

* **participant_id** - that refers to the individual users.
* **timestamp** - the time when the event occurred, in datetime format eg (2017-08-17 19:41:09)
* **item** - button participant has clicked on e.g. play button
* **action** - the result of clicking button e.g. play, pause etc

A common ordering that only requires four parameters, and allows the "item" and "action" parameters to be defined as users wish, means that the IDVT can be as restrictive or as flexible as needed.

When the file is uploaded to IDVT a new directory, called "input" is made to house the data and later on the data visualisations.

### Visualisations / Summary Statistics

When the "Run Analysis" button is pressed, the an "output" directory is made which houses two subdirectories, "click_plots", which houses the visulisations and "stats" which will contains the summary statistics in form of a CSV (also created now) that can be downloaded for futhur analysis.

The raw data is then pre-processed to get rid of ind and NAN values. It then creates two additional columns, "time_diff" and "action_item". "time_diff", is the value of the time that the click happened relative to the start of the experience.

Once the processing is complete, the original data is overwritten and then the visualisations are created.

The scripts create five interactive, colour visualisations and a summary statistics table.

1. **Click Type** - This displays a timeline of each particpant's clicks. Hovering over each point displays the Participant ID, Action Item and Time (in Minutes). Each unique Action Item is displayed along the right side. They can be filterted to display the type of click a user wants displayed. The "compare data on hover" option in the toolbar is useful if a user wants to see all clicks at a particular time.
2. **Click Density** - Tracks the number of clicks over 5 minute interals. Hovering over each interval will display the Participant ID, Interval time and Number of events in that interval. Individual participants can be filtered on the right.
3. **Click Count** - Histogram showing total click count. Hovering over will display the number of participants and the bin size (automatically set depending on data)
4. **Clicks Per Minute** - Histogram showing clicks per minute. Hovering over will display the number of participants and the bin size (automatically set depending on data)
5. **Time Taken (in Minutes)** - Histogram showing time between first and last clicks of each particpant. Hovering over will display the number of participants and the bin size (automatically set depending on data)
6. **Table of Stats** - A table of summary statistics.

These data points were chosen as they are fairly broad and allow for comparisons to be made between behaviour of users, the frequency and type of button clicks. The summary statistics allow for futhur analysis to be made if needed. This means that the IDVT's users can ask an array of questions of the data.

The addition of colour in the first few data visualisations makes it easier 

Each plot can be easily shared. Interactive plots can be dwonloaded as a HTML file and then opened in browser, negating the need to download additional software or dependicies. As its pure HTML it can be inserted into webpages, and used in presentations. A static copy can be downlaoded as a PNG file by clicking the camera icon in the toolbar, allowing the plots to be used in situatiions when interactivity isn't needed such as a scientific paper.

# IDVT Use Case

[CAKE](https://www.bbc.co.uk/taster/pilots/cook-along-kitchen-experience), (Cook-Along Kitchen Experience) is an online based interactive experience.  
An Object Based Media (OBM) experience from the BBC. OBM is a way to tailor  
content to the individual users based on their requirements. For example a  
TV broadcast could be broken down into various objects such as audio,  
video, subtitles, then rearranged based on the device that a viewer is  
viewing this content, whether on TV, mobile or in a browser.

In the case of CAKE, at the beginning of the experience users are asked  
several questions such as confidence cooking, number of people cooking for,  
and then tailors the experience based on the user's answers. The experience  
also scaled depending on the device the user was using.

The BBC wanted to find out how people navigate their way through this  
experience. In an internal test, users were either given the OBM experience described above or a more traditional approach with a static video accompanied by the recipe in it's written form. The click data collected from the test from both experiences informed [1] and [2]. 

As mentioned earlier, the click data was messy and difficult to gain meaningful insight from in it's raw form and bespoke scripts were wriiten to take a look at the data. Even though the results were published in two papers (see notes), writing and re-writing scripts soon became tiresome, especially when making small changes to parameters. 

[to be finalised]

Running the same data, split by user who had the OBM experience and those who had the static experience through IDVT outputs the same results but in a more interactive form.

[comment] I assume some figs of the CAKE Data can be put here. Perhaps compaing the OBM and static data sets? or having both on the same visualisation? to show how it can read click data from different sources?

## Future Use / Applications

The usefulness of the IDVT lies in its the general nature. It can be used in various points of comparison and contexts; as long as the data being used contains the minimum data points.

## Furthur Development

 Add simple slider to toggle time on plots generated by `action_item` and `click_density`. More info [here](https://plot.ly/python/sliders/)
- Make scripts more efficient for larger datasets
- Lessen the runtime on scripts.
- Ability to download plots from previously uploaded datasets. This has been set-up with separate folders. Implementation needs to be finished.

## Acknowledgements


## Papers

* [1] "Identifying Latent Indicators of Technical Difficulties from Interaction Data" -  Jonathan Carlton, Joshua Woodcock, Andy J Brown, John Keane, Caroline Jay
* [2] Using Low-Level Interaction Data to Explore User Behaviour in Interactive-Media Experiences - Jonathan Carlton, Andy J Brown, Caroline Jay, John Keane 


### How the Scripts Work

This section goes over each script and describes how it works and why it is relevant to the IDVT.

### Pre Processing - data_pre_pro.py

For the click data to work with IDVT it needs to be pre=processed. This makes sure that the data is formatted correctly for the scripts that will create the plots. It will also get rid of data that has been recorded incorrectly.

First the the inf (infinite), and NAN (Not a number) are dropped. This scrubs the data of values that would stop the visualisation scripts from running.

Next, if the click doesn't have the 'time_diff', or 'action_item' columns, it will create them using the data available. 

'time_diff' is essential for the running of the visualisation scripts as it is the time differences between the click and the beginning of the participants "session". This allows a timeline to be created in the "Click Type". Additionally it will help work out the click density in the "Click Density' plot by working out which clicks occured in each five minute interval relative to the begining of the users session.

To work out the 'time_diff' column the data is sorted by unique 'participant_id'. The 'timestamp' column is sorted in ascending order and the the first timestamp value is created
and appended to a list that will create a 'min_time' column. The 'time-diff' column is created by looping over each click of each participant and subtracting that participants 'min_time' from the click's 'timestamp'.

'action_item' is created by concantonating the 'action' and 'item' columns. 'action_item' is used in the 'Click Type" plot. It provides context to the button click by providing us with a better idea of what each click does, by telling us what the participant has clicked on ('item") and what the result of the click was, e.g. play, pause.

When the pre processing is complete the file is saved as a copy of the original data.




