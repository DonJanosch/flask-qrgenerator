echo "Now: Pulling project from github"
git clone https://github.com/DonJanosch/flask-qrgenerator.git app && cd app
echo "Now: Building the docker image and starting a container"
docker build -t flask-qrgenerator:latest .
docker run -d -p 80:8080 --restart always --name qrgenerator flask-qrgenerator
echo "All Done, Container is up and running. Visite http://$(hostname -I | cut -d' ' -f1)"
