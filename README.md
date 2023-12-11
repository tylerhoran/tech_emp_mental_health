# Predicting Employee Use of Mental Health Services

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/tylerhoran/tech_emp_mental_health?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/tylerhoran/tech_emp_mental_health)
![GitHub pull requests](https://img.shields.io/github/issues-pr/tylerhoran/tech_emp_mental_health)
![GitHub](https://img.shields.io/github/license/tylerhoran/tech_emp_mental_health)
![contributors](https://img.shields.io/github/contributors/tylerhoran/tech_emp_mental_health)
![codesize](https://img.shields.io/github/languages/code-size/tylerhoran/tech_emp_mental_health)

## Overview

This project focuses on analyzing a dataset from an online survey on mental health conducted in 2019 by Open Sourcing Mental Illness (OSMI). The objective is to explore the state of mental health in the tech industry and develop a machine learning model to predict mental health treatment seeking behavior among tech employees.

The company stakeholder was interested in knowing if employees would use mental health services if offered. By using an existing dataset that surveyed the use of mental health services by technology employees, a model was developed that allowed a company to create a similar survey to understand the percentage of employees that woudl belikely to use mental health services if that benefit was offered to their employees.

## Dataset

The dataset used in this project is sourced from the OSMI Mental Health in Tech Survey 2019, which can be found here.

## Application

The production application, built using FastAPI and deployed on Heroku, serves as an interactive platform to predict whether individuals in the tech industry are likely to seek treatment for mental health issues based on survey responses. The application is accessible at: [Tech Mental Health](https://tech-mental-health-985271153624.herokuapp.com/).

## Features

The survey data includes various features such as age, gender, country of residence, employment details, family history of mental illness, and personal mental health experiences.

## Model

The machine learning model was trained on the survey data, focusing on predicting whether an individual is likely to seek treatment for mental health issues. Different machine learning algorithms were evaluated, with the best-performing model being deployed in the production application.

## Usage

Users can interact with the model through the web application by inputting survey-like responses. The model then predicts the likelihood of the user seeking mental health treatment.

# Code structure
Explain the code structure and how it is organized, including any significant files and their purposes. This will help others understand how to navigate your project and find specific components.

Here is the basic suggested skeleton for your data science repo (you can structure your repository as needed ):

```bash
├── data
│   ├── survey-data.csv
│   ├── data2.csv
├── model
│   ├── final_model.pkl
│   ├── preprocessor.pkl
├── test
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main_api.py
├── eda_model.ipynb
├── main.py
├── Procfile
├── README.md
├── request_app.py
├── requirements.txt
├── runtime.txt
└── setup.py
```

## Local Setup

To set up the project locally, follow these steps:

1. Clone the repository.
2. Install the required dependencies as listed in requirements.txt.
3. Run the application locally using Uvicorn or a similar ASGI server.


## Contributions

Contributions to the project are welcome. Please refer to the contribution guidelines for more details.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).

## Acknowledgments

Special thanks to Open Sourcing Mental Illness for providing the dataset and to all the contributors to this project.


