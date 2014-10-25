#!/bin/sh

# connect to the server -- key: $1 ip: $2
ssh -i $1 ubuntu@$2 "
wget "https://bitbucket.org/stevenlysc/cs553_assignment2/downloads/swift_init.sh"
chmod +x swift_init.sh
./swift_init.sh
rm swift_init.sh
"

ssh -i $1 ubuntu@$2