sudo apt install docker.io
#sudo systemctl enable --now docker
sudo pip3 install numpy

sudo /etc/init.d/docker start 
sudo usermod -aG docker $USER

sudo apt install docker-compose

sudo systemct1 restart docker
sudo docker stop $(docker ps -a -q)
sudo docker rm $(docker ps -a -q)

sudo docker-compose up --build
