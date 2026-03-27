#!/bin/bash

# Couleurs pour affichage
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}============================================${NC}"
echo -e "${GREEN}      MINI LAB OSINT GRATUIT & PRATIQUE   ${NC}"
echo -e "${BLUE}============================================${NC}"

LAB_DIR=~/MINI_LAB_OSINT
mkdir -p "$LAB_DIR"
cd "$LAB_DIR" || exit

# Création de l'environnement virtuel si absent
if [ ! -d "venv" ]; then
    echo -e "${BLUE}[*] Création de l'environnement virtuel...${NC}"
    python3 -m venv venv
else
    echo -e "${YELLOW}[*] Environnement virtuel déjà présent.${NC}"
fi

# Activation du venv
source venv/bin/activate

echo -e "${BLUE}[*] Mise à jour de pip...${NC}"
pip install --upgrade pip wheel

echo -e "${GREEN}--- Installation outils OSINT gratuits ---${NC}"

pip install \
maigret \
sherlock-project \
holehe \
phoneinfoga \
googlesearch-python \
requests \
beautifulsoup4 \
pandas \
folium \
networkx \
whois

echo -e "${BLUE}============================================${NC}"
echo -e "${GREEN}        INSTALLATION TERMINÉE              ${NC}"
echo -e "${BLUE}============================================${NC}"

echo ""
echo -e "${GREEN}Activer l'environnement :${NC}"
echo "source ~/MINI_LAB_OSINT/venv/bin/activate"

