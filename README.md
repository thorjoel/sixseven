# Sekstisju-protokollen

Kalibreringssertifikat for tallet 67. Én statisk HTML-fil, ingen avhengigheter,
ingen byggesteg.

Dokumentet behandler 6-7-memet som det lengdemålet det egentlig er:
6′7″ = 79 tommer × 25,4 mm = **2006,6 mm**. Derfra følger toleranser,
avviksklasser og en obligatorisk håndbevegelse spesifisert til ±13° ved 2 Hz.

## Innhold

| Klausul | Emne |
| --- | --- |
| §1 | Opphav og omløp — kildekritisk gjennomgang |
| §2 | Nummerisk revisjon — verifiserte egenskaper ved 67 |
| §3 | Feltmålinger — ytringsfrekvens etter klassetrinn |
| §4 | Utførelsesprotokoll — håndbevegelsen som teknisk tegning |
| §5 | Avviksklasser A–D |
| §6 | Konklusjon |

Tallene i Fig. 2 er merket som illustrasjonsdata. Alt i Tabell 1 er
verifiserbart: 67 er det 19. primtallet, danner et *sexy primtallspar* med 61,
er atomnummeret til holmium — grunnstoffet med det høyeste magnetiske momentet
av alle naturlig forekommende — og 67° N er første hele breddegrad nord for
polarsirkelen.

Instituttet i dokumentet finnes ikke. Tallet gjør det.

## Kjør lokalt

Åpne `index.html` direkte i en nettleser. Ingen server nødvendig.

## Deploy

Statisk side på Vercel. Framework preset **Other**, ingen build command,
output directory er repo-rota.

## Teknisk

- Én fil, ~700 linjer HTML/CSS/SVG. Ingen JavaScript.
- Figurene er håndtegnet SVG som arver fargene fra temavariablene.
- Fullt lys/mørkt tema via `prefers-color-scheme` og `data-theme`.
- Håndbevegelsen i Fig. 3 respekterer `prefers-reduced-motion` og fryses da
  i motsatt utslag, slik at stillbildet fortsatt viser gesten.
- Typografi: Bricolage Grotesque, Petrona og Spline Sans Mono, inlinet som
  base64 woff2 direkte i fila. Ingen eksterne kall — sida er selvstendig.
  Fire variabel-faces over latin-subsettet, deklarert over sine reelle
  wght-akser (200-800, 100-900, 300-700).

## Måleusikkerhet

±0.
