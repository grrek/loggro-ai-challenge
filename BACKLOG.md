# Backlog antes de lanzar el reto al primer candidato

Lo que falta para que el repo template este 100% listo. Auditado 2026-05-13.

## 🔴 Bloqueantes (sin esto, un candidato real no puede arrancar)

### Datasets sinteticos incompletos

| Track | Archivo | Estado | Meta | Falta |
|-------|---------|--------|------|-------|
| B | `data/track-b-insights/campaigns.json` | 2 entradas placeholder | 30 campañas reales con funnel completo, anomalias plantadas, lessons_learned en 5-7 de ellas | **28 campañas más** |
| C | `data/track-c-pieces/briefs.json` | 1 entrada placeholder | 3 briefs (DIAN, cross-sell POS, retencion Nomina) | **2 briefs más** |
| C | `data/track-c-pieces/good_pieces.json` | 1 entrada placeholder | 10 piezas referencia que pasan brand voice | **9 piezas más** |
| C | `data/track-c-pieces/bad_pieces.json` | 1 entrada placeholder | 10 piezas que deberian rechazarse (con razon documentada) | **9 piezas más** |
| D | `data/track-d-intel/*.mp3` | 0 archivos | 9 MP3 (3 obligatorios + 1 edge case + 5 opcionales) basados en los scripts en `docs/audio-scripts/` | **9 MP3s** |

### Eval held-out

| Archivo | Estado | Falta |
|---------|--------|-------|
| `eval/held_out/cases_a.json` | no existe | 5 casos secretos Track A (no se commitean al template publico, se cargan al evaluar) |
| `eval/held_out/cases_b.json` | no existe | 5 casos secretos Track B |
| `eval/held_out/cases_c.json` | no existe | 5 casos secretos Track C |
| `eval/held_out/cases_d.json` | no existe | 5 casos secretos Track D |

**Decision:** los held-out se mantienen privados. Generarlos antes de cada evaluacion, dropearlos al repo del candidato post-clone, correr `python eval/eval.py --track X --dataset eval/held_out/cases_X.json`, borrarlos.

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

El skeleton actual (105 lineas) tiene los headers correctos con `<!-- comments -->` guia. Esta bien para template — el candidato lo llena. **Verificar que AgentLint corre OK contra el skeleton vacio** (no debe dar 0/100 por estar vacio, debe dar algo razonable porque la estructura esta).

### Brand voice

| Archivo | Estado |
|---------|--------|
| `docs/BRAND_VOICE.md` | revisar que tenga contenido real para que Track C tenga referencia |

## 🟢 Nice-to-have (post-lanzamiento)

- **GitHub Actions** `.github/workflows/eval.yml`: hoy corre el eval skeleton. Cuando esten los held-out, agregar matrix por track para correr automaticamente en cada PR
- **Docker compose** opcional para LLM broker local (mock) si el candidato quiere desarrollar sin consumir budget
- **Postman/Bruno collection** con la API del broker
- **Loom de Grego explicando el repo** (existe en `/growth-engineer` como `PUBLIC_LOOM_URL` o el video self-hosted)

## Como completarlo

### Track B (28 campañas)
- Generar con script Python que produzca 30 entradas variadas siguiendo el schema actual (canales, productos, presupuestos, funnel, anomalias plantadas)
- Plantar las 3 anomalias listadas en el README + 2 campañas engañosas
- Subir como commit unico

### Track C (briefs + piezas)
- Pedir al equipo de Marketing (Ana Maria, Kissy) muestras reales recientes anonimizadas
- Generar variaciones con LLM siguiendo el formato actual

### Track D (9 MP3)
- Opcion 1: TTS con ElevenLabs usando los scripts ya escritos en `docs/audio-scripts/`
- Opcion 2: Whisper inverso (grabar humanos)
- Opcion 3: Mix (3 reales + 6 sinteticos para ahorrar tiempo)

### Held-out cases
- 5 casos por track, similares en formato al input pero NO en el dataset publico
- Plantear scenarios edge donde la solucion no-trivial gana
- Mantenerlos en un repo privado del equipo Loggro

## Owner

@grrek (Grego Aristizabal) — ownership hasta lanzamiento. Sponsor: Edison Castro (review tecnico antes del envio).
