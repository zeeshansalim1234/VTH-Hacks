# VTH-Hacks

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-3670A0?style=for-the-badge&logo=flask&logoColor=ffdd54)

#### API Blueprint: 
•Google-Scrapper API : https://github.com/facundoolano/google-play-scraper

•App Annie API: https://www.programmableweb.com/api/app-annie-rest-api

## What is Applytics ?

Applytics is an open-source web application bridging the gap between Users and Developers. Applytics is responsible for automatically matching Patch notes with the Bug reports reported by the Users. Often User finds it difficult to solve an issue and at times their issues remain unsolved. Developers on the other hand spend approximately about 42% of their time trying to solve bugs. Our goal is to notify the developers of the issues that are important but unsolved. Furthermore, we wish to apply this app as a tool to the pre-existing software Jira which is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management.

## Challenges we ran into:
We ran into multiple challenges along with the development phase and were dealt with accordingly. For Front-End we had challenges with aligning placeholders that were used to display the results from our Machine Learning model. For Back-End we ran into time-bounded challenges as the Machine learning model takes a considerable amount of time to create the tensor file of our embeddings. Employing a Machine Learning model also posed challenges as the packages to be downloaded were conflicting with existing packages, resolving dependencies also required a lot of time dedication. Our API choice was another thing we struggled with as we wanted to ensure we were using the best and more reliable technologies for development and debugging.

## What we learnt:

Hackathons are a great way to meet new people, network with industry professionals, learn new things, flex your problem-solving muscles, and maybe even win some great prizes.
VTHacks IX presented us with the opportunity to work on a real-life problem that is highly complex yet often overlooked in the Software Development Community.
Several Apps on App Stores, such as Google Play or the Apple Store, allow users to provide constructive or positive feedback on apps by posting their personalized reviews.
From our research, it has been clear that users reviews include bug reports, feature requests, that can assist app developers to accomplish software maintenance and evolution tasks. According to several statistics, it has been proven that several important bugs and technical issues with the advancing technology are often not noticed by the developers. This is when we decided to create a web application that helps solve this cause.

## Interface 

![image](https://user-images.githubusercontent.com/72998580/155878994-7bee243f-1fc8-4735-805a-568bcd79bdb2.png)
![image](https://user-images.githubusercontent.com/72998580/155879001-8d60fbdc-8b0b-4f25-a641-439717fb6cf3.png)
![image](https://user-images.githubusercontent.com/72998580/155881724-5c5f89ae-e6a0-430a-8a42-bb464752cc06.png)





## Technologies Used

| Stack     | Technologies Used                    |
|-----------|--------------------------------------|
| Front-End | HTML, JavaScript, CSS                |
| Back-End  | Python, Flask                        |
| Database  | MySQL                                | 
| Machine Learning | JupyterNotebook               |


## Machine Learning Models used :
  •LDA modelling (Machine Learning)
  
  •Specter Allen/AI (Generates Embeddings)
  
## API's used :

  • Google_play_scraper
  
  • App Annie
  
## ML model integration
- The reviews gathered from the Google-Scrapper API were clustered into groups of major bugs detected. This was done using LDA Topic Modelling.
- These Major Bugs are mapped to reviews using SPECTRE.
- SPECTRE model in Applytics is built using allenai-specter model with SentenceTransformers.
- Patch Notes and Negative Reviews are generated using the App Annie API and then passed these notes to the Spectre model to create embeddings.
- Proceeding to perform Cosine-Similarity to map patches to reviews and display results on Flask.
  
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
