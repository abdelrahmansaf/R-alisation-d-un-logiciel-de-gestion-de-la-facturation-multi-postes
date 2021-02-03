import mysql.connector 
from mysql.connector import Error
import locale
import datetime 
locale.setlocale(locale.LC_ALL, 'fr')
#import pymysql
f='\x1b[0m'
j='\33[33m'
r='\33[91m'
n='\33[30m' 
v='\33[32m' 
b='\33[34m'
rose='\33[35m'
b_f='\33[36m'


def add_clients(cursor):
    
    """ This function allows to add a customer in the table 'clients'. 
    The user enters the fields one by one.

    cursor : Cursor is the bridge that connects Python and MySQL databases
    It will be use to execute MySQL commands. It acts like a position indicator 
    and will be mostly use to retrieve data.

    """

    type_c = input(f"particulier ou entreprise :{v} ")
    raison =input(f"{f}Votre nom :{v} ")
    email = input(f"{f}Votre email :{v}")
    adresse =input(f"{f}Votre adresse :{v}")
    tel = input(f"{f}Votre numéro de téléphone :{v}")
    sql_clients = "INSERT INTO clients (type_client,raison_sociale, email, adresse , tel) VALUES (%s, %s, %s, %s ,%s)"
    info_client = (type_c,raison,email,adresse,tel) 
    cursor.execute(sql_clients, info_client)
    connection.commit()
    voir_client = "SELECT * FROM clients ORDER BY client_id DESC LIMIT 1"
    cursor.execute(voir_client)
    res_inf = cursor.fetchone()
    print(f'{f}{b}*****Voici les infos mises à jour****{f}\n \n{j}Type client :{f} {v}{(res_inf[1])}{f} \n{j}Nom :{f} {v}{(res_inf[2])}{f} \n{j}Email:{f} {v}{(res_inf[3])}{f}\n{j}Adresse :{f} {v}{(res_inf[4])}{f}\n{j}Tel :{f} {v}{(res_inf[5])}{f}')


def recherche_facture(cursor):
    
    """ This function allows to look for an invoice in the table 'factures'. 
    The user searches from the invoice number

    cursor : Cursor is the bridge that connects Python and MySQL databases
    It will be use to execute MySQL commands. It acts like a position indicator 
    and will be mostly use to retrieve data.
    """

    user_input = (input(f"{r}Votre numéro de facture :{f} "),)
    query = ("SELECT factures.*, email,COALESCE(sum(liens_produits_factures.quantite*produits.prix_unite),0) as total_facture FROM factures LEFT JOIN liens_produits_factures ON factures.num_facture=liens_produits_factures.Fk_facture_id  LEFT JOIN produits ON produits.produit_id=liens_produits_factures.Fk_produit_id INNER JOIN clients ON factures.Fk_client_id = clients.client_id WHERE num_facture = %s group by  factures.num_facture;")
    cursor.execute(query,user_input)
    resultat_facture= cursor.fetchone()
    graph_resultat = len(resultat_facture)+3
    line_gra=graph_resultat*'-'
    print(f'{line_gra*graph_resultat} \n {v}N°{f}: {j}{resultat_facture[0]}{f} | {v}Date{f}: {j}{resultat_facture[1]}{f} | {v}E-mail{f}: {j}{resultat_facture[3]}{f} | {v}TOTAL{f}: {j}{resultat_facture[4]}{f}€ \n{line_gra*graph_resultat} ' )
# # faire une seule requête qui permet d'afficher toutes les infos de la facture    

