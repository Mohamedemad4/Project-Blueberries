sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt update
sudo apt install libtf2-kdl-dev python-tf2-kdl liborocos-kdl-dev liborocos-kdl1.3 libeigen3-dev ros-stereo-msgs libstereo-msgs-dev libtf2-bullet-dev libbullet-dev

