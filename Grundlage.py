# 1 
# VSCode Konfiguration für Python
# Python Entwicklungsumgebung bilden: (.venv)
# Auf Suche -> > -> Python: Creating Environment...
# oder:
python -m venv .venv

# dann aktiviere ich die Umgebung:
# Unter Powershell
.venv\Scripts\activate
# Unter Linux
source .venv/bin/activate

# Jetzt installiere ich die Module pygame:
pip install pygame

# Unter Linux:
# Wenn Fehler kommt: 
sudo kill -9 6319
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/dpkg/lock
sudo dpkg --configure -a
sudo apt update
sudo apt install python3.12-venv

# Unter Powershell: 
pip install pygame 
# Fehler
# Manuell die Wheel für pygame installieren
# https://github.com/pygame/pygame/releases
# Hier muss ich prüfen, welche Version von Python ich benutze: 
python --version
# Meine Version ist 3.13
# hier herunterlade ich die Datei: 
# pygame-2.6.1-cp313-cp313-win_amd64.whl
# Dann installiere ich die Module mit dem Verzeichnisse:
pip install C:\Users\xxx\Documents\python_lernen\Mini_Games\pygame-2.6.1-cp313-cp313-win_amd64.whl
# Jetzt überprüfe ich, ob ich die installiert habe:
python -m pygame --version
# oder 
pip show pygame

