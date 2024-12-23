import os
import platform
import time
import random
import threading
from colorama import init, Fore, Style

# Initialisation de colorama pour les couleurs
init()

# Fonction pour afficher un effet Matrix continu
def matrix_effect(stop_event, width=80):
    chars = "01"
    while not stop_event.is_set():
        # Génère une ligne aléatoire de 0 et 1
        line = "".join(random.choice(chars) for _ in range(width))
        print(Fore.GREEN + line + Style.RESET_ALL)
        time.sleep(0.05)
    print(Style.RESET_ALL, end="")  # Réinitialise les couleurs

# Fonction pour effectuer un ping
def ping(address, packets=4):
    system = platform.system().lower()
    param = "-n" if system == "windows" else "-c"
    cmd = f"ping {param} {packets} {address}"

    print(Fore.GREEN + f"\n--- Starting Ping 🕵️ {address} ({packets} paquets) ---\n" + Style.RESET_ALL)
    time.sleep(1)

    try:
        # Exécute la commande ping et capture le résultat
        process = os.popen(cmd)
        for line in process:
            print(Fore.YELLOW + line.strip() + Style.RESET_ALL)
            time.sleep(0.2)  # Simule un affichage progressif des résultats
    except Exception as e:
        print(Fore.RED + f"Error Ping 💻🌍🔌 : {e}" + Style.RESET_ALL)

# Fonction principale
def main():
    # Message de bienvenue
    print(Fore.GREEN + Style.BRIGHT + "CyberPing 💻\n" + Style.RESET_ALL)
    time.sleep(1)

    # Demande d'une adresse IP ou un site web
    address = input(Fore.GREEN + "Enter an IP address or Website 🌍 : " + Style.RESET_ALL).strip()
    if not address:
        print(Fore.RED + "Erreur : Invalid address! End of the Program 🌍🔌" + Style.RESET_ALL)
        return

    # Demande du nombre de paquets
    try:
        packets = int(input(Fore.GREEN + "Enter the number of packets to send (default 4) 📦️ : " + Style.RESET_ALL).strip() or 4)
        if packets <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Erreur : Invalid packet count. Using the default value (4) 🔌📦️ : " + Style.RESET_ALL)
        packets = 4

    # Création d'un événement pour arrêter l'effet Matrix
    stop_event = threading.Event()

    # Lancement de l'effet Matrix dans un thread séparé
    matrix_thread = threading.Thread(target=matrix_effect, args=(stop_event,))
    matrix_thread.start()

    try:
        # Lancement du ping
        ping(address, packets)
    except KeyboardInterrupt:
        print(Fore.RED + "\nUser Interruption. End of the program 🔌💻️ " + Style.RESET_ALL)
    finally:
        # Arrêt de l'effet Matrix
        stop_event.set()
        matrix_thread.join()

    # Message de fin
    print(Fore.GREEN + "\nProgram Completed. Thank you for using cyberping created by https://linktr.ee/Brandon008 💻️👍️ " + Style.RESET_ALL)

# Lancer le script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nUser Interruption. End of the program 🔌💻️ " + Style.RESET_ALL)
