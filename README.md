# Sekstisju-protokollen

Et fiktivt kalibreringsinstitutt behandler 6-7-memet som det lengdemålet det
egentlig er: 6′7″ = 79 tommer × 25,4 mm = **2006,6 mm**. Derfra følger
toleranser, avviksklasser, en obligatorisk håndbevegelse spesifisert til ±13°
ved 2 Hz, et litteraturregister og en masteroppgave.

Statisk nettsted. Seks sider, ingen avhengigheter, ingen byggesteg.

## Sider

| Fil | Dokument | Innhold |
| --- | --- | --- |
| `index.html` | NISK-67/2026 | Protokollen: §1–§5, med målestav, feltmålinger og utførelsesprotokoll |
| `avvik.html` | NISK-67/2026 B | Klassifiseringsskjema A–D og verktøy for selvklassifisering |
| `litteratur.html` | NISK-67/2026 C | Ni arbeider med sammendrag, fagfellemerknader og tilgangsstatus |
| `masteroppgave.html` | MGK-67/2026 | Masteroppgave i gestuell kalibrering, med faseplott |
| `arkiv.html` | ARK-67 | Sorterbart dokumentregister. Ett dokument er unntatt offentlighet |
| `instituttet.html` | NISK-01/2025 | Mandat, seksjoner, bemanning, åpningstider |
| `404.html` | NISK-404 | Avvik i dokumentforvaltningen. Skiller seg fra dokumenter som finnes, men er unntatt offentlighet |

## Hva som er ekte

Nettstedet holder to atskilte henvisningssystemer, slik at det oppdiktede ikke
kan forveksles med det verifiserbare:

- **Hevet tall** peker til *Kildegrunnlag* i protokollens kolofon. Dette er
  faktisk etterprøvbart: Dictionary.com kåret «67» til Word of the Year 2025,
  Skrilla ga ut «Doot Doot (6 7)» i 2024, 6′7″ er en registrert spillerhøyde i
  NBA, og nytellingsmåten (*sekstisju* framfor *syv og seksti*) ble innført i
  Norge i 1951.
- **`[n]` i oransje mono** peker til litteraturregisteret, som i sin helhet er
  oppdiktet og merket som det på hver side.

Tabell 1 er verifiserbar hele veien: 67 er det 19. primtallet, danner et *sexy
primtallspar* med 61 (etablert fagterm), 6 × 7 = 42, 6/7 = 0,857142 med
periodelengde 6, holmium har atomnummer 67 og det høyeste magnetiske momentet
av alle naturlig forekommende grunnstoffer, og 67° N er første hele breddegrad
nord for polarsirkelen.

Instituttet, seksjonene, de ansatte, litteraturen og masteroppgaven finnes
ikke. Tallet gjør det.

## Én fil

`python build-bundle.py` spleiser de seks sidene til én selvstendig fil med
hash-ruter, der `#/litteratur` og kryssenker som `[3]` fortsatt virker:

- `dist/sekstisju-protokollen.html` — frittstående dokument
- `dist/artifact.html` — samme innhold uten doctype og head, for publisering

Flersidesversjonen i rota er kanonisk. Den har ekte URL-er, virker uten
JavaScript, og lar hvert dokument deles for seg — som er hele poenget med et
institutt som nummererer dokumentene sine. Bundelen genereres fra samme kilde,
så de to kan ikke gli fra hverandre.

## Teknisk

- **Én delt `assets/base.css`** med tokens, komponenter og fonter. Lastes én
  gang og gjenbrukes på alle seks sidene.
- **Fontene er inlinet** som base64 woff2: fire variabel-faces over
  latin-subsettet, deklarert over sine reelle wght-akser (Bricolage Grotesque
  200–800, Petrona 100–900, Spline Sans Mono 300–700). Ingen eksterne kall;
  typografien er ikke nettverksavhengig.
- **Figurene er håndtegnet SVG** som arver farger fra temavariablene. Fig. 4 er
  et faseplott generert fra `sin(2π·2t)`.
- **Fullt lys/mørkt tema** via `prefers-color-scheme` og `data-theme`.
- **Ingen rammeverk.** To små vanilla-skript: sortering av arkivtabellen og
  selvklassifiseringen.
- **Utskriftsstil** i `@media print`: navigasjon og lenkekort skjules, figurer
  og tabeller brytes ikke over sider, animasjonen fryses, 18 mm marg.
- **Favicon** er en inline SVG i data-URI, samme merke som instituttets segl.
- Skriv `67` hvor som helst på nettstedet. Instituttet registrerer ytringen.
- Håndbevegelsen i Fig. 3 respekterer `prefers-reduced-motion` og fryses da i
  motsatt utslag, slik at stillbildet fortsatt viser gesten.

### Om motfase

Håndleddsaksene står speilvendt om midtlinjen. En rotasjon med *samme* fortegn
i begge håndledd gir derfor *motsatt* vertikalt utslag ved fingertuppene:
leddvinklene er i fase, utslagene i motfase. Animasjonen i Fig. 3 og kurvene i
Fig. 4 bygger på dette, og masteroppgavens kapittel 5 handler om nettopp den
forvekslingen.

## Kjør lokalt

```
python -m http.server 8067
```

Sidene må serveres over HTTP, ikke åpnes direkte fra disk — `assets/base.css`
er en relativ referanse. `.claude/launch.json` starter det samme på port 8067.

## Deploy

Statisk side på Vercel. Framework preset **Other**, ingen build command,
output directory er repo-rota. Hver push til `main` auto-deployer.

## Måleusikkerhet

±0.