def recherche_fature_date(cursor):
    
    """ This function allows to look for invoices issued between two dates 
    in the table 'factures'. The user enters two dates (dd/mm/yyyy)

    cursor : Cursor is the bridge that connects Python and MySQL databases
    It will be use to execute MySQL commands. It acts like a position indicator 
    and will be mostly use to retrieve data.
    """

    print("Utilises Cette Format: ({v}jour/mois/an{f}) ({v}31/01/2020{f})")
    if __name__ == '__main__' :
    
        date_input1 = (input("Entre : "))
        date_input2 = (input("Et : "))
        first = datetime.datetime.strptime(date_input1 ,"%d/%m/%Y")
        second = datetime.datetime.strptime(date_input2,"%d/%m/%Y")

    if first < second:
        date_response = ("SELECT num_facture, date_emission, email, raison_sociale from factures INNER JOIN clients ON factures.Fk_client_id = clients.client_id WHERE date_emission >= %s  AND date_emission <= %s ")
        result_date = (first,second)
        cursor.execute(date_response,result_date)
    elif first > second:
        date_response = ("SELECT num_facture, date_emission, email, raison_sociale from factures INNER JOIN clients ON factures.Fk_client_id = clients.client_id  WHERE date_emission <= %s  AND date_emission >= %s ")
        result_date = (first,second)
        cursor.execute(date_response,result_date)
    else:
        print("Vous Avez Entré Deux Datees Similaires")
    rows = cursor.fetchall()
    graph_resultat = len(rows)+2
    line_graph = graph_resultat*"-"
    for row in rows:
        print(f'{line_graph*graph_resultat}\n  N°: {v}{row[0]}{f}  |  Date:{v}{row[1]}{f} | Email:{v}{row[2]}{f} | Nom:{v}{row[3]}{f}')
#refaire la ligne de print pour qu'elle soit propre

def supprimer(cursor):
    
    """ This function allows to delete a customer 
    or an invoice in the table 'clients' or 'factures'.
    The user searches from the name or the email to delete a customer's account
    or from the invoice number to delete an invoice.

    cursor : Cursor is the bridge that connects Python and MySQL databases
    It will be use to execute MySQL commands. It acts like a position indicator 
    and will be mostly use to retrieve data.
    """

    choix_supp = input(f"Que voulez-vous supprimer client {j}(taper 1){f} ou facture {j}(taper 2){f}? {v}")
    if choix_supp == "1":
        email=(input(f"{f}Entrer l'email du client que vous voulez supprimer:{v} "),)
        supp= "DELETE FROM clients WHERE email = %s" 
        cursor.execute(supp, email)
        connection.commit()
        print(f"Ce Client{r} {email}{f} a été Bien Supprimé")
    #ajouter des infos sur client sélectionné puis demander une confirmation et informer utilisateur qu'un client a bien été supprimé
    elif choix_supp == "2": 
        facture= (input(f"{f}Entrer le numero de facture que vous voulez supprimer: {v}"),)
        supp= "DELETE FROM factures WHERE num_facture = %s" 
        cursor.execute(supp, facture)
        connection.commit()
        print(f"{f}Cette Facture {r}{facture}{f} a été Bien Supprimé")
    else :
        print("erreur")    




