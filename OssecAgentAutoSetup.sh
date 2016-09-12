#!/bin/bash
sudo add-apt-repository -y ppa:git-core/ppa
sudo apt-get -y update
sudo apt-get -y install git
sudo apt-get -y install gcc make
sudo apt-get -y install libssl-dev
cd ~
mkdir ossec_tmp && cd ossec_tmp
git clone -b stable https://github.com/wazuh/ossec-wazuh.git
cd ossec-wazuh
sudo ./install.sh <<!
en

agent

10.0.4.142






!
curl -u foo:bar -k -X PUT https://<master-ip>:55000/manager/restart
sleep 20
sudo /var/ossec/bin/agent-auth -m <master-ip> -p 1515
sleep 20
sudo /var/ossec/bin/ossec-control start
sleep 20
