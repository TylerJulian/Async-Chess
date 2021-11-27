sudo apt install docker.io
#sudo systemctl enable --now docker

sudo /etc/init.d/docker start 
sudo usermod -aG docker $USER

sudo apt install docker-compose

sudo docker-compose up --build
