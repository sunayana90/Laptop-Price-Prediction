from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load files
pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html',
        companies=sorted(df['Company'].unique()),
        typenames=sorted(df['TypeName'].unique()),
        cpus=sorted(df['Cpu brand'].unique()),
        gpus=sorted(df['Gpu brand'].unique()),
        oss=sorted(df['os'].unique()),
        rams=sorted(df['Ram'].unique()),
        hdds=sorted(df['HDD'].unique()),
        ssds=sorted(df['SSD'].unique())
    )

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form['company']
    typename = request.form['typename']
    ram = int(request.form['ram'])
    weight = float(request.form['weight'])
    touchscreen = 1 if request.form.get('touchscreen') == 'yes' else 0
    ips = 1 if request.form.get('ips') == 'yes' else 0
    screen_size = float(request.form['screen_size'])
    resolution = request.form['resolution']
    cpu_brand = request.form['cpu']
    hdd = int(request.form['hdd'])
    ssd = int(request.form['ssd'])
    gpu_brand = request.form['gpu']
    os = request.form['os']

    # Calculate ppi
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size

    # Create input dataframe
    query = pd.DataFrame([[company, typename, ram, weight, touchscreen, ips, ppi,
                           cpu_brand, hdd, ssd, gpu_brand, os]],
                         columns=['Company', 'TypeName', 'Ram', 'Weight',
                                  'Touchscreen', 'Ips', 'ppi', 'Cpu brand',
                                  'HDD', 'SSD', 'Gpu brand', 'os'])

    # Make prediction
    prediction = int(np.exp(pipe.predict(query)[0]))

    return render_template('index.html',
        companies=sorted(df['Company'].unique()),
        typenames=sorted(df['TypeName'].unique()),
        cpus=sorted(df['Cpu brand'].unique()),
        gpus=sorted(df['Gpu brand'].unique()),
        oss=sorted(df['os'].unique()),
        rams=sorted(df['Ram'].unique()),
        hdds=sorted(df['HDD'].unique()),
        ssds=sorted(df['SSD'].unique()),
        prediction_text=f"Predicted Price: ₹{prediction:,}"
    )

if __name__ == '__main__':
    app.run(debug=True)
