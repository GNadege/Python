import socket

domain = input("Domaine : ")

try :
	ip = socket.gethostbyname(domain)
	print(f"[+] Domaine : {domain}")
	print(f"[+] Adresse IP : {ip}")

except:
	print("Erreur")
