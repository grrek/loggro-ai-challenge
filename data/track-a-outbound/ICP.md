# Track A - ICP (Ideal Customer Profile)

Esto es tu input principal. Tu pipeline tiene que **generar ~100 cuentas nuevas** que matcheen este ICP usando las fuentes y herramientas que prefieras.

## El ICP que tenés que cubrir

Loggro vende ERP en la nube. El ICP para esta campaña es:

### Empresa
- **Pais:** Colombia
- **Tamaño:** 50 a 500 empleados
- **Sector:** uno de estos (mix balanceado; no concentres en uno solo):
  - Retail / Comercio minorista
  - Manufactura
  - Hoteleria y alojamiento
  - Gastronomia (cadenas con 5+ puntos)
  - Logistica y distribucion
  - Construccion
  - Servicios profesionales medianos
  - Agroindustria
- **Ingresos estimados:** $500M a $5.000M COP/año (mid-market colombiano)

### Señales de pain o intent
La cuenta es "buen target" si tiene **al menos 2 de estas señales**:
1. Vacante reciente (últimos 6 meses) de Contador, CFO, Analista Financiero, Jefe Administrativo o equivalente
2. Operación multi-sede o multi-bodega que sugiere complejidad contable
3. Tiene un ERP legado conocido (SAP B1 viejo, World Office sin nube, Helisa) o Excel como sistema principal
4. Aparece en prensa por expansion, apertura de nuevas sedes, o crecimiento sustancial
5. Publicación pública del CEO/CFO mencionando "transformación digital", "modernizar contabilidad", "mejor reporteria"
6. Cambio reciente de equipo financiero (CFO nuevo en últimos 12 meses)

### Lo que NO es ICP
- Empresas <50 empleados (muy pequeñas, no rinden TCO)
- Empresas >1000 empleados (van directo a Enterprise / SAP, no Pymes)
- Sectores muy regulados específicos (banca, seguros, salud hospitalaria) — tienen ERP de nicho
- Multinacionales con sede en Colombia pero decisión de ERP fuera

## Lo que debes producir

Una lista de **100 cuentas (target)** que matcheen este ICP. Cada cuenta en el formato de [`accounts_example.json`](./accounts_example.json) (incluido como referencia).

### Schema obligatorio por cuenta

```jsonc
{
  "id": "ACC-NEW-001",
  "name": "...",
  "domain": "...",
  "sector": "...",
  "employees_estimate": 120,
  "city": "...",
  "revenue_band": "small_50_200" | "mid_200_500" | "upper_mid_500_1000",
  "current_erp": "Excel" | "SAP B1" | null,
  "signals": [
    "Senal 1 publica con fuente verificable",
    "Senal 2 publica con fuente verificable"
  ],
  "sources": [
    "https://... (LinkedIn vacante)",
    "https://... (RUES)",
    "https://... (prensa o web propia)"
  ],
  "confidence": "high" | "medium" | "low",
  "icp_match_score": 0.85
}
```

**Diferencia clave con [accounts_example.json](./accounts_example.json):**
- Tu output tiene **`sources` obligatorio** con URLs reales
- `confidence` y `icp_match_score` que decidís vos según tu pipeline
- Las cuentas pueden ser reales (verificables) o cuentas que generes con justificación clara (marcalas como `confidence: low`)

## Fuentes sugeridas (usa las que quieras o inventa)

| Fuente | Para qué sirve | Costo |
|---|---|---|
| **RUES (Registro Único Empresarial)** — `rues.org.co` | Datos básicos de empresa registrada en Colombia (CIIU, tamaño, status) | Gratis (API o scraping) |
| **LinkedIn** — vacantes + perfiles de CFO | Señales de pain (vacante de Contador / CFO) + decision makers | Free tier (cuidado con TOS scraping) |
| **Web propia de la empresa** | "Sobre nosotros", clientes, sedes, prensa | Gratis |
| **Crunchbase / Pitchbook** | Funding, growth signals | Free tier limitado |
| **Apollo.io / Clearbit / Lusha** | Enrichment automático con decision makers | Free trial 50-200 lookups |
| **Google News / Google Search dorks** | Prensa, expansion, nuevos CFO | Gratis |
| **Cámaras de comercio regionales** | Bases de datos sectoriales | Variable |
| **Datos abiertos del gobierno** — `datos.gov.co`, `dnp.gov.co` | Empresas activas por sector | Gratis |

## Reglas duras

1. **No vamos a hacer outreach real** a estas cuentas. Pueden ser empresas reales — pero el reto NO es enviarles correos. Es construir el pipeline que las identifica + enriquece + escribe la secuencia.
2. **Cita TUS fuentes** en cada cuenta. Si no podés citar fuente, marcá `confidence: low` y dí por qué la incluiste igual.
3. **No inventes** datos que se puedan verificar (ingresos exactos, números de empleados específicos). Usa bandas y rangos.
4. **Respeta TOS** de las plataformas. LinkedIn scraping agresivo está prohibido. Phantombuster / Apify con rate limits sensatos o uso humano (manual + paste-into-tool) es legal.

## Cómo te evaluamos en este track

| Dimension | Qué miramos |
|---|---|
| **Calidad del ICP match** | De tus 100 cuentas, ¿qué % realmente cumple el ICP? Si decis que tienes 100 cuentas pero 30 son <50 empleados o de otro pais, baja la nota. |
| **Diversidad sectorial** | ¿Concentraste en un solo sector o tenes mix balanceado? |
| **Fuentes citadas** | ¿Las URLs realmente existen? ¿Las señales son verificables? |
| **Dedupe** | ¿Tu pipeline detecta empresas duplicadas (mismo dominio, mismo NIT)? |
| **Justificación del scoring** | Tu `icp_match_score` y `confidence` deben tener lógica clara, no ser random. |
| **Secuencia outreach** | Email + WhatsApp adaptados al sector y rol del destinatario. No 1 plantilla para todos. |
| **Clasificador de respuestas** | Funciona contra `responses_sample.json` (incluido). |

## Lo que NO tenes que hacer

- Enviar correos reales (NO)
- Pagar herramientas de scraping (gratuitas o trial son suficientes)
- Generar 1000 cuentas (100 con calidad > 500 con basura)
- Cubrir todos los sectores listados (5-6 con buen mix está bien)

## ¿Puedo usar IA para generar las cuentas?

Sí, totalmente. **Pero documentalo en tu AI Audit Log.** Por ejemplo, si usas Claude con web search para encontrar 30 cuentas en el sector hospitalidad, escribilo. Lo medimos como uso de IA bueno (apalancarla para search), no como "inventaste cuentas con LLM".

Si **generaste** cuentas (no encontraste, las inventaste con justificación porque el ICP es muy específico y no hay muchas reales), marcalas con `verified: false` en tu output y explicá tu razonamiento en el README de tu repo.
