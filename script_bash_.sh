#!/bin/bash
sed -i 's/#\?\(PerminRootLogin\s*\).*$/\1 no/' /etc/ssh/sshd_config
service ssh reload
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating date/time..."
timedatectl set-timezone Europe/Paris
#apt-get upgrade
apt-get update
echo "Installing base packages"
apt-get install --yes git git-extras python3-pip
sudo ps aux | grep -i apt
echo "Installing MySql"
apt -yq install mysql-server
apt install --yes crudini
echo "Change password authentification yes to no"
sudo sed -i 's/#\?\(PasswordAuthentication\s*\).*$/\1 no/' /etc/ssh/sshd_config
echo "restart ssh for save changes"
/etc/init.d/ssh restart
echo "Updating mysql configs in /etc/mysql/my.cnf."
sudo chmod 600 /etc/mysql/my.cnf
crudini --set /etc/mysql/my.cnf mysqld bind-adress 0.0.0.0
sudo -S mysqladmin -u root password "Joco75015"
sudo mysql -e "create database compte;"
sudo mysql -e "create user 'simplon'@'%' identified by 'simplon123';"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'simplon'@'%';"
sudo mysql -e "flush privileges;"
mysql --user=simplon --password='simplon123' < database.sql
sudo systemctl stop mysql
sudo systemctl start mysql
sed -i 's/#\?\(PerminRootLogin\s*\).*$/\1 yes/' /etc/ssh/sshd_config
sudo service ssh reload
