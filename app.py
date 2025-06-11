from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and dataset
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', df=df)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form['company']
    type = request.form['type']
    ram = int(request.form['ram'])
    weight = float(request.form['weight'])
    touchscreen = 1 if request.form['touchscreen'] == 'Yes' else 0
    ips = 1 if request.form['ips'] == 'Yes' else 0
    screen_size = float(request.form['screen_size'])
    resolution = request.form['resolution']
    cpu = request.form['cpu']
    hdd = int(request.form['hdd'])
    ssd = int(request.form['ssd'])
    gpu = request.form['gpu']
    os = request.form['os']

    # Compute PPI
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    # Create input array
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]).reshape(1, 12)

    # Predict price
    predicted_price = int(np.exp(pipe.predict(query)[0]))

    return render_template('result.html', price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
