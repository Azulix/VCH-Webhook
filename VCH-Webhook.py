import requests
import os
from colorama import init, Fore
from dhooks import *
import time
cooldown_spam = 0


init(convert=True)



choices = 'Webhooks Tools\n\n'+ Fore.RED + '[0] ' + Fore.GREEN + 'Webhook Sender \n' + Fore.RED + '[1] ' + Fore.GREEN + 'Webhook Deleter \n' + Fore.RED + '[2] ' + Fore.GREEN + 'Webhook Spammer \n'  + Fore.RED + '[3] ' + Fore.GREEN + 'Webhook Renamer \n' 
def main():
    os.system("cls")
    os.system("color A")

    print(choices)
    print()
    print()
    print()
    choice = input("Choice" + Fore.RED + " → ")
 
    if choice == '0':
        os.system("title Webhook Sender")
        WebhookURL = input(Fore.GREEN + "Veuillez envoyer le webhook" + Fore.RED + " →	")
        WebhookMSG = input(Fore.GREEN + "Veuillez envoyer le message" + Fore.RED + " →	")      
        hook = Webhook(WebhookURL)
        hook.send(WebhookMSG)
        os.system("cls")
        input(Fore.WHITE + "Message envoyé avec succès ! Veuillez appuyer sur entrée pour retourner dans le menu principal.")  
        main()
            
                
                
	
    if choice == '1':   
        os.system("title Webhook Deleter") 
        Deleter = input(Fore.GREEN + "Veuillez envoyer le webhook à supprimer" + Fore.RED + " →	")      
        requests.delete(Deleter)
        print("Webhook: " + Fore.RED + Deleter + " a été supprimé avec succès !") 
        os.system("cls")              
        input(Fore.WHITE + "Webhooks supprimé avec succès ! Veuillez appuyer sur entrée pour retourner dans le menu principal.")
        main()
        
    if choice == '2':   
        os.system("title Webhook Spammer") 
        webhookURL1 = input(Fore.GREEN + "Veuillez envoyer le lien du webhook à spam" + Fore.RED + " →	")
        webhookMessage = input(Fore.GREEN + "Veuillez envoyer le message à spam" + Fore.RED + " →	" )
        num = int(input(Fore.GREEN + "Veuillez envoyer le nombre de message à spam" + Fore.RED + " →	"))
        hook1 = Webhook(webhookURL1)
        for i in range(num): 
            f = i + 1
            e = f  
            hook1 = Webhook(webhookURL1)
            hook1.send(webhookMessage)
            print(f'Message: {webhookMessage} | Nombre d\'envoie(s): {f}/{num}')
            time.sleep(1.5)
            if f == num:
                input(Fore.WHITE + "Spam effectué avec succès ! Veuillez appuyer sur entrée pour retourner dans le menu principal.")
                main()
                
                
    if choice == '3': 
        os.system("title Webhook Renamer")
        webhookURL2 = input(Fore.GREEN + "Veuillez envoyer le lien du webhook à renommer" + Fore.RED + " →	")
        webhookName = input(Fore.GREEN + "Veuillez envoyer le nom du webhook" + Fore.RED + " →	" )
        r = requests.patch(webhookURL2, json={ "name":webhookName })
        input(Fore.WHITE + 'Le webhook a été renommé avec succès ! Veuillez appuyer sur entrée pour retourner dans le menu principal.')
        main()
        
        
                            
                    
               
       
main()    

