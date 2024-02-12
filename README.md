# Project Title - Book Recommendation System
Final Project
=======
This README document provides an overview and step-by-step guide for building a machine learning model for our book recommendation system.
In this project, we are building a Recommendation Engine based on User ratings of Books. This will help readers decide their next read or can be adapted for their specific use cases.

## Overview
This book recommendation system attempts to suggest books to users based on their preferences, past interactions, and similarities between users and books. Various machine learning techniques were used to build the system by analyzing historical user-book interaction data and deriving patterns to make personalized recommendations.

In this project, we built a machine learning model to recommend books to users based on their previous reads (rating history), if applicable, or based on the most popular books in the database. We also analysed and created visualizations to show interesting insights from the data. Also, we built a web application using Flask. This will help readers decide their next read, search for books related to their reading history or what others are reading and can be adapted for other specific use cases.

The project can be run using following steps:
1. Generate the Pickle files  - Run Jupyter Notebooks to get the data in pickle files
2. Running the Flask Application - Run the app.py file to get the data
3. Website - The html page will by default display a Most Popular Books. There are pages to Recommend based on Book Titles, Recommend by User id , Search for a book and Data Insights

### Limitations
This engine uses a static set of data. Due to time constraints, we could not build a recommender system that can work with new data in this iteration of the project.

### Dataset
Our dataset was obtained from [Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset). It included these 3 files providing metadata about users and books. We generated a fourth dataset, for further analysis and visualizations.

Books:ISBN, Book title, Book author, Year of publication, Publisher
Users: User ID, Location(country)
Ratings: User ID, ISBN, Book rating
Geo Location: Country, Latitude, Longitude

### Methodology
The project consisted of the following broad steps. Step by step processes are commented within the .ipynb file:
1. Data Preprocessing and exploratory data analysis
2. Researching and experimenting on various recommendation system techniques - we tried collaborative filtering, content-based filtering and matrix factorization techniques. 
3. Create dashboard visualizations 
4. Interactive website - The html home page will by default display top rated books by users. Navigating to other pages will display a search bar to search by users and book titles. 

### Preprocessing
This involved cleaning the data, handling missing values, encoding categorical variables, and splitting the data into training and testing sets. Specific preprocessing steps can be found in the respective .ipynb file.

### Feature Engineering
This involved creating new features or transforming existing features to improve the performance of our recommendation system. For example, we calculated and assigned average weighted score for ratings.

### Training, Cross-validation and Evaluation
Our Recommender engine is focused on Collaborative Filtering (books similarity and user similarity)
We trained two machine learning models using:

1. Singular Value Dcomposition (SVD), and
2. SVD Funk (which was popularized by Simon Funk during the Netflix Prize) using the training dataset.
We also cross-validated the model using the Surprise module, and hypertuning SVD to identify the best parameters and ensure robustness of the model.
We evaluated our model's performance using appropriate evaluation metrics such as RMSE (Root Mean Squared Error) and number of latent factors for accuracy. 

The SVD model using the weighted mean ratings performed the best.

### Tools, Languages and Libraries
Machine Learning - Singular Value Decomposition (SVD)
Visualization - Tableau
Web Development - Flask, HTML, CSS
Data Preprocessing and EDA - Python, Jupyter Notebook, Pandas, Matplotlib, Numpy, Scipy, Scikit-learn
IDE - Visual Studio Code

### References
[Recommendation Engine Concepts](https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-recommendation-engine-python/)  
[BootStrap](https://www.w3schools.com/bootstrap/bootstrap_get_started.asp)  
[Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)  
[Jinja Template](https://jinja.palletsprojects.com/en/3.1.x/)  
[CSS](https://www.w3schools.com/css/)  


### Acknowledgements
Project Team:
1. Daria Z.
2. Neha S.
3. Seeke O.D
4. Valentyna K.

It has been great working and learning with you all.

 
