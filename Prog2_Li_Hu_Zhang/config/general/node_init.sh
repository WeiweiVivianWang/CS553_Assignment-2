#!/bin/sh

# pre-work
mkdir -p ~/Hadoop ~/Swift ~/App ~/data

# install JDK, git, pip and apache-libcloud
cd ~/App

sudo apt-get update
sudo apt-get -y install default-jdk
sudo apt-get -y install git

# set environment variable JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/default-java

wget "https://bootstrap.pypa.io/get-pip.py"
sudo python get-pip.py
rm get-pip.py

sudo pip install apache-libcloud

# download keys and credential file
mkdir -p ~/Swift/swift_conf
cd ~/Swift/swift_conf
wget "https://bitbucket.org/stevenlysc/cs553_assignment2/downloads/credentials.csv"
wget "https://bitbucket.org/stevenlysc/cs553_assignment2/downloads/mykeypair.pem"
chmod 400 mykeypair.pem

# install Hadoop
cd ~/Hadoop
wget http://www.gtlib.gatech.edu/pub/apache/hadoop/common/hadoop-1.2.1/hadoop-1.2.1.tar.gz
tar -zxf "hadoop-1.2.1.tar.gz"
rm hadoop-1.2.1.tar.gz
export HADOOP_HOME=~/Hadoop/hadoop-1.2.1
export PATH=$PATH:$HADOOP_HOME/bin

# install Swift
cd ~/Swift
wget "http://swiftlang.org/packages/swift-0.95-RC6.tar.gz"
tar -zxf "swift-0.95-RC6.tar.gz"
rm swift-0.95-RC6.tar.gz
export SWIFT_HOME=~/Swift/swift-0.95-RC6
export SWIFT_HOME=~/Swift/swift-0.95-RC6

# Download 10GB DataSet and Extract
mkdir ~/data/
cd ~/data/
wget "https://s3.amazonaws.com/cs-553/wiki10gb.xz"
#xz -d "wiki10gb.xz"

# config Swift
cd ~/Swift
git clone https://github.com/yadudoc/cloud-tutorials.git
cd cloud-tutorials/ec2
mv configs configs.default
wget "https://bitbucket.org/stevenlysc/cs553_assignment2/downloads/configs"
# Must source the setup script
#source setup.sh

# Export environment variables into system
echo export HADOOP_HOME=~/Hadoop/hadoop-1.2.1 >> ~/.bashrc
echo export PATH=$PATH:$HADOOP_HOME/bin >> ~/.bashrc
echo export SWIFT_HOME=~/Swift/swift-0.95-RC6 >> ~/.bashrc
echo export PATH=$PATH:$SWIFT_HOME/bin >> ~/.bashrc
echo export JAVA_HOME=/usr/lib/jvm/default-java >> ~/.bashrc