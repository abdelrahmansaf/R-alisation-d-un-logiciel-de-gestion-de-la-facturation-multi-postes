set/p ip=Read-host -Prompt 'Tapez votre nom_serveur@192.168.1.XXX :'
ssh  %ip% " mkdir -p ~\.ssh "
scp  C:\Users\.ssh\id_rsa.pub %ip%:.ssh/authorized_keys
scp  C:\Users\database_test.sql %p%:./scriptt.sql
ssh %ip%



