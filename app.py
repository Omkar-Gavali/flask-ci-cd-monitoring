from flask import Flask
from prometheus_client import generate_latest, Counter

app = Flask(__name__)
page_visits = Counter('page_visits', 'Number of visits to the homepage')

@app.route('/')
def home():
    page_visits.inc()
    return "CI/CD Pipeline without Docker is working!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4'}
