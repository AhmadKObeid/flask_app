# flask_app

User managment Fullstack application developed with Flask and MongoDB. The application adds, deletes, and lists users in the mongo database.

### Run the application
- pip install -r requirements.txt
- flask run --host=0.0.0.0
- view app on localhost:5000

### Run Unit tests
- pytest

### Run Application via docker
- docker build -t flaskapp .
- docker run -p 5000:5000 flaskapp
- view app on localhost:5000

### Deploy Application in Kubernetes
- clone https://github.com/AhmadKObeid/flask_app_ops.git
- kubectl apply -f kubernetes/configmap.yaml
- kubectl apply -f kubernetes/secret.yaml
- kubectl apply -f kubernetes/deployment.yaml
- kubectl port-forward deployment/flask-app 5000:5000
- view app on localhost:5000

