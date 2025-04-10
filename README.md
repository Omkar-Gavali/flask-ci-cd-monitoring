# 🚀 Flask CI/CD Monitoring App

This project demonstrates my understanding of **CI/CD pipelines**, **automated testing**, and **monitoring integration** — all key skills for DevOps and ML Engineering roles.

## 🔧 Tech Stack

- **Flask**: Lightweight Python web app
- **GitHub Actions**: CI pipeline for testing on every push
- **Pytest**: Unit testing
- **Prometheus Client**: Monitoring-ready integration (basic setup)

## 🎯 What This Project Proves

✅ CI/CD without Docker — using GitHub Actions to test automatically on code changes  
✅ Basic Monitoring — metrics endpoint ready for Prometheus (can be scaled)  
✅ Flask Web App with testing + version control  
✅ Real-world folder structure + deployment simulation  

## 📁 Folder Structure



flask-ci-cd-monitoring/
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── main.yml
├── README.md



## 🔄 CI Pipeline Details

Every time I push or open a pull request to `main`, GitHub Actions:

1. Installs dependencies
2. Runs tests using `pytest`
3. Logs success/failure of the build
4. Ready to add CD (e.g., deployment to Heroku, Vercel, or Dockerhub)

> Check `.github/workflows/ci.yml` to see the exact pipeline setup.

## 🌐 How to Run Locally

```bash
git clone https://github.com/your-username/flask-ci-cd-monitoring
cd flask-ci-cd-monitoring
pip install -r requirements.txt
python app.py
