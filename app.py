import io
import os

# --- CRITICAL RE-CONFIGURATION FOR RENDER FREE TIER (512MB RAM) ---
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Silence heavy logging warnings
os.environ["OMP_NUM_THREADS"] = "1"  # Force single thread to save RAM
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"

import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from PIL import Image

# Disable internal eager execution memory allocations
tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)

app = Flask(__name__)

# Load your standard Alzheimer's Keras weights file
MODEL_PATH = "my_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

CLASSES = ["Mild Dementia", "Moderate Dementia", "Non Dementia", "Very Mild Dementia"]
print("✅ Keras model initialized safely under 512MB environment restrictions.")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file chunk found in the request"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Read image via Pillow and downsample safely
        img = Image.open(io.BytesIO(file.read())).convert("RGB")
        img = img.resize((224, 224))

        # Convert image to numpy array matrix
        img_array = tf.keras.utils.img_to_array(img)
        img_array = img_array / 255.0  # Normalize pixel density
        img_array = np.expand_dims(img_array, axis=0)

        # Execute lightweight inference evaluation
        predictions = model.predict(img_array, batch_size=1, verbose=0)

        predicted_class_idx = int(np.argmax(predictions))
        predicted_label = CLASSES[predicted_class_idx]

        return jsonify({"prediction": str(predicted_label)})

    except Exception as e:
        return jsonify({"error": f"API Evaluation failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=7860, debug=True)
