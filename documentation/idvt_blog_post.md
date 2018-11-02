## Creating a Interactive Data Visualisation Tool for click data.

[CAKE](https://www.bbc.co.uk/taster/pilots/cook-along-kitchen-experience), (Cook-Along Kitchen Experience) is an online based interactive experience that allows users to cook along with the presenter. It does this using Object Based Media (OBM). OBM is a different way of delivering media. For example a TV show will deliver audio, video, subtitles components at the same time regardless of device. It can be inflexible. OBM separates these components and assembles them as late as possible before they reach the user. This enables the components to be changed based on different contexts, such as dynamically changing the screen size based on their device or changing the audio mix depending on how they are listening. It also takes into account the user's individual preferences.

In the case of CAKE, the key feature was that audience members could choose which recipes they wanted, and the component steps (i.e the audio, video, subtitles etc) could be delivered to the user so they could follow along with the recipe in real time. For example, if they got behind the different components would be rescheduled to sompenstate.

BBC R&D wanted to find out if this approach to content delivery would benefit the user. A trial was set-up to see how participants navigated their way through the OBM CAKE experience compared with the same content presented in a traditional fashion, in this case a static video with the written recipe displayed alongside. Different types of interaction data was collected to see if it could be used to learn more about the user. For example, how engaged they were, whether we could tell if the had technical or UI difficulties.

The large amount of data made it difficult to sift through so we focused on button click data, as it could give us some understanding into how the user behaves during the experiences. would be useful.The click data was messy and difficult to gain meaningful insight from in it's raw form. Initially bespoke scripts were written to filter, sort and eventually visualise the data.Even though the results were published in two papers (see notes), writing and re-writing scripts soon became tiresome,especially when making small changes to the parameters. The usefulness of a tool that could automate the process by allowing the user to change the parameters for themselves as well as interact with the plots, soon became apparent. Even better, if the tool was generalised it could be re-used in other projects that require the analysis of click data.

That's what the Interaction Data Visualisation Tool (IDVT) does. It is web tool that automates the processing of the data and the creation of several different interactive visualisations that explore the type of clicks, the density of clicks, and histograms displaying the summary statistics. It's a is a quick and easy way to make initial visualisations as the first step before a more detailed look at the data. As IDVT is a web app it can be easily shared, used and updated. Additionally, the ability to download the plots as HTML or PNG files means that the results can be shared with other researchers and easily added to papers. Additionally, due to the general nature of the tool it can be used with any click data as long as each action contains four simple parameters, a participant_id, timestamp, action and item. This means that the IDVT can be easily used in other projects that deal with click data, speeding up their initial analysis, leaving more time to explore the dataset in more detail and form a hypothesis from the data. 

### Notes
* "Identifying Latent Indicators of Technical Difficulties from Interaction Data" -  Jonathan Carlton, Joshua Woodcock, Andy J Brown, John Keane, Caroline Jay.
* Using Low-Level Interaction Data to Explore User Behaviour in Interactive-Media Experiences - Jonathan Carlton, Andy J Brown, Caroline Jay, John Keane. 