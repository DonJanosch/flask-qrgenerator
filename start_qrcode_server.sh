echo "Pulling the project from github"
git clone https://github.com/DonJanosch/flask-qrgenerator.git app
cd app
echo "Building and launching the container"
docker build -t flask-qrgenerator:latest .
docker run -d -p 80:8080 --restart always --name qrgenerator flask-qrgenerator
echo $(docker logs qrgenerator)
echo "All Done, Container is up and running"
