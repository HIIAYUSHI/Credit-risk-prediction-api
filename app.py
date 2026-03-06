from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)


@app.route("/")
def home():
    return str(feature_names)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]

    # Arrange features in correct order
    input_data = [data[feature] for feature in feature_names]

    prediction = model.predict([input_data])

    return jsonify({"prediction": int(prediction[0])})


if __name__ == "__main__":
    app.run(debug=True)