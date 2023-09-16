from flask import Flask, jsonify
import pandas as pd
import joblib
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load('../model.pkl')

@app.route('/previsao/<start_date>/<end_date>', methods=['GET'])
def previsao(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        date_range = []
        current_date = start_date
        while current_date <= end_date:
            date_range.append(current_date)
            current_date += timedelta(days=1)

        forecasts = []
        for date in date_range:
            forecast = model.predict(pd.DataFrame({'ds': [date]}))
            forecast_date = forecast['yhat'].values[0]
            forecasts.append({'data': date.strftime('%d/%m/%Y'), 'previsao': forecast_date})

        return jsonify({'previsoes': forecasts})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
