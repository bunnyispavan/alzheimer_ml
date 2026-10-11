# 🧠 Alzheimer's Detection ML Web App

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

* **Dataset Download Link:** [Click here to download archive.zip]((https://drive.google.com/file/d/11umCeEdumM_JyZ2GpLa_dbuxKOPDBL9p/view?usp=sharing))

---

## 💻 Local Installation & Setup

Follow these quick commands to run the application server on your laptop:

### 1. Clone the Repository
```bash
git clone https://github.com/bunnyispavan/alzheimer_ml
cd alzheimer_ml
```

### 2. Install Project Dependencies
```bash
pip install -r requirements.txt
```

### 3. Running Web on Local Web
```bash
python app.py
```
Once initialized, open your browser and navigate to `http://127.0.0.1:5000` to view the web dashboard.

---

## 🚀 How it Works (The User Experience)

From the perspective of an end-user visiting the app, the entire machine learning pipeline is completely invisible. They interact with a standard, seamless web experience:

1. **Accessing the Site:** The user simply types your deployment URL (like a Vercel link) into their browser. The cloud server immediately delivers the frontend webpage (`index.html`) to their screen. To the user, it looks like a standard, lightweight website.
2. **Uploading an Image:** The user clicks a button on the screen to upload a brain MRI scan from their device and clicks "Analyze". 
3. **Instant Cloud Prediction:** In the background, the website sends that single image up to the cloud. The Python script (`app.py`) instantly resizes it to a `224x224` pixel matrix and feeds it into the pre-trained `my_model.keras` file sitting in the root folder.
4. **Getting the Result:** The model processes the image in milliseconds and determines the stage of dementia. The web app instantly updates the user's screen with the final result (e.g., "Non Dementia"). 

The user never has to download a dataset, install Python, or know anything about TensorFlow—they just get a fast, working web utility.

---

🛠️ Built With

* **Core Web Server:** Flask
* **Deep Learning Engines:** TensorFlow-CPU / Keras
* **Data Pipelines & Modeling:** NumPy, Pandas, Pillow, Scikit-Learn
