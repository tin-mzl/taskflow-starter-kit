# Guide Buildozer (WSL) - Résumé rapide

1. Installer WSL + Ubuntu.
2. sudo apt update && sudo apt install -y python3-pip build-essential git
3. pip install --user buildozer
4. Créer buildozer.spec : `buildozer init`
5. Modifier `requirements = python3,kivy` etc.
6. buildozer android debug deploy run
*Remarque* : ce guide est un résumé ; garder le fichier complet dans l'archive.
