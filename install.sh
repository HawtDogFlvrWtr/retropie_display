#!/bin/bash
sed -i -e '$i \/opt/retropie_display/display.py &\n' /etc/rc.local
sudo apt-get install git-core -y
sudo apt-get update -y
sudo apt-get upgrade -y
apt-get install --no-install-recommends htop python-dev python-pip -y
cd /opt
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
cd /opt/retropie_display/pcd8544/cpu_show/
chmod +x compile.sh
./compile.sh
pip install psutil netifaces
