set/p ip=Read-host -Prompt 'Tapez votre nom_serveur@192.168.1.XXX :'
ssh %ip% "mkdir -p ~/.ssh/"
type C:\Users\utilisateur\.ssh\id_rsa.pub | ssh %ip% "cat >> ~/.ssh/authorized_keys"
scp C:\Users\utilisateur\Documents\svr_install\script_bash.sh %ip%:./script_bash.sh
scp C:\Users\utilisateur\Documents\svr_install\db_comptable.sql %ip%:./database.sql
ssh %ip% "sed -i -e 's/\r$//' ./script_bash.sh"
ssh %ip% "chmod 777 ./script_bash.sh"
ssh %ip% "chmod 777 ./database.sql"
pip install mysql-connector-python
ssh %ip%