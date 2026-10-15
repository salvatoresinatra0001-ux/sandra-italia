# Sandra · Italia

Archivio italiano indipendente dedicato alla voce di Sandra. Sito statico in italiano, senza dipendenze, senza build step.
Cura editoriale: **Salvatore Sinatra**. Stato dei dati: **16 ottobre 2026**.

> Progetto editoriale indipendente, non affiliato all'artista, al management o alle etichette.

## Pubblicazione

Sito statico servito da GitHub Pages dal branch `main`, cartella radice.
Indirizzo: `https://salvatoresinatra0001-ux.github.io/sandra-italia/`

Per un dominio personalizzato (`sandra-italia.it`): aggiungere un file `CNAME` con il dominio
e puntare il DNS a GitHub Pages. Non è stato aggiunto perché il DNS non è configurato.

## Struttura

- `index.html` — Home
- `biografia.html` — Biografia
- `discografia.html` — Discografia
- `ascolta.html` — Ascolta
- `concerti.html` — Concerti
- `media.html` — Media
- `fonti.html` — Fonti e metodo
- `crediti-foto.html` — Crediti foto

Asset: `assets/css/style.css`, `assets/js/site.js`, `assets/img/favicon.svg`.
`.nojekyll` disattiva l'elaborazione Jekyll; `robots.txt` e `sitemap.xml` sono inclusi.

## Metodo editoriale

Tre livelli di solidità su ogni dato:

| Livello | Significato |
|---|---|
| **Solido** | Almeno due fonti indipendenti, o fonti primarie coerenti (sito ufficiale, etichetta, distributore) |
| **Una fonte** | Un solo riscontro; pubblicato ma non presentato come definitivo |
| **Incerto** | Fonti in conflitto o dato dedotto; le date si pubblicano solo come mese e anno |

Le diverse edizioni linguistiche della stessa enciclopedia contano come **una sola fonte**.
I metadati dei negozi digitali non sono fonte per le etichette.
La precisione della data (giorno / mese / anno) è un campo distinto dalla solidità.

## Immagini

Nessuna fotografia dell'artista è inclusa in questa versione: gli archivi a licenza libera non
erano raggiungibili in fase di compilazione. Gli spazi sono predisposti e dichiarati in
`crediti-foto.html`, che contiene anche le regole di inserimento e il formato della didascalia.
Copertine, foto stampa e fotogrammi di videoclip non sono immagini libere.

## Controlli ancora aperti

- **Date di Mirrors e Paintings in Yellow** — Risolvere il conflitto interno alla fonte su Discogs e sulle edizioni originali Virgin.
- **Ingresso negli Arabesque** — Stabilire se agosto 1978 o 1979; le due edizioni dell'enciclopedia divergono.
- **Calendario dal vivo** — Riconfermare ogni data su canale ufficiale o sito della venue; gli anni delle date passate sono dedotti.
- **Date italiane** — Scorrere lo storico completo delle scalette, non solo le voci in evidenza.
- **Canali ufficiali** — Individuare e verificare sito e profili ufficiali attivi; finché non sono verificati non vengono linkati.
- **Immagini** — Verificare file per file autore, licenza e risoluzione su archivi liberi prima di qualunque pubblicazione fotografica.
- **Profilo Apple Music** — Riconfermare l'identificativo 1697889245: i brani corrispondono, l'elenco degli album no.

## Modifiche

I contenuti sono scritti direttamente nell'HTML: per aggiornare un dato si modifica la riga
della tabella e, se cambia il livello di verifica, il relativo indicatore di solidità
(`<span class="sol s-solid|s-one|s-weak">`).

<!-- GitHub Pages: richiesta nuova pubblicazione dal branch main, 2026-10-16. -->