def modifier(cursor):
    
    """ This function allows to modify customer's informations in the table 'clients'.
    The user searches the customer he wants to modify with email or name. The user needs 
    to specify the customer id and a specific field for interact with it.
    
    cursor : Cursor is the bridge that connects Python and MySQL databases
    It will be use to execute MySQL commands. It acts like a position indicator 
    and will be mostly use to retrieve data.
    """

    nom_email1 = input(f"Vous Voulez chercher Comment?par nom ou par email ?:{v}")
    if nom_email1 == 'nom' or nom_email1 == 'NOM' :
        nom_email = input(f"{f}Quel Nom ?:{v}")
        cursor.execute("SELECT  * FROM clients WHERE raison_sociale LIKE '%s%%'" % (nom_email,))
    
    elif nom_email1 == 'email' or nom_email1 == 'email' :
        nom_email = input(f"{f}Quel email ?:{v}")
        cursor.execute("SELECT  * FROM clients WHERE email LIKE '%s%%'" % (nom_email,))
        
    resultat = cursor.fetchall()
    for row in resultat :
        print(f'{f}N° client : {v}{row[0]}{f} | type: {v}{row[1]}{f} | nom: {v}{row[2]}{f} | E-mail: {v}{row[3]}{f} | Adresse: {v}{row[4]}{f} | Tel: {v}{row[5]}{f}')
    #rendre ligne print plus propre
    quel_client =input(f"{f}Quel n° client voulez-vous modifier {j}(rentrer le n°):{f} {v}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    modif = input(f"{f}choisissez ce que voulez modifier exact: {j}(type_client , raison_sociale , email , adresse , tel):{f} {v}")
    nouveau=input(f"{f}choisissez son nouveau {modif}: {v}")
    nouvelle_valeur = (nouveau, quel_client)
    update_colonne = str("UPDATE clients SET ") + modif + str(" =%s WHERE client_id = %s ")
    cursor.execute(update_colonne,nouvelle_valeur)
    connection.commit()
    #dans cette fonction, revoir le parcours utilisateur
    #ajouter une ligne pour voir les modif
    voir_modif = "SELECT * FROM clients WHERE client_id = %s "
    cursor.execute(voir_modif, (quel_client,))
    res_ajout = cursor.fetchone() 
    print(f'{j}*****Voici les infos mises à jour****{f}\nType client : {v}{(res_ajout[1])}{f}\nNom : {v}{(res_ajout[2])}{f}\nEmail: {v}{(res_ajout[3])}{f}\nAdresse : {v}{(res_ajout[4])}{f}\nTel : {v}{(res_ajout[5])}{f}\n')

def demander_action(cursor):
    
    """ This function asks the user to choose an option. 

    cursor : Cursor is the bridge that connects Python and MySQL databases
    It will be use to execute MySQL commands. It acts like a position indicator 
    and will be mostly use to retrieve data.
    """
    
    print(f"- Tapez{v} 1 {f}pour une recherche facture\n- Taper{v} 2 {f}mpour ajouter un nouveau client\n- Taper{v} 3 {f}pour modifier les informations d'un client\n- Taper{v} 4 {f}pour rechercher des factures entre deux dates\n- Taper{v} 5 {f}pour supprimer une facture ou un client\n- Taper{v} 6 {f}pour sortir du programme")
    return input("\33[33mTapez votre choix:\x1b[0m ")

def choix_utilisateur(cursor, demande):
    
    """ This function return the customer's choice and execute a specific function.
    
    cursor : Cursor is the bridge that connects Python and MySQL databases
    It will be use to execute MySQL commands. It acts like a position indicator 
    and will be mostly use to retrieve data.
    """

    if demande == '1':
        print("Vous avez choisi l'option recherche facture")
        recherche_facture(cursor)
    elif demande == '2':
        print("Vous avez choisi ajout d'un nouveau client")
        add_clients(cursor)
    elif demande == '3':
        print("Vous avez choisi l'option modifier informations client")
        modifier(cursor)
    elif demande == '4':
        print("Vous avez choisi l'option recherche facture entre deux dates")
        recherche_fature_date(cursor)
    elif demande == '5':
        print("Vous avez choisi l'option supprimer un client ou une facture")
        supprimer(cursor)

# faire une def main() , penser à ajouter connection dans les paramètre?
def main():
    try:

        connection = mysql.connector.connect(read_default_file='C:\config1.ini',)
        db_info = connection.get_server_info() 
        print(f'{r}Connection au serveur MySql{f} {b}{db_info}{f}')
        cursor = connection.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print(f"{r}Vous êtes connecté a la base de données{f} {b}{record}{f}")
        suite ='Y'
        while True:
            if suite == 'Y' or suite =='y' :
                demande = demander_action(cursor)
                choix_utilisateur(cursor, demande)
                suite = input(f"{j}Voulez-Vous Faire Une Autre Demande{f} ({rose}Y/N{f})?")
            elif suite == 'N' or suite == 'n' :
                break

        
    except Error as e:
        print(f"{r}Erreur de connection au serveur MySQL {f}{e}")
        connection.close()
if __name__ == "__main__":
    main()


