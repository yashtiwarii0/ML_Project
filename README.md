# 🎯 Student Math Score Predictor – End-to-End ML Project with MLOps

This project is a complete end-to-end **Data Science** pipeline aimed at predicting a student's **Math score** based on their other academic performances. It covers everything from raw data ingestion to model deployment, following best practices in **Machine Learning** and **MLOps**.

---

## 🔍 Problem Statement

Predict the **Math score** of students using their scores in other subjects. This serves as a regression problem where the goal is to help identify students who might need extra support in mathematics based on their overall academic profile.

---

## 🚀 Key Features

* ✅ **End-to-End ML Pipeline**
  From data collection to prediction, including preprocessing, training, evaluation, and deployment.

* 📊 **Exploratory Data Analysis (EDA)**
  Understand feature distributions, relationships, and insights using statistical plots.

* ⚙️ **Modular Code Structure**
  Structured using custom Python modules under `src/` and script-based control via `main.py`.

* 🧪 **Machine Learning Models**
  Implemented multiple models and selected the best one using performance metrics.

* 🔁 **MLflow Tracking**
  Tracks experiments and metrics for each run under `mlruns/`. Integrated with **DagsHub** for remote experiment tracking.

* 📦 **MLOps with DVC**
  Handled data versioning and pipeline reproducibility using **DVC** (Data Version Control).

* 🐳 **Dockerized**
  The entire application is containerized with a `Dockerfile` for consistent environments.

* ⚠️ **Exception Handling & Logging**
  Integrated robust error handling and logging to track issues easily.

* 🌐 **Web Application**
  A minimal Flask-based interface (`app.py`) for interactive predictions.

---

## 📁 Project Structure (Key Components)

```bash
.
├── src/                   # Source code for data pipeline & modeling
├── artifacts/             # Saved models, processed data, etc.
├── notebook/              # EDA and experimentation notebooks
├── mlruns/                # MLflow tracking runs
├── app.py                 # Flask app for model inference
├── Dockerfile             # Docker container definition
├── dvc.yaml/.dvc/         # DVC pipeline files
├── requirements.txt       # Python dependencies
├── setup.py               # Project setup script
└── README.md              # Project overview
```

---

## 📌 Tech Stack

* Python 🐍
* Pandas, NumPy
* Scikit-learn, CatBoost
* Matplotlib, Seaborn
* DVC, MLflow, DagsHub
* Flask
* Docker

---

## ✅ How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/student-math-score-predictor.git

# Set up environment
pip install -r requirements.txt

# Run the main pipeline
python main.py

# Launch the app
python app.py
```

---

## 🔐 MLflow with DagsHub (Secure Setup)

To use DagsHub as a remote MLflow tracking server, create a `.env` file in your project root (make sure it's in `.gitignore`) and add the following:

```env
MLFLOW_TRACKING_URI=https://dagshub.com/yashtiwarii0/ML_Project.mlflow
MLFLOW_TRACKING_USERNAME=yashtiwarii0
MLFLOW_TRACKING_PASSWORD=1251286f313342e782ffa4daff23e5d5c253b0ee
```

Then in your Python code:

```python
from dotenv import load_dotenv
import os
import mlflow

load_dotenv()

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
mlflow.set_tracking_username(os.getenv("MLFLOW_TRACKING_USERNAME"))
mlflow.set_tracking_password(os.getenv("MLFLOW_TRACKING_PASSWORD"))
```

---

## 📊 Future Enhancements

* Add CI/CD integration with GitHub Actions
* Extend the app with Streamlit UI
* Use cloud storage and remote DVC integration (S3/GCP)
