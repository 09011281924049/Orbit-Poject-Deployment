from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('arima_cast', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', purchase="", months="")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    months = [x for x in request.form.values()][0]
    
    prediction = model.predict(start=104, end=104 + int(months), typ='levels').rename('ARIMA Predictions')

    output = prediction.to_json()

    return render_template('index.html', purchase=output, months=months)


if __name__ == '__main__':
    app.run(debug=True)