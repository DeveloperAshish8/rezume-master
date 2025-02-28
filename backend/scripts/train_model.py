import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os
model_dir = os.path.join(os.path.dirname(__file__), "../models")

# Ensure directory exists
os.makedirs(model_dir, exist_ok=True)

# Load training data from JSON file
file_path = os.path.join(os.path.dirname(__file__), "../models/TrainingData.json")
with open(file_path, "r") as file:
    training_data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame(training_data)

# Extract relevant fields for training
df["resume_text"] = df.apply(lambda x: f"{x['job_title']} with {x['experience']} experience. Skills: {', '.join(x['skills'])}. Education: {x['education']}.", axis=1)
df["score"] = df["ats_score"].apply(lambda x: x["total"] if isinstance(x, dict) else None)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=100)
X = vectorizer.fit_transform(df['resume_text']).toarray()
y = df['score']

# Save vectorizer
joblib.dump(vectorizer, os.path.join(model_dir, "vectorizer.pkl"))

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, os.path.join(model_dir, "resume_scoring_model.pkl"))  


print("Model trained and saved successfully!")

