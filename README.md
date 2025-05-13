🎯 Student Math Score Predictor – End-to-End ML Project with MLOps

This project is a complete end-to-end Data Science pipeline aimed at predicting a student's Math score based on their other academic performances. It covers everything from raw data ingestion to model deployment, following best practices in Machine Learning and MLOps.
🔍 Problem Statement

Predict the Math score of students using their scores in other subjects. This serves as a regression problem where the goal is to help identify students who might need extra support in mathematics based on their overall academic profile.
🚀 Key Features

    ✅ End-to-End ML Pipeline
    From data collection to prediction, including preprocessing, training, evaluation, and deployment.

    📊 Exploratory Data Analysis (EDA)
    Understand feature distributions, relationships, and insights using statistical plots.

    ⚙️ Modular Code Structure
    Structured using custom Python modules under src/ and script-based control via main.py.

    🧪 Machine Learning Models
    Implemented multiple models and selected the best one using performance metrics.

    🔁 MLflow Tracking
    Tracks experiments and metrics for each run under mlruns/.

    📦 MLOps with DVC
    Handled data versioning and pipeline reproducibility using DVC (Data Version Control).

    🐳 Dockerized
    The entire application is containerized with a Dockerfile for consistent environments.

    ⚠️ Exception Handling & Logging
    Integrated robust error handling and logging to track issues easily.

    🌐 Web Application
    A minimal Flask-based interface (app.py) for interactive predictions.

📌 Tech Stack

    Python 🐍

    Pandas, NumPy

    Scikit-learn, CatBoost

    Matplotlib, Seaborn

    DVC, MLflow

    Flask

    Docker

📊 Future Enhancements

    Add CI/CD integration with GitHub Actions

    Extend the app with Streamlit UI

    Use cloud storage and remote DVC integration (S3/GCP)
