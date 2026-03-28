import subprocess
import os
import re
from datetime import datetime

OUTPUT_DIR = "EXTRACTED_DATA"
CONTACTS_SUBDIR = os.path.join(OUTPUT_DIR, "CONTACTS")
SMS_SUBDIR = os.path.join(OUTPUT_DIR, "SMS")

MIME_TYPES = {
    "vnd.android.cursor.item/phone_v2": "Telephone",
    "vnd.android.cursor.item/email_v2": "Email",
    "vnd.android.cursor.item/postal-address_v2": "Adresse",
    "vnd.android.cursor.item/note": "Note/Secret",
    "vnd.android.cursor.item/organization": "Organisation/Entreprise",
    "vnd.android.cursor.item/im": "Messagerie Instantanee",
    "vnd.android.cursor.item/contact_event": "Evenement (Anniversaire/Autre)",
    "vnd.android.cursor.item/website": "Site Web",
    "vnd.android.cursor.item/nickname": "Pseudo"
}

CALL_TYPES = {
    "1": "ENTRANT",
    "2": "SORTANT",
    "3": "MANQUE",
    "4": "VOICEMAIL",
    "5": "REJETE",
    "6": "BLOQUE"
}

# Fonction pour executer les commandes ADB
def run_cmd(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

# Creation de l'arborescence des dossiers
def setup():
    for d in [OUTPUT_DIR, CONTACTS_SUBDIR, SMS_SUBDIR]:
        if not os.path.exists(d): 
            os.makedirs(d)
    print(f"Debut de l'extraction")

# Extraction et rangement des contacts par fiche individuelle
def extract_and_sort_contacts():
    print("Tri des contacts")
    uri = "content://com.android.contacts/data"
    cmd = f"adb shell content query --uri {uri}"
    result = run_cmd(cmd)
    
    contacts = {}
    if result.stdout:
        for line in result.stdout.splitlines():
            if "Row:" in line:
                # Parsing des infos nom, valeur et type
                name_match = re.search(r"display_name=([^,]+)", line)
                data1_match = re.search(r"data1=([^,]+)", line)
                mime_match = re.search(r"mimetype=([^,]+)", line)

                if name_match and data1_match and mime_match:
                    name = name_match.group(1).strip()
                    val = data1_match.group(1).strip()
                    label = MIME_TYPES.get(mime_match.group(1).strip(), "Info")
                    
                    if name not in contacts: 
                        contacts[name] = []
                    contacts[name].append(f"{label} : {val}")

        # Ecriture d'un fichier texte par contact
        for name, infos in contacts.items():
            clean_name = "".join(x for x in name if x.isalnum() or x in "._- ").strip()
            with open(os.path.join(CONTACTS_SUBDIR, f"{clean_name}.txt"), "w", encoding="utf-8") as f:
                f.write(f"FICHE : {name}\n" + "="*30 + "\n" + "\n".join(set(infos)))
    print(f"Extraction contacts terminée")

# Extraction et tri des SMS par numero avec horodatage
def extract_and_sort_sms():
    print("Tri des SMS")
    cmd = "adb shell content query --uri content://sms --projection address:body:type:date"
    result = run_cmd(cmd)
    
    sms = {}
    if result.stdout:
        for line in result.stdout.splitlines():
            if "Row:" in line:
                # Recuperation du numero, message, sens et date
                addr_match = re.search(r"address=([^,]+)", line)
                body_match = re.search(r"body=(.*?), (?:date|type)=", line)
                type_match = re.search(r"type=([^,]+)", line)
                date_match = re.search(r"date=([^, ]+)", line)
                
                if addr_match and body_match and date_match:
                    addr = addr_match.group(1).strip()
                    body = body_match.group(1).strip()
                    raw_date = date_match.group(1).strip()
                    
                    # Conversion du timestamp Unix en date lisible
                    try:
                        dt_object = datetime.fromtimestamp(int(raw_date) / 1000.0)
                        readable_date = dt_object.strftime('%d/%m/%Y %H:%M:%S')
                    except:
                        readable_date = "Date inconnue"

                    direction = "RECU" if type_match and type_match.group(1).strip() == "1" else "ENVOYE"
                    
                    if addr not in sms: 
                        sms[addr] = []
                    sms[addr].append(f"[{readable_date}] {direction} : {body}")

        # Creation d'un fichier par conversation
        for addr, msgs in sms.items():
            msgs.sort() 
            clean_addr = addr.replace("+", "plus").replace("/", "_")
            file_path = os.path.join(SMS_SUBDIR, f"conv_{clean_addr}.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"CONVERSATION AVEC : {addr}\n" + "="*45 + "\n\n")
                f.write("\n".join(msgs))
    print(f"Extraction SMS terminée")

# Nouvelle fonction pour l'historique des appels
def extract_call_logs():
    print("Extraction de l'historique des appels")
    uri = "content://call_log/calls"
    # On recupere le numero, le nom, la date, la duree et le type d'appel
    cmd = f"adb shell content query --uri {uri} --projection number:name:date:duration:type"
    result = run_cmd(cmd)
    
    calls_list = []
    if result.stdout:
        for line in result.stdout.splitlines():
            if "Row:" in line:
                num_match = re.search(r"number=([^,]+)", line)
                name_match = re.search(r"name=([^,]+)", line)
                date_match = re.search(r"date=([^,]+)", line)
                dur_match = re.search(r"duration=([^,]+)", line)
                type_match = re.search(r"type=([^,]+)", line)
                
                if num_match and date_match:
                    num = num_match.group(1).strip()
                    name = name_match.group(1).strip() if name_match else "Inconnu"
                    duration = dur_match.group(1).strip() if dur_match else "0"
                    raw_date = date_match.group(1).strip()
                    call_type_id = type_match.group(1).strip() if type_match else "0"
                    
                    try:
                        dt_object = datetime.fromtimestamp(int(raw_date) / 1000.0)
                        readable_date = dt_object.strftime('%d/%m/%Y %H:%M:%S')
                    except:
                        readable_date = "Date inconnue"
                    
                    type_str = CALL_TYPES.get(call_type_id, "AUTRE")
                    calls_list.append(f"[{readable_date}] {type_str} - Num: {num} ({name}) - Duree: {duration}s")

        # Sauvegarde dans un fichier unique trié par date
        calls_list.sort()
        with open(os.path.join(OUTPUT_DIR, "CALL_HISTORY.txt"), "w", encoding="utf-8") as f:
            f.write("HISTORIQUE DES APPELS\n" + "="*50 + "\n\n")
            f.write("\n".join(calls_list))
    print("Extraction appels terminee")

# Recuperation des fichiers multimedia et documents (SDCard)
def pull_files():
    folders = ["/sdcard/DCIM", "/sdcard/Download", "/sdcard/Recordings", "/sdcard/Documents"]
    print(f"Transfert des fichiers")
    for folder in folders:
        dest = os.path.join(OUTPUT_DIR, os.path.basename(folder))
        # Commande adb pull pour copier les dossiers vers l'ordinateur
        subprocess.run(f"adb pull {folder} {dest}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    setup()
    extract_and_sort_contacts()
    extract_and_sort_sms()
    extract_call_logs()
    pull_files()
    print(f"Extraction terminée à 100% !")

if __name__ == "__main__":
    main()