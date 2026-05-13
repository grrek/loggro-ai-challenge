# Backlog antes de lanzar el reto al primer candidato

Lo que falta para que el repo template este 100% listo. Auditado 2026-05-13, simplificado tras eliminacion del eval automatizado.

## 🔴 Bloqueantes (sin esto, un candidato real no puede arrancar)

### Datasets sinteticos incompletos

| Track | Archivo | Estado | Meta | Falta |
|-------|---------|--------|------|-------|
| A | `data/track-a-outbound/ICP.md` | ✅ **CERRADO** | ICP escrito con criterios + senales + fuentes | — |
| A | `data/track-a-outbound/accounts_example.json` | ✅ **CERRADO** | 30 cuentas de referencia formato canonico | — |
| A | `data/track-a-outbound/responses_sample.json` | ✅ **CERRADO** | 10 respuestas con ground_truth | — |
| B | `data/track-b-insights/campaigns.json` | ✅ **CERRADO** | 124 campanas reales Q1-Q2 2026 + 3 anomalias plantadas | — |
| C | `data/track-c-pieces/briefs.json` | 1 entrada placeholder | 3 briefs (DIAN, cross-sell POS, retencion Nomina) | **2 briefs mas** |
| C | `data/track-c-pieces/good_pieces.json` | 1 entrada placeholder | 10 piezas referencia que pasan brand voice (extraer de Meta Ad Library Loggro) | **9 piezas mas** |
| C | `data/track-c-pieces/bad_pieces.json` | 1 entrada placeholder | 10 piezas que deberian rechazarse (LLM-generadas con flaws) | **9 piezas mas** |
| D | `data/track-d-intel/*.mp3` | 0 archivos | 9 MP3 (3 obligatorios + 1 edge case + 5 opcionales) basados en los scripts en `docs/audio-scripts/` | **9 MP3s** |

## 🟡 Importantes (no bloquean pero mejoran señal)

### Templates de docs

| Archivo | Estado | Mejora sugerida |
|---------|--------|-----------------|
| `docs/AI_AUDIT_LOG_template.md` | placeholder con tabla vacia | Agregar 2 ejemplos concretos (uno bueno, uno malo) al principio para fijar el listón |
| `docs/AI_STACK_template.md` | placeholder | Agregar matriz de categorias sugeridas |
| `docs/ADR_template.md` | placeholder | OK |
| `docs/PREMORTEM_template.md` | placeholder | OK |
| `prompts/README.md` | guia OK | ✅ |
| `docs/sessions/README.md` | guia OK | ✅ |

### CLAUDE.md template

El skeleton actual tiene los headers correctos con `<!-- comments -->` guia. **Verificar que AgentLint corre OK contra el skeleton vacio** (no debe dar 0/100, debe dar algo razonable porque la estructura esta).

### Brand voice

| Archivo | Estado |
|---------|--------|
| `docs/BRAND_VOICE.md` | revisar que tenga contenido real para que Track C tenga referencia |

## 🟢 Nice-to-have (post-lanzamiento)

- **Docker compose** opcional para LLM broker local (mock) si el candidato quiere desarrollar sin consumir budget
- **Postman/Bruno collection** con la API del broker
- **Loom de Grego explicando el repo** (ya existe en `/growth-engineer` como video HeyGen self-hosted)

## ❌ Removido del scope

Los siguientes items quedaron OUT tras la decision de **eliminar el eval automatizado** (los 4 tracks son demasiado heterogeneos para un harness unificado):

- ~~`eval/eval.py` skeleton + implementacion de `run_track`~~ → eliminado, reemplazado por LLM judge async
- ~~`eval/held_out/cases_a.json` (5 casos Track A)~~ → no aplica
- ~~`eval/held_out/cases_b.json` (5 casos Track B)~~ → ya estaban en `private/eval-held-out/`, dejados como referencia historica
- ~~`eval/held_out/cases_c.json` (5 casos Track C)~~ → no aplica
- ~~`eval/held_out/cases_d.json` (5 casos Track D)~~ → no aplica
- ~~`make eval` como comando del Makefile~~ → reemplazado por `make judge` opcional

## Plan de lanzamiento (orden sugerido)

1. **Track C piezas** (3-4h): scrapear Meta Ad Library Loggro para good_pieces, LLM-gen bad_pieces, redactar 2 briefs faltantes
2. **Track D audios** (2-3h): ElevenLabs Studio multi-speaker contra los 9 scripts ya escritos
3. **AI_AUDIT_LOG_template examples** (30 min): 1 entrada buena + 1 mala al principio del template
4. **AgentLint test contra CLAUDE.md vacio** (15 min): correr y ajustar el skeleton si da <30
5. **Manual end-to-end test** (1h): tomar el rol de candidato, clonar el template, simular 2-3h de trabajo, ver que se siente

## Owner

@grrek (Grego Aristizabal) — ownership hasta lanzamiento. Sponsor: Edison Castro (review tecnico antes del envio).
