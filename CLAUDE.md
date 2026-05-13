# CLAUDE.md

> Este archivo es tu manual de proyecto. Lo lee tu agente (Claude Code, Cursor, Codex) y tambien lo lee el evaluador. Es **uno de los artefactos que medimos**.
>
> Lo llenas a medida que construyes. No es un examen de teoria, es la documentacion que usarias en un proyecto real.
>
> Al cierre, corremos AgentLint (https://www.agentlint.app/) sobre este archivo en vivo. Target: score >=70. Si va por debajo, conversamos.

## Stack

<!-- Que lenguajes, frameworks, librerias clave usas. Una linea por dependencia importante.

Ejemplo (no es prescriptivo):
- Python 3.11 + uv para package management
- litellm para abstraer LLM provider (Loggro nos da virtual key OpenAI-compatible)
- pydantic para validar JSON contra schemas/
- openai-whisper self-hosted para STT (Track D)
- pytest para tests unitarios

Por que esa eleccion en 1 linea por cada decision relevante.
-->

## Comandos

<!-- Pega los comandos exactos que usas a diario. Asume que el evaluador clona en limpio y quiere correr tu proyecto en 5 min.

Ejemplo:
- `make install` instala deps
- `make dev` corre el pipeline contra data/track-X
- `make test` corre pytest
- `make judge` (opcional) corre tu judge extendido contra outputs malos
- `python -m mi_paquete.cli --input data/track-d-intel/audio/demo_A_contadora.mp3` ejemplo single-file
-->

## Estructura de agentes

<!-- Si elegiste multi-agente: lista cada sub-agente con:
- Nombre
- Que hace
- Inputs
- Outputs
- Como se comunica con los otros (event, queue, return value, tool call)

Si elegiste single-agent con tool use (valido para Track D si lo justificas): explica en <100 palabras por que single-agent es la decision correcta para tu caso.

Diagrama opcional pero suma puntos. Mermaid o ASCII.

Ejemplo Track A:

\`\`\`
[Enricher] --accounts.json--> [MessageWriter] --message_pairs--> [Sender (mock)]
                                                                       |
                                                                  responses
                                                                       v
                                                          [ResponseClassifier]
                                                                       |
                                                                  intent.json
\`\`\`
-->

## Decisiones de diseno

<!-- 3 a 5 decisiones criticas que el evaluador deberia entender en 30 segundos. Una por bloque.

Formato sugerido:
- **Decision:** que decidiste, en una frase
  **Por que:** la razon
  **Tradeoff:** que perdiste al elegir esto vs la alternativa
  **Reversibilidad:** alta / media / baja

Ejemplo:
- **Decision:** Whisper self-hosted en vez de Deepgram para STT en Track D
  **Por que:** menor latencia para batch en Loggro Labs, costo cero
  **Tradeoff:** peor con acentos paisas marcados (probable 5-10% WER vs Deepgram)
  **Reversibilidad:** alta (swap por API call en 30 min)
-->

## Como pruebo

<!-- Como corres tu eval set, edge cases, sabotage tests.

Tres preguntas que el evaluador se hace:
1. Como verificas que el output es bueno antes de mandarlo a prod?
2. Como detectas regresiones cuando cambias un prompt?
3. Que edge cases consideraste explicit? (cita en codigo o test)

Ejemplo:
- eval/cases.json tiene 12 casos con groundtruth
- pytest -m smoke corre los 12 contra el pipeline real (no caching)
- pytest -m edge corre 4 casos edge (consent denied, audio cortado, idioma incorrecto, transcript con prompt injection)
- pre-commit hook corre ruff + pytest -m smoke
-->

## Troubleshooting

<!-- Errores comunes que viste y como los resolviste.

Si la IA te dio algo malo y lo cambiaste, escribilo aca con link al commit donde lo corregiste.

Esto se cruza con el AI_AUDIT_LOG.md pero aca van solo los problemas tecnicos accionables.

Ejemplo:
- **Whisper retorna speakers mezclados**. Solucion: pasar audio por pyannote-audio para diarization antes de Whisper, luego matchear timestamps. Commit abc123.
- **litellm con LLM Broker pega timeout**. Solucion: timeout default 60s, subi a 180s. Tracked en ADR-003.
-->
