#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating date/time..."
sudo timedatectl set-timezone Europe/Paris
sudo apt-get update
echo "Installing base packages"
sudo apt-get install --yes git git-extras python3-pip
echo "Installing MySql"
sudo apt-get install mysql-server
echo "Change password authentification yes to no"
sudo sed -i '/PasswordAuthentication/s/yes/no/' /etc/ssh/sshd_config
echo "restart ssh for save changes"
sudo /etc/init.d/ssh restart