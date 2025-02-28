import joblib
import os
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load model and vectorizer
model_dir = os.path.join(os.path.dirname(__file__), "../models")
model = joblib.load(os.path.join(model_dir, "resume_scoring_model.pkl"))
vectorizer = joblib.load(os.path.join(model_dir, "vectorizer.pkl"))

# Load test data
file_path = os.path.join(os.path.dirname(__file__), "../models/TrainingData.json")
with open(file_path, "r") as file:
    training_data = json.load(file)

df = pd.DataFrame(training_data)
df["resume_text"] = df.apply(lambda x: f"{x['job_title']} with {x['experience']} experience. Skills: {', '.join(x['skills'])}. Education: {x['education']}.", axis=1)
df["score"] = df["ats_score"].apply(lambda x: x["total"] if isinstance(x, dict) else None)

# Vectorize test data
X_test = vectorizer.transform(df["resume_text"]).toarray()
y_test = df["score"]

# Make predictions
y_pred = model.predict(X_test)

# Regression Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Function to categorize scores into classes
def categorize(score):
    if score < 60:
        return "Low"
    elif score < 80:
        return "Medium"
    else:
        return "High"

# Convert scores into categories
y_test_class = [categorize(score) for score in y_test]
y_pred_class = [categorize(score) for score in y_pred]

# Confusion Matrix
cm = confusion_matrix(y_test_class, y_pred_class, labels=["Low", "Medium", "High"])

# Plot Confusion Matrix
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Low", "Medium", "High"], yticklabels=["Low", "Medium", "High"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix for Resume Scoring")
plt.show()
