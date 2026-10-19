# Pubblicazione — sandra-italia

## GitHub Pages
- Repository: `salvatoresinatra0001-ux/sandra-italia`
- Branch: `main`.
- Edizione completa: https://salvatoresinatra0001-ux.github.io/sandra-italia/
- Edizione Light indipendente: https://salvatoresinatra0001-ux.github.io/sandra-italia/light/
- La Light Edition vive in `main/light/index.html` e non sostituisce la home completa.

## Netlify — edizione editoriale
- Progetto Netlify: https://app.netlify.com/projects/sandra-music-italia
- Repository da collegare: `salvatoresinatra0001-ux/sandra-italia`
- Branch produzione: `netlify-light`
- Directory pubblicazione: `netlify` (impostata anche nel file `netlify.toml` alla radice di questo branch)
- Comando build: nessuno; sito HTML/CSS/JS statico.
- Homepage Netlify: `netlify/index.html`, CSS `netlify/assets/style.css`, JS `netlify/assets/app.js`.
- Dominio personalizzato previsto e già visibile nella scheda Netlify: `sandra-music-italia.it`.
- HTTPS/DNS non verificati da questo documento; non considerare il sito pubblicato finché il deploy è `ready` e il dominio risolve.

## DNS esterni / Keliweb
Prima di modificare i nameserver, esportare o annotare tutti i record esistenti. Preservare MX, SPF, DKIM, DMARC, sottodomini e servizi di terze parti. La delega NS va confermata con gli esatti valori assegnati da Netlify, che non sono universali. Non cambiare la configurazione GitHub Pages quando si modifica il DNS destinato al progetto Netlify.

## Checklist collaudo
- [ ] GitHub Pages Light HTTP 200 e rendering responsive
- [ ] Netlify collegato al branch `netlify-light` e primo deploy `ready`
- [ ] Verifica CSS/JS, ricerca album e filtri
- [ ] Canonical, robots.txt, sitemap.xml
- [ ] Controllo record NS/A/CNAME e mail Keliweb
- [ ] HTTPS e redirect canonici sul dominio personalizzato
- [ ] Verifica collegamenti ufficiali e pagine 404
