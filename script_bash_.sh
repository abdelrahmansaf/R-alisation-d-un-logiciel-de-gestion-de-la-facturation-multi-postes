#!/bin/bash
#export DEBIAN_FRONTEND-noninteractive
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating date/time..."
timedatectl set-timezone Europe/Paris
#apt-get upgrade
apt-get update
echo "Installing base packages"
apt-get install --yes git git-extras python3-pip
echo "Installing MySql"
apt -yq install mysql-server
#echo -e "\ny\n0\nAzErTy123*\nAzErTy123*\ny\ny\ny\ny" | sh /usr/bin/mysql_secure_installation
echo "Change password authentification yes to no"
sed -i '/PasswordAuthentication/s/yes/no/' /etc/ssh/sshd_config
echo "restart ssh for save changes"
/etc/init.d/ssh restart

sudo -S mysqladmin -u root password "password"
sudo mysql -e "create user 'simplon'@'localhost' identified by 'simplon123';"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'simplon'@'localhost';"
sudo mysql -e "flush privileges;"
mysql --user=simplon --password='simplon123' < database.sql
sudo systemctl start mysql