from flask import Flask
import time
from prometheus_client import start_http_server, Summary

app = Flask(__name__)

# Prometheus metric
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()
def hello():
    time.sleep(0.5)  # Simulated delay
    return "Hello from Omkar's Flask App with CI/CD + Monitoring!"

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus on port 8000
    app.run(host='0.0.0.0', port=5000)
