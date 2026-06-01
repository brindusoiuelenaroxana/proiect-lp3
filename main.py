"""
Nume Proiect: D3-T1 | Redenumirea fișierelor care respectă un șablon dat
Echipa: 21-E6 | Studenți: BRÎNDUŞOIU ELENA-ROXANA, TOADER DENISA
"""
import os
import shutil

# Categorii de fișiere
categorii = {"Documente": [".pdf", ".docx", ".txt"],"Imagini": [".jpg", ".png", ".jpeg"],
             "Video": [".mp4", ".mkv"],"Arhive": [".zip", ".rar"]}

# Limită pentru fișiere mari (100 MB)
limita_mare = 100 * 1024 * 1024

# Folderul Downloads din proiect
cale_director = "Downloads"

# Creează folderul dacă nu există
os.makedirs(cale_director, exist_ok=True)

print("Începere organizare")

# Deschide fișierul jurnal
with open("log.txt", "w", encoding="utf-8") as log:

    # Parcurge toate fișierele
    for fisier in os.listdir(cale_director):

        cale_veche = os.path.join(cale_director, fisier)

        # Ignoră folderele
        if os.path.isdir(cale_veche):
            continue

        # Obține dimensiunea și extensia
        dimensiune = os.path.getsize(cale_veche)
        _, extensie = os.path.splitext(fisier)

        categorie_noua = "Altele"

        # Verifică dacă fișierul este mare
        if dimensiune > limita_mare:
            categorie_noua = "Mari"

        else:
            # Caută categoria după extensie
            for categorie, extensii in categorii.items():

                if extensie.lower() in extensii:
                    categorie_noua = categorie
                    break

        # Creează subfolderul categoriei
        cale_subdirector = os.path.join(cale_director, categorie_noua)
        os.makedirs(cale_subdirector, exist_ok=True)

        # Noua locație a fișierului
        cale_noua = os.path.join(cale_subdirector, fisier)

        # Mută fișierul
        shutil.move(cale_veche, cale_noua)

        # Scrie în log
        log.write(f"{cale_veche} -> {cale_noua}\n")

        print(f"Mutat: {fisier} -> {categorie_noua}")

print("Organizare finalizată")