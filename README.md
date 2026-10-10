# 🧠 Alzheimer's MRI Classifier

## About the Project
This project uses Machine Learning to classify brain MRI images into different Alzheimer's disease stages.

Users can upload an MRI image through a simple web interface and view the prediction made by the trained model.

## Features
- Upload brain MRI images
- Preview the selected image
- Predict the class using a trained ML model
- Simple, modern web interface

## Technologies Used
- Python
- TensorFlow / Keras
- Flask
- HTML, CSS, JavaScript

## Project Structure
```text
alzheimer_ml/
├── app.py
├── predict.py
├── train.py
├── my_model.keras
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/bunnyispavan/alzheimer_ml.git
cd alzheimer_ml
```

### 2. Create a virtual environment
```bash
python -m venv .venv
```

Activate it on Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the application
```bash
python app.py
```

Open the local URL shown in your terminal, usually `http://127.0.0.1:5000`.

## Team
Developed as a hackathon project.

## Disclaimer
This project is for educational and research purposes only. Its predictions are not a medical diagnosis and should not be used to make healthcare decisions.
