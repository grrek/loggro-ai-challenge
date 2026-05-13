# ADR-NNN: [Titulo de la decision]

**Status:** propuesta | aceptada | reemplazada por ADR-MMM | obsoleta
**Fecha:** YYYY-MM-DD
**Decisores:** [tu nombre]

## Contexto

<!--
Por que esta decision aparece ahora. Que problema resuelves. Que constraints te llevaron aca.

Maximo 5 oraciones. Si no podes resumirlo en 5 oraciones, tal vez la decision es muy grande y necesitas partirla en 2 ADRs.
-->

## Decision

<!--
Que decidiste, en una frase.

Ejemplo: "Uso Whisper self-hosted en Loggro Labs en vez de Deepgram API para STT."
-->

## Alternativas consideradas

<!--
2 a 3 alternativas que descartaste. Para cada una:
- Que era
- Por que la descartaste

Ejemplo:
- **Deepgram API:** mejor precision con acentos paisas (WER ~5% vs Whisper ~12% en LATAM). Descartada por costo: a 9 audios cuesta $0.40 USD pero a 1000 audios/mes ya pesa $40, y el budget post-reto es cero.
- **AssemblyAI:** similar a Deepgram pero peor docs en espanol. Descartada por la misma razon de costo + menos confianza.
-->

## Consecuencias

**Positivas:**

<!-- 2-4 bullets -->

**Negativas:**

<!-- 1-3 bullets honestos -->

**Riesgos:**

<!--
Que podria salir mal con esta decision. Como lo detectarias. Que harias si pasa.

Ejemplo:
- Riesgo: Whisper falla con acentos paisas en audios reales de Loggro
- Como lo detectaria: WER >20% en eval set de 5 acentos regionales
- Mitigacion: switch a Deepgram con feature flag, costo absorbible para 3 meses
-->
