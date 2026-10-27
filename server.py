"""
Walmart Analytics Studio — Local Server & REST API
Serves index.html and provides real-time model predictions.
"""

import os
import json
import pickle
import pandas as pd
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Load models
rf_model = None
lin_model = None
if os.path.exists(os.path.join(DIRECTORY, 'outputs', 'model_rf.pkl')):
    with open(os.path.join(DIRECTORY, 'outputs', 'model_rf.pkl'), 'rb') as f:
        rf_model = pickle.load(f)

if os.path.exists(os.path.join(DIRECTORY, 'outputs', 'model_lin.pkl')):
    with open(os.path.join(DIRECTORY, 'outputs', 'model_lin.pkl'), 'rb') as f:
        lin_model = pickle.load(f)

class AnalyticsHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/api/predict':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                params = json.loads(body)
                # Form input dataframe
                sample = pd.DataFrame([{
                    'Holiday_Flag': int(params.get('holiday_flag', 0)),
                    'Temperature': float(params.get('temperature', 50.0)),
                    'Fuel_Price': float(params.get('fuel_price', 3.5)),
                    'CPI': float(params.get('cpi', 215.0)),
                    'Unemployment': float(params.get('unemployment', 7.5)),
                    'Month': int(params.get('month', 11)),
                    'WeekOfYear': int(params.get('week_of_year', 46)),
                    'lag_1': float(params.get('lag_1', 1500000.0)),
                    'lag_52': float(params.get('lag_52', 1500000.0)),
                    'roll_mean_4': float(params.get('roll_mean_4', 1500000.0)),
                    'Store': int(params.get('store', 1))
                }])
                
                rf_pred = float(rf_model.predict(sample)[0]) if rf_model else 0.0
                lin_pred = float(lin_model.predict(sample)[0]) if lin_model else 0.0
                
                response = {
                    'status': 'success',
                    'pred_rf': round(rf_pred, 2),
                    'pred_linear': round(lin_pred, 2),
                    'confidence_lower': round(rf_pred * 0.941, 2),
                    'confidence_upper': round(rf_pred * 1.059, 2)
                }
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': str(e)}).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, AnalyticsHandler)
    print(f"==================================================================")
    print(f"Walmart Retail Analytics Executive Studio running at:")
    print(f"http://localhost:{PORT}")
    print(f"Press Ctrl+C to stop.")
    print(f"==================================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    run()
