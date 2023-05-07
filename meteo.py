from bluepy.btle import Scanner
import logging

# Configuration du fichier log
logging.basicConfig(
    filename="log.txt", # nom du fichier
    encoding="utf-8", # type d'encodage
    level=logging.DEBUG, # Information détaillée, intéressante seulement lorsqu'on diagnostique un problème
    format="%(asctime)s %(message)s",
)
logging.info(G)

# Création d'un objet scanner
scanner = Scanner()

# Affichage d'un message de début de scan
print("Début du scan, c'est parti !")

# Boucle infinie pour scanner les périphériques en continu
while True:
    
    # Lancement du scan pendant une durée de 3 secondes
    devices = scanner.scan(timeout=3.0)
    
    # Parcours de la liste des périphériques détectés
    for device in devices:
        
        # Liste des adresses MAC des périphériques à rechercher
        mac_adresses = 'd6:1c:bf:b7:76:62', 'd6:c6:c7:39:a2:e8', 'd7:ef:13:27:15:29'
        
        # Si l'adresse MAC du périphérique courant fait partie de la liste recherchée
        if device.addr in mac_adresses:
            
            # Affichage des informations du périphérique détecté : adresse MAC et puissance du signal
            print(
                f"Appareil trouvé ! Adresse MAC : {device.addr}, "
                f"Puissance du signal : {device.rssi} dB"
            )
            
            # Affichage des données des profils génériques
            for adtype, description, value in device.getScanData():
                
                # Affichage du numéro de profil générique, de la description et de la valeur
                print(f"Numéro de profil générique : ({adtype}), Description : {description} = {value}")
                
                # Isole la ligne où la trame apparaît
                if adtype == 22:
                    
                    # Extraction des données de la batterie, de la température et de l'humidité
                    batterie = int(value[20:22], 16)
                    temperature = int(value[24:28], 16) * 10 ** -2 # 10 ** -2 pour convertir en degrés Celsius.
                    humidite = int(value[28:32], 16) * 10 ** -2
                                    
                    # Affichage des données extraites
                    print(f"La batterie est à un niveau de {batterie}%")
                    print(f"La température est de {temperature}°C")
                    print(f"L'humidité est de {humidite}%")
                    
            # Affichage d'une ligne vide pour séparer les résultats des différents périphériques détectés
            print()