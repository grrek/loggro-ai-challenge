# schemas/

JSON Schema (draft 2020-12) de los objetos que tu pipeline lee o escribe.

| Archivo | Para que track | Que valida |
|---|---|---|
| `hubspot_mock.json` | A, B, C, D | Subset minimo de HubSpot (Contact, Deal, Campaign, ConversationIntel). Tu pipeline lee/escribe instancias conformes |
| `insights_schema.json` | D | Output de cada llamada (`insights.json`). Es el schema fijo del Track D |

## Como validar

```python
from jsonschema import Draft202012Validator
import json

schema = json.load(open("schemas/insights_schema.json"))
instance = json.load(open("data/track-d-intel/audio/demo_A_contadora.insights.json"))

validator = Draft202012Validator(schema)
errors = list(validator.iter_errors(instance))
if errors:
    for e in errors:
        print(e.message)
else:
    print("Valid")
```

## Convenciones

- IDs:
  - Contact: `CONT-NNNNNN` (6 digitos)
  - Deal: `DEAL-NNNNNN`
  - Campaign: `CAMP-NNN`
- Moneda: siempre COP, sin decimales (entero) en campos `*_cop`
- Fechas: ISO 8601 (`YYYY-MM-DD` para date, `YYYY-MM-DDTHH:MM:SSZ` para datetime)
- Sin em-dashes en strings libres
- Espanol Colombia para texto libre

## Cuando agregar campos

Si tu pipeline necesita campos adicionales que el schema no contempla:

- **Opcion 1 (preferida):** abre un issue en el repo template explicando el caso de uso
- **Opcion 2:** extiende el schema en una copia local, documentalo en ADR, y mencionalo en tu README

NO modifiques estos schemas directamente sin discutirlo. Son contrato compartido entre tu pipeline y el eval automatico que corremos.
