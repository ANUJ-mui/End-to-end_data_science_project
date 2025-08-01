# End-to-end_data_science_project


NAME : Anuj Kumar

INTERN ID: CT04DH1662

DOMAIN : DATA SCIENCE

DURATION : 4 WEEK

MENTOR : NEELA SANTOSH

YOU HAVE TO ENTER DESCRIPTION OF YOUR TASK : COMPANY: CODETECH IT SOLUTIONS NAME: Devank INTERN ID: CT1MTWK169 DOMAIN: DATA SCIENCE DURATION : 4 WEEKS MENTOR: NEELA SANTOSH

Here's a roadmap for your end-to-end data science project, culminating in a deployed API or web app using Flask or FastAPI This project demonstrates a complete end-to-end data science pipeline—from data collection and preprocessing to machine learning model development and deployment. The goal is to solve a real-world problem by building a predictive model and making it accessible through a web-based API.

The project begins with sourcing the dataset from an open data platform. The data is then cleaned, transformed, and prepared for modeling using standard preprocessing techniques. A machine learning model is trained and evaluated to ensure reliable performance.

After training, the model is serialized and integrated into a lightweight Flask application that exposes an API endpoint for making predictions. Users can send a POST request with input data and receive predictions in real-time. This setup is then deployed to a cloud platform, showcasing the practical usability of the model through a live demo.

Deliverables: Cleaned and preprocessed dataset Trained and saved machine learning model Flask-based API for prediction Deployed application accessible via public URL README with setup instructions
Deliverables: Cleaned and preprocessed dataset Trained and saved machine learning model Flask-based API for prediction Deployed application accessible via public URL README with setup instructions.
im happy to complete this task and be a part in codetech , coming to this task i have faced many issues during completion like first i did in colab but later i found that it cannot have terminal , in this task i have used python as my core programming language thoughout this project , Pandas For data loading and preprocessing task,Scikit-learn (sklearn) For building the machine learning pipeline, including preprocessing and model training,Random Forest Classifier – The machine learning algorithm used for classification. Pickle To serialize and save the trained model. FastAPI A modern Python web framework used to build the REST API. Uvicorn ASGI server used to run the FastAPI app. Swagger UI Auto-generated API documentation that helped test and visualize the endpoints. ** Project Overview:** This project focuses on building a complete machine learning pipeline to predict the survival of passengers aboard the Titanic based on features such as age, gender, class, and fare. After training the model, I deployed it using FastAPI, so users can interact with the model in real-time through an API endpoint. The overall flow: Load Titanic dataset from a remote source. Clean and preprocess the data. Train a Random Forest classifier. Save the model using pickle. Create an API using FastAPI to make real-time predictions. Test and validate using Swagger UI. im listing some challenges faced during the task : Like every real-world project, this one came with a fair share of challenges:

Library Errors & Environment Setup: Initially, I ran into issues with installing dependencies like tensorflow, pandas, and scikit-learn due to Python version conflicts. I learned the importance of using compatible versions and managing virtual environments for smooth installations.

Module Import Errors: When I tried to run the API using Uvicorn, I kept getting ModuleNotFoundError because I had accidentally named both my folder and Python file as titanic_project, which confused Python. Renaming the file to api.py resolved the issue.

Data Preprocessing Bugs: Handling categorical data like 'Sex' and ensuring all transformations were applied consistently across training and prediction pipelines took time to debug.

Understanding ASGI and FastAPI Structure: Unlike Flask, FastAPI is async-based and follows stricter structure. Learning how to define models using Pydantic and link everything using decorators was initially confusing but became easier with practice.

What I Learned: This task was extremely beneficial in making me more confident with end-to-end machine learning deployment. Specifically, I learned:

How to clean and preprocess real-world datasets.

How to build scalable ML pipelines using Pipeline and ColumnTransformer.

How to save and load models using pickle. this was new to me but i learned during this project

How to expose ML models as REST APIs using FastAPI.

The importance of API testing and documentation using Swagger UI.

It wasn’t just about writing ML code — it was about productizing it for real-time use.

This project simulates a real-world business scenario. Predictive models like this can be applied to:

Customer churn prediction (similar data structure).

Loan approval systems in fintech.

Medical diagnosis tools (survival prediction, risk assessment).

Insurance claims and fraud detection.

Embedded decision-making tools in web or mobile apps.

By exposing the model as an API, it can be integrated into any front-end or enterprise application. For example, a travel company could integrate this model into their CRM to estimate passenger risk for certain scenarios.

This task wasn't just a coding exercise — it was a complete simulation of how machine learning models are deployed in production. It taught me to think like a developer and an engineer, not just a data scientist. By completing this project, I now have a solid understanding of how data-driven products are built from scratch and delivered to users through APIs.

I'm proud to say this project has boosted my technical confidence, and I now feel more prepared to handle full-stack data science problems in real-world settings.
