# Sandra Italia — Netlify Edition

**Autore, ideazione e direzione editoriale:** Salvatore Sinatra.

## Fotografia principale
- Fonte / scheda di provenienza: https://commons.wikimedia.org/wiki/File:Sandra_Cretu.jpg
- Autore fotografico: Tim Lehmann
- Risoluzione dell'originale: 769×1024 px
- Licenza: CC BY-SA 2.0
- Originale disponibile presso Wikimedia Commons; collegamento esterno nel markup HTML.
- Non attribuire la fotografia a Salvatore Sinatra. Non rimuovere l'attribuzione, il link di licenza o l'indicazione dell'autore. La presentazione via CSS adatta soltanto la finestra visiva e non genera file derivati.

## Fonti primarie
- https://sandra-music.com/
- https://sandra-music.com/discography/

## Architettura
- Branch Netlify: `netlify-light`
- Pubblicazione: `netlify/`
- `netlify/index.html`: documento, fotografia, icone SVG inline per link esterni, metadati e sezioni legali
- `netlify/assets/style.css`: layout e mobile
- `netlify/assets/app.js`: filtri di catalogo
- `netlify.toml`: directory di output statica

## Informativa editoriale
Questo è un archivio non ufficiale e indipendente. I marchi, le immagini, le opere e le pubblicazioni discografiche appartengono ai rispettivi titolari. Le fonti esterne restano sotto il controllo dei rispettivi gestori. Non dichiarare approvazioni o affiliazioni non esistenti.

## Pubblicazione
Per avviare il primo deploy Netlify con continuous deployment, associare il repository a Netlify scegliendo il branch di produzione `netlify-light`, directory `netlify`, senza comando di build. I file inseriti nel repository non equivalgono alla conferma di deploy; verificare l'identificativo e lo stato `ready` del deploy effettivo.
