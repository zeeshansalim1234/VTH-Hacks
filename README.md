# VTH-Hacks

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-3670A0?style=for-the-badge&logo=flask&logoColor=ffdd54)

#### API Blueprint: 
•Google-Scrapper API : https://github.com/facundoolano/google-play-scraper

•App Annie API: https://www.programmableweb.com/api/app-annie-rest-api

## What is Appanalytics ?

Applytics is an open source web application bridging the gap betweeen User and Developers. Applytics is responsible for automatically matching Patch notes with the Bug reports reported by the Users. Often User's find it difficult to solve an issue and at times their issues remain unsolved. Developers on the otherhand spend approximately about 42% of their time trying to solve bugs. Our goal is to notify the developers of the issues that are important but unsolved. Furthermore, we wish to apply this app as a tool to the pre-existing software Jira which is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management. 

## Challenges we ran into:
We ran into multiple challenges along the development phase and were dealt with accordingly. With respect to Front-End we had challenges with aligning of placeholders that were used to display the results from our Machine Learning model. With respect to Back-End we ran into time bounded challenges as Machine learning model takes a considerable amount of time to create the tensor file of our embeddings. Employing a Machine Learning model also posed as challenges as the packages to be downloaded were conflicting with existing packages, resolving dependies also required a lot of time dedication. Our API choice was another thing we struggled with as we wanted to ensure we were using the best and more reliable technologies with respect to development and debugging.

## What we learnt:

Hackathons are a great way to meet new people, network with industry professionals, learn new things, flex your problem-solving muscles, and maybe even win some great prizes.
VTHacks IX presented us with the opportunity to work on a real-life problem that is highly complex in nature yet often overlooked in the Software Developement Community.
Several Apps on App Stores, such as Google Play or the Apple Store, allow users to provide constructive or positive feedback on apps by posting their personalized reviews.
From our research it has been clear that users reviews includes bug reports, feature requests, that can assist app developers to accomplish software maintenance and evolution tasks. According to several statistics it has been proven that several important bugs and technical issues with the advancing technology are often not noticed by the developers.
This is when we decided to create a web application which helps solve this cause.


## Technologies Used

| Stack     | Technologies Used                    |
|-----------|--------------------------------------|
| Front-End | HTML, JavaScript, CSS                |
| Back-End  | Python, Flask                        |
| Database  | MySQL                                | 
| Machine Learning | JupyterNotebook               |


## Machine Learning Models used :

  •Bert-Extractive-Summarizer (Generates summary)

  •Specter (Generates Embeddings)

## Technologies Used :

  • HTML5 •CSS3 •Python 
  • Flask •JS •JupyterNotebook
  •PowerShell
  
## API's used :

  • Google_play_scraper
  
  • App Annie
  
## ML model integration
- The reviews gathered from the Google-Scrapper API was clustered into groups of major bugs detected. This was done using LDA Topic Modelling.
- These Major Bugs are mapped to reviews using SPECTRE.
- SPECTRE model in Appanalytics is built using allenai-specter model with SentenceTransformers.
- Patch Notes and Negative Reviews are generated using the App Annie API and then passing these notes to the Spectre model to create embeddings.
- Proceeding to perform Cosine-Similarity to map patches to reviews and displaying results on Flask.
  
## Prequisites to run the ML Model
```
pip install regex
pip install torch
pip install pickle5
pip install sentence-transformers
pip install pandas
pip install neattext
pip install transformers requests beautifulsoup4 pandas numpy
```
## License
