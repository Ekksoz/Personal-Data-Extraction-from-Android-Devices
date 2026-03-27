#!/bin/bash

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}=================================================${NC}"
echo -e "${GREEN}      LAB OSINT & PROFILAGE (Extraction Mobile) ${NC}"
echo -e "${BLUE}=================================================${NC}"

LAB_DIR=~/LAB_OSINT

mkdir -p "$LAB_DIR"
cd "$LAB_DIR" || exit

# Création environnement Python seulement si absent
if [ ! -d "venv" ]; then
    echo -e "${BLUE}[*] Création de l'environnement virtuel...${NC}"
    python3 -m venv venv
else
    echo -e "${YELLOW}[*] Environnement virtuel déjà présent.${NC}"
fi

source venv/bin/activate

echo -e "${BLUE}[*] Mise à jour de pip...${NC}"
pip install --upgrade pip wheel

echo -e "${GREEN}--- Installation outils OSINT ---${NC}"

pip install \
maigret \
sherlock-project \
holehe \
phonenumbers \
googlesearch-python \
requests \
beautifulsoup4 \
lxml

echo -e "${GREEN}--- Installation outils Profilage / Analyse ---${NC}"

pip install \
pandas \
sqlitedict \
Pillow \
exifread \
hachoir \
geopy \
folium \
spacy \
networkx \
matplotlib \
python-dateutil

echo -e "${GREEN}--- Outils interface / reporting ---${NC}"

pip install \
rich \
tqdm \
python-dotenv \
tabulate

echo -e "${BLUE}[*] Installation modèle NLP français (spaCy)...${NC}"
python3 -m spacy download fr_core_news_sm

echo -e "${BLUE}=================================================${NC}"
echo -e "${GREEN}           INSTALLATION TERMINÉE ${NC}"
echo -e "${BLUE}=================================================${NC}"

echo ""
echo -e "${GREEN}Activer l'environnement :${NC}"
echo "source ~/LAB_OSINT/venv/bin/activate"

echo ""
echo -e "${GREEN}Exemples OSINT :${NC}"
echo "maigret username"
echo "sherlock username"
echo "holehe email@gmail.com"

echo ""
echo -e "${GREEN}Profilage données :${NC}"
echo "- pandas/sqlite3 : analyse SMS / contacts"
echo "- exifread : extraction GPS photos"
echo "- folium : génération cartes HTML"
echo "- spacy : extraction noms/lieux dans messages"
echo "- networkx : graphes relations sociales"

echo ""
echo -e "${YELLOW}LAB installé dans : $LAB_DIR${NC}"