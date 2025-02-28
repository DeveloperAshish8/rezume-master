import sys
import json
import joblib
import os

print("✅ Python script started", file=sys.stderr)

model_dir = os.path.join(os.path.dirname(__file__), "../models")

# Load vectorizer and model
try:
    print("✅ Loading model and vectorizer...", file=sys.stderr)
    vectorizer = joblib.load(os.path.join(model_dir, "vectorizer.pkl"))
    model = joblib.load(os.path.join(model_dir, "resume_scoring_model.pkl"))
except Exception as e:
    print(json.dumps({"error": f"Model loading failed: {str(e)}"}))
    sys.exit(1)

def predict_score(text):
    features = vectorizer.transform([text]).toarray()
    predicted_score = model.predict(features)[0]
    return predicted_score

if __name__ == "__main__":
    try:
        print("✅ Reading input from stdin...", file=sys.stderr)
        input_data = sys.stdin.read().strip()

        if not input_data:
            raise ValueError("No input data received")

        print(f"✅ Received input data: {input_data}", file=sys.stderr)
        data = json.loads(input_data)

        if not isinstance(data, dict):
            raise ValueError("Invalid JSON format: Expected dictionary")

        resume_text = data.get("resume_text")
        if not resume_text:
            raise ValueError("resume_text is missing")

        print("✅ Predicting score...", file=sys.stderr)
        score = predict_score(resume_text)

        print(json.dumps({"score": score}))

    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON input"}))
        sys.exit(1)

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
