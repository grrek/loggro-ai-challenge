# Dataset Track A (Outbound Automation): Reto VE-1770

Este dataset alimenta el Track A del reto tecnico de Loggro para la vacante VE-1770 (Analista de Automatizacion & RevOps). El candidato debe construir un sistema de outbound (scraping, enriquecimiento, secuencia email + WhatsApp, clasificacion de respuestas) que pueda procesar estos archivos como entrada.

## Archivos

| Archivo | Que contiene | Filas |
|---|---|---|
| `accounts.json` | 30 cuentas (empresas mid-market colombianas) candidatas a ser prospectadas por Loggro | 30 |
| `responses_sample.json` | 10 respuestas sinteticas a un outreach (email y WhatsApp) con groundtruth para evaluar el clasificador del candidato | 10 |
| `README.md` | Este archivo | 1 |

## Reglas de uso

1. **No contactar las empresas reales** del dataset. Hay companias verificables (Crystal, Haceb, Conconcreto, Frisby, etc.) listadas con `verified: true`. Son referencia, no objetivo comercial real.
2. **No incluir datos sensibles** en los outputs del reto (telefonos reales, ingresos exactos, nombres de personas que no sean ficcion). Si necesitas mostrar contactos en tu demo, usa los nombres de `responses_sample.json` (todos ficticios).
3. Este dataset es de **uso unico para el reto**. No redistribuir.

## Schema (`accounts.json`)

| Campo | Tipo | Notas |
|---|---|---|
| `id` | string | Formato `ACC-NNN` (001 a 030) |
| `name` | string | Razon social o nombre comercial |
| `domain` | string | Dominio web (mayoria `.com.co`) |
| `sector` | string | Uno de: retail, manufactura, agropecuario, hoteleria, salud, logistica, construccion, servicios_profesionales, gastronomia, distribucion |
| `employees_estimate` | int | 50 a 500 |
| `city` | string | Ciudad principal de operacion |
| `revenue_band` | string | `small_50_200`, `mid_200_500`, `upper_mid_500_1000` (COP MM anuales, banda referencial) |
| `current_erp` | string or null | ERP/contable actual conocido o `null` si no se sabe |
| `signals` | array of string | 2 a 4 observaciones publicas plausibles (vacantes, expansion, prensa) |
| `verified` | bool | `true` si la empresa es real y verificable publicamente; `false` si es sintetica plausible |

### Mix por sector

| Sector | Cantidad |
|---|---|
| retail | 5 |
| manufactura | 4 |
| agropecuario | 3 |
| hoteleria | 3 |
| salud | 3 |
| logistica | 3 |
| construccion | 3 |
| servicios_profesionales | 3 |
| gastronomia | 2 |
| distribucion | 1 |

### Ejemplo (1 row)

```json
{
  "id": "ACC-005",
  "name": "Moda Express Cali",
  "domain": "modaexpress.com.co",
  "sector": "retail",
  "employees_estimate": 160,
  "city": "Cali",
  "revenue_band": "small_50_200",
  "current_erp": "Excel",
  "signals": [
    "Cadena de moda femenina con 12 tiendas en Valle del Cauca",
    "Vacante publica de Jefe de Contabilidad (ago 2025)",
    "Operacion aun apoyada en hojas de calculo segun perfil del CFO"
  ],
  "verified": false
}
```

## Schema (`responses_sample.json`)

| Campo | Tipo | Notas |
|---|---|---|
| `id` | string | Formato `RESP-NNN` (001 a 010) |
| `channel` | string | `email` o `whatsapp` |
| `account_id` | string | FK hacia `accounts.json` (campo `id`) |
| `from` | string | Nombre + cargo de quien responde (todos ficticios) |
| `received_at` | string | ISO 8601 con timezone `-05:00` (Colombia) |
| `subject` | string or null | Solo para `channel = email`; `null` en WhatsApp |
| `body` | string | Texto de la respuesta, espanol Colombia natural |
| `groundtruth_intent` | string | Uno de: `interesado`, `objecion`, `fuera_de_scope`, `pedir_reunion` |
| `confidence` | string | `high`, `medium`, `low`. Los `low` son ambiguos a proposito (estresan al clasificador) |

### Distribucion de intents

| Intent | Cantidad |
|---|---|
| interesado | 3 |
| objecion | 3 |
| fuera_de_scope | 2 |
| pedir_reunion | 2 |

### Distribucion de confidence

| Confidence | Cantidad |
|---|---|
| high | 6 |
| medium | 2 |
| low | 2 |

### Ejemplo (1 row)

```json
{
  "id": "RESP-002",
  "channel": "email",
  "account_id": "ACC-021",
  "from": "Felipe Restrepo (Gerente Administrativo y Financiero)",
  "received_at": "2026-03-21T10:05:00-05:00",
  "subject": "Re: Loggro para operadores logisticos",
  "body": "Gregorio, buen dia. Si nos interesa explorar. Ya venimos evaluando moverNos de Excel hacia un ERP integrado y Loggro esta en la lista corta junto con World Office...",
  "groundtruth_intent": "interesado",
  "confidence": "high"
}
```

## Como cruzar `responses` con `accounts`

El campo `account_id` en `responses_sample.json` es la FK hacia el campo `id` en `accounts.json`. Ejemplo en Python:

```python
import json

with open("accounts.json") as f:
    accounts = {a["id"]: a for a in json.load(f)}

with open("responses_sample.json") as f:
    responses = json.load(f)

for r in responses:
    acct = accounts[r["account_id"]]
    print(f"{r['id']} ({r['channel']}) -> {acct['name']} [{acct['sector']}, {acct['city']}]")
```

Esto permite al candidato:
- Enriquecer la respuesta con sector, tamano, ciudad y senales de la cuenta antes de clasificar
- Demostrar manejo de joins basicos en su pipeline (HubSpot, n8n, script propio, lo que use)
- Medir si el clasificador mejora cuando recibe contexto de la cuenta vs solo el body de la respuesta

## Notas sobre `verified`

- `verified: true` (10 cuentas): empresas reales colombianas conocidas publicamente. Los `signals` son plausibles y consistentes con lo que se publica de ellas, pero NO se afirman hechos especificos no verificables (fechas exactas de vacantes, montos de inversion).
- `verified: false` (20 cuentas): nombres y dominios construidos para verse plausibles. NO existen como empresas reales con esos datos exactos. Sirven para llenar el funnel sin riesgo de difamacion ni de outreach accidental.

Si el candidato cita empresas `verified: true` en su demo, debe hacerlo como ejemplos hipoteticos, no como leads reales.
