## Creating a Interactive Data Visualisation Tool

[CAKE](https://www.bbc.co.uk/taster/pilots/cook-along-kitchen-experience), (Cook-Along Kitchen Experience) is an online based interactive experience.  
An OBM (Object Based Media) experience from the BBC. OBM is a way to tailor  
content to the individual users based on their requirements. For example a  
TV broadcast could be broken down into various objects such as audio,  
video, subtitles, then rearranged based on the device that a viewer is  
viewing this content, whether on TV, mobile or in a browser.

In the case of CAKE, at the beginning of the experience users are asked  
several questions such as confidence cooking, number of people cooking for,  
and then tailors the experience based on the user's answers. The experience  
also scaled depending on the device the user was using.

The BBC wanted to find out how people navigate their way through this  
experience. To do this different types of interaction data was collected. 
Research has shown that low level interaction data such as button clicks 
are an indicator of interaction behaviour.

The click data was messy and difficult to gain meaningful insight from in it's raw form.
Initially bespoke scripts were written to take a look at the data. Even though the results 
were published in two papers (see notes), writing and re-writing scripts soon became tiresome,
especially when making small changes to the parameters. The usefulness of a tool that 
could automate the process by allowing the user to change the parameters for themselves as well
as interact with the plots, soon became apparent. If it was generalised, the tool could
be re-used in other projects that require the analysis of click data.

That's what the Interaction Data Visualisation Tool (IDVT) does all of this. It's a web tool
takes the click data, processes it, and creates several different interactive visualisations to
give researchers a way to start their analysis of the data. As it's a web app it can be easily shared, used and updated. 
Additionally, the ability to download the plots as HTML or PNG files means that the results can be shared with other researchers and
easily added to papers. Having the summary statistics (eg clicks per minute, total time taken etc) available means that 
further analysis can be made.

As the tool is generalised it can be used with any click data as long as each action contains four simple parameters, 
a participant_id, timestamp, action and item. This means that the IDVT can be reused in other projects that deal with click data,
speeding up their initial analysis, leaving more time to make an in-depth 

### Notes
* "Identifying Latent Indicators of Technical Difficulties from Interaction Data" -  Jonathan Carlton, Joshua Woodcock, Andy J Brown, John Keane, Caroline Jay
* Using Low-Level Interaction Data to Explore User Behaviour in Interactive-Media Experiences - Jonathan Carlton, Andy J Brown, Caroline Jay, John Keane 