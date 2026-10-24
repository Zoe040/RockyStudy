# RockyStudy (PWA)

Karteikarten-App fürs Studium mit Lernplan (FSRS), Kursen mit Unterstapeln, Lückentext, Hörmodus und Probeklausur. Läuft offline, installierbar auf dem iPhone.

**Hier liegen keine Karteikarten.** Karten werden nur auf dem Gerät angelegt oder importiert (IndexedDB) und per Backup-Datei gesichert.

## Dateien

- `index.html` – die App (installierbare Version mit Manifest und Service Worker)
- `app.html` – dieselbe App ohne PWA-Kopf, Quelle für den Claude-Prototyp
- `manifest.webmanifest` – Name, Farben, Icons
- `sw.js` – Offline-Cache
- `vendor/ts-fsrs.umd.js` – Lernplan-Bibliothek ts-fsrs 5.2.3 (MIT, siehe `vendor/LICENSE-ts-fsrs.txt`)
- `icons/` – App-Icons (Waschbär Rocky, eigene Zeichnung)
- `build.py` – baut `index.html` aus `app.html` und zählt die Cache-Version hoch

## Online stellen (GitHub Pages)

1. Alle Dateien ins Repo laden.
2. Repo → Settings → Pages → Branch `main`, Ordner `/ (root)` → Save.
3. Nach ca. 1 Minute: `https://<nutzername>.github.io/<repo>/`

## Installieren

iPhone: Link in Safari öffnen → Teilen → „Zum Home-Bildschirm“. Danach nur noch über das Icon öffnen: Die Home-Bildschirm-App hat ihren eigenen Speicher, getrennt von Safari.

## Spracheingabe

Nutzt die Web Speech API (Siri/Diktat muss an sein). In Web-Apps auf dem Home-Bildschirm blockiert iOS sie bisher meist. Die App merkt das, blendet das Mikrofon aus und liest weiter vor. Unter Einstellungen → Spracheingabe → „Erneut testen“ lässt sie sich wieder einschalten.
