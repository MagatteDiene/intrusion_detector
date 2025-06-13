from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

model = joblib.load("model/random_forest_optimized.pkl")
scaler = joblib.load("model/scaler.pkl")
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'datafile' not in request.files:
        return render_template('index.html', prediction="Aucun fichier reçu")

    datafile = request.files['datafile']
    file_path = os.path.join("uploads", datafile.filename)
    os.makedirs("uploads", exist_ok=True)
    datafile.save(file_path)

    try:
        df = pd.read_csv(file_path)

        X = df.values
        X_scaled = scaler.transform(X)
        predictions = model.predict(X_scaled)

        n_intrusions = np.sum(predictions)
        total = len(predictions)


        pourcentage = (n_intrusions / total) * 100
        
        msg = f"{n_intrusions} intrusion(s) détectée(s) sur {total} lignes. ({pourcentage:.2f}%)"

        return render_template('index.html', prediction=msg)

    except Exception as e:
        return render_template('index.html', prediction=f"Erreur lors du traitement : {str(e)}")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
