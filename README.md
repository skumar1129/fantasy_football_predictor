# Project Background
This project is full stack application that also uses some data work. The project is a website that allows a user to choose a football player will give their projected fantasy football output for the following season. It is able to give this projection using a machine learning algorithm called linear regression. However, we first gather the data from a website using a webscraper, then we take that data to train our model. Finally we run our model against the remaining players and store the results in a local mongodb instance.

## Tech Stack / Folder Explanation
backend: Python Flask application to grab precomuted scores from model
<br>
data store: Local mongodb instance
<br>
model_trainer: Jupyter Notebook to read in data, cleanse it, and construct the model
<br>
react-frontend: Frontend written in React
<br>
webscraper: Python script that uses beautiful soup to scrape data for model
