# Posts de marca pròpia (nov 2026 – feb 2027)

- `content.py` — títols, textos de slide, captions i hashtags (català) dels 27 carrusels.
- `render.py` — plantilla HTML (Open Sans, 1080×1350) → PNG amb Playwright. Retalla els packshots al seu contorn (`cut/`).
- `posts.json` — per a cada post: URL públiques dels slides, `due_at` en UTC, caption i hashtags.
- `publish_buffer.py` — crea els posts programats a Buffer via GraphQL (`--send`; per defecte dry-run).
- Imatges d'origen: `GenerazionePack_…` (packshots Unifarco amb la marca Farmàcia del Diamant).

Regles de contingut: només al·legacions de salut autoritzades (Reg. 1924/2006); "Producte sanitari. Llegiu detingudament les instruccions d'ús" quan n'hi ha; mai "cura/tracta/ferida/associació"; sense preus ni descomptes.
