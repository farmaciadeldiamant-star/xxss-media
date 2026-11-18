# Posts de marca pròpia (nov 2026 – feb 2027)

- `content.py` — títols, textos de slide, captions i hashtags (català) dels 27 carrusels.
- `render.py` — plantilla HTML (Open Sans, 1080×1350) → PNG amb Playwright. Retalla els packshots al seu contorn (`cut/`).
- `posts.json` — per a cada post: URL públiques dels slides, `due_at` en UTC, caption i hashtags.
- `publish_buffer.py` — crea els posts programats a Buffer via GraphQL (`--send`; per defecte dry-run).
- Imatges d'origen: `GenerazionePack_…` (packshots Unifarco amb la marca Farmàcia del Diamant).

Regles de contingut: només al·legacions de salut autoritzades (Reg. 1924/2006); "Producte sanitari. Llegiu detingudament les instruccions d'ús" quan n'hi ha; mai "cura/tracta/ferida/associació"; sense preus ni descomptes.

## Publicar a Buffer (des del pipeline xxss-farmacia)

```bash
export BUFFER_API_KEY=...            # ja la té el pipeline
python3 publish_buffer.py --status                 # què hi ha programat al canal d'Instagram
python3 publish_buffer.py                          # dry-run (no envia res)
python3 publish_buffer.py --send                   # pla de pagament: programa els 38 d'un cop
python3 publish_buffer.py --send --max-queue 10    # pla Free: omple la cua fins a 10 i deixa la resta per a demà (posar-ho al cron diari)
```

Límits de l'API (pla Free): 150 peticions/15 min, 100/24 h, 3.000/30 dies. L'script fa ~2 peticions per post i espera 2 s entre mutacions; amb `--max-queue` només crea els que caben.
Els posts que no caben no es perden: en execucions següents es creen i, si la seva data ja ha passat, es mouen al següent dia lliure a la mateixa hora.
