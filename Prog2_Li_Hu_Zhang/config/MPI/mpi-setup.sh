#! /bin/sh

sudo apt-get update
sudo apt-get -y install python-setuptools
sudo apt-get -y install python-dev
sudo apt-get -y install python-pip
sudo easy_install StarCluster
sudo pip uninstall boto -y
sudo pip install boto==2.32.0
starcluster createkey mykey -o ~/.ssh/mykey.rsa
