# Course Project-03: ICC Cricket World Cup 2023 ML challenge

In this project we are performing different kinds of tasks using Machine Learning and Deep Learning algorithms which are briefly explained below, this model is then deployed using FastAPI and the Uvicorn ASGI web server.

## Data_Scraping_and_Cleaning.ipynb

This file contains the code we have used for scraping data from the internet to be used as datasets for different tasks in the project.

## Task1.ipynb

In this file, we have built a model to predict the following

i) the top 5 batsman who will hit most sixes in the tournament.

ii) the top 5 bowlers who will be the leading wicket-taker in the tournament.

iii) the top bowler who took maximum number of 4-wicket haul.

## Task2.ipynb

In this file, we have built a model to predict the playing 11 for the teams playing the final match. The finalists have already been predicted in task 3 and we have used a representative team for showcasing the prediction of our model.

## Task3.ipynb

In this file, we have predicted the winner of the World Cup. For this, we have used a step-by-step approach. We used a dataset of all matches played between 2015-2023 before the World Cup and built a model to predict the winners of each match in the current World Cup. From the winners list, we built a leaderboard to obtain the teams qualified for semi-finals. Then, we virtually conducted the semi-finals and finals to obtain the winner of the World Cup.

To run this FastAPI application, follow these steps:

## Requirements

Make sure you have the following installed:

- Python 3.x
- FastAPI
- Uvicorn
- Pickle

## Usage

## 1. Install the required libraries using pip:
```bash 
pip install fastapi uvicorn numpy pickle pandas scikit-learn
```

## 2. Command to run API server:
```bash
python -m uvicorn main:app --reload
```

## 3. The API will be accessible at http://127.0.0.1:8000
- You can see outcomes by sending POST requests to http://127.0.0.1:8000/docs with JSON data in the format specified by the 'Task2_API.py' and 'Task3_API.py '.

## API Endpoints
```
/Top 6 Bowlers of INDIA!!: Endpoint to predict the top 6 bowlers of each country.
/Prediction of 11 Players for INDIA!!: Endpoint to predict the 11 players for each country.
/Final_Winner: Endpoint to predict semifinalists, finalists, and the winner of the ICC World Cup.
//Finalists: Endpoint to predict finalists of the ICC World Cup.
/Semifinalists: Endpoint to predict semifinalists of the ICC World Cup.
```
