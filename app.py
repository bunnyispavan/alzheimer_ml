import io
from flask import Flask, jsonify, render_template, request
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

# 1. LOAD YOUR ALZHEIMER'S MODEL
MODEL_PATH = "my_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# 2. DEFINED STAGE LABELS
# Ensure this list maps perfectly to the output class tracking order of your model
CLASSES = ["Mild Dementia", "Moderate Dementia", "Non Dementia", "Very Mild Dementia"]

print("✅ Keras model running with 224x224 layout matrix alignment.")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check if an actual file was uploaded
        if "file" not in request.files:
            return jsonify({"error": "No file chunk found in the request"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Open the image using Pillow and convert to standard RGB mode
        img = Image.open(io.BytesIO(file.read())).convert("RGB")

        # 3. PREPROCESS THE IMAGE PIXELS
        # Corrected image dimension structure to 224x224 pixels
        img = img.resize((224, 224))

        # Convert image data matrix into a numpy floating array
        img_array = tf.keras.utils.img_to_array(img)

        # Scale pixel range between 0.0 and 1.0 (Normalization standard)
        img_array = img_array / 255.0

        # Expand data dim to create batch format shape: [1, 224, 224, 3]
        img_array = np.expand_dims(img_array, axis=0)

        # 4. RUN MODEL PREDICTION
        predictions = model.predict(img_array)

        # Extract numerical class positioning array index
        predicted_class_idx = int(np.argmax(predictions))
        predicted_label = CLASSES[predicted_class_idx]

        # Return explicit raw string values back to frontend
        return jsonify({"prediction": str(predicted_label)})

    except Exception as e:
        return jsonify({"error": f"API Analysis error line exception: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
