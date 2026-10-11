# 🧠 Alzheimer's Detection Machine Learning Web App

A machine learning-powered web application designed to detect and classify Alzheimer's Disease. This project features a trained deep learning model integrated with a clean Flask web interface, optimized for fast and lightweight cloud deployment.

---

## 📁 Repository Structure
Your repository follows a clean, production-ready structure where all core execution logic and model weights sit directly in the root directory:

```text
├── templates/
│   └── index.html       # Web application user interface (HTML frontend)
├── .gitignore           # Specifies intentionally untracked local dataset files
├── README.md            # Project documentation and hackathon submission guide
├── app.py               # Flask web server handling routing and user form uploads
├── my_model.keras       # Pre-trained Keras deep learning model weights
├── predict.py           # Inference script to load model and process inputs
├── requirements.txt     # Python package dependencies optimized for cloud environments
└── train.py             # Script used to train the machine learning model locally
```

---

## 📊 Dataset & External Hosting

Due to the large size of medical neuroimaging assets, the raw training data is securely hosted externally to keep the active deployment build and Git architecture completely lightweight.

* **Dataset Download Link:** [Click here to download archive.zip from Google Drive](PASTE_YOUR_GOOGLE_DRIVE_LINK_HERE)

### Local Development Data Setup
To retrain the model or test your training code locally:
1. Download the `archive.zip` file using the shared Google Drive link.
2. Extract the archive contents into a folder named `data/` or `dataset/` in the root of your local project space.
3. The dataset files will remain local and hidden from your cloud commits since they are completely blocked via your active `.gitignore` rules.

---

## 🚀 How it Works (Cloud Architecture)

1. **Training (Local Framework):** `train.py` was executed locally utilizing the 500MB dataset to train the deep learning network, outputting the frozen weights inside `my_model.keras`.
2. **Inference (Cloud Production/Vercel):** When deployed to the cloud, the system **does not require the raw dataset**. The Flask app (`app.py`) loads the lightweight `my_model.keras` file into active serverless memory and executes quick individual evaluations on user-uploaded images on-the-fly.

---

## 💻 Local Installation & Setup

Follow these quick commands to run the application server on your laptop:

### 1. Clone the Repository
```bash
git clone https://github.com
cd alzheimer_ml
```

### 2. Install Project Dependencies
```bash
pip install -r requirements.txt
```

### 3. Spin Up the Local Server
```bash
python app.py
```
Once initialized, open your browser and navigate to `http://127.0.0.1:5000` to view the web dashboard.

---

## 🛠️ Built With

* **Core Web Server:** Flask
* **Deep Learning Engines:** TensorFlow-CPU / Keras
* **Data Pipelines & Modeling:** NumPy, Pandas, Pillow, Scikit-Learn
