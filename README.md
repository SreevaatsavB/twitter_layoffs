# Automated tweets collection

Tweets about the topic "layoffs" will be collected everyday after 12am IST and will be added to the repository. This automation is done using Github Actions.

This repo consists of 3 main files:- 
- requirements.txt :- A file consisting the required packages to be installed in the enviornment.
- twitter_scape.py :- Fetches the tweets of the required topic using snscrape library and saves the dataframe of tweets into the repo.
- actions.yml :- Automates the process of collection, adding and commiting the new data into the repo. 
