# eval/

Contrato de evaluacion automatica para tu entregable.

## Archivos

| Archivo | Que es | Quien lo toca |
|---|---|---|
| `judge_prompt.md` | Prompt publico para LLM-as-judge. Rubrica de 5 dimensiones | Lo lees vos; lo extendes en Apendice.5 |
| `eval.py` | Skeleton del eval harness. Implementa `run_track` | Lo completas vos |
| `held_out/` | Dataset secreto. Provisto por Loggro al evaluarte | NO commitees nada aca (esta en `.gitignore`) |

## Contrato de `eval.py`

`run_track(track, cases)` debe retornar:

```python
{
    "total": int,
    "passed": int,
    "reasoning_quality": float,  # 0-1
    "details": [
        {"case_id": str, "passed": bool, "reasoning_quality": float, "notes": str}
    ]
}
```

## Threshold publicado

Para pasar el gate code-based:

- `passed >= 3` (de los 5 casos held_out)
- `reasoning_quality >= 0.7`

## Que es held_out

Loggro tiene 5 casos secretos que no estan en este repo. Cada uno tiene groundtruth conocido. Cuando entregas tu pipeline, corremos `python eval/eval.py --track {x} --dataset held_out/cases.json` y vemos cuantos pasas.

**No intentes adivinar el contenido del held_out.** Es secreto para que el eval sea AI-resistant.

## Judge extension (Apendice.5)

Pasos:

1. Lee `judge_prompt.md` completo
2. Identifica 2-3 criterios adicionales especificos de tu track
3. Extiende el prompt y guardalo como `judge_prompt_extended.md`
4. Genera 2 outputs deliberadamente malos para tu track (cada uno falla en algo distinto)
5. Corre tu judge extendido contra los 2 outputs malos
6. Reporta en tu README:
   - ¿Que criterios anadiste y por que?
   - ¿Tu judge atrapo el sabotaje? Si NO, ¿que ajustaste para que lo atrapara?

Este sub-ejercicio es el de **mas alto signal** de toda la prueba. Si lo haces bien, suma puntos en `ai_fluency` y `eval_discipline`.

## Tip de costo del judge

El judge usa Claude API por candidato. Con prompt caching del system + rubrica (es la misma para todos), el caching hit rate puede llegar a 90%. Costo por candidato: ~$0.20 USD. Sin caching: ~$2 USD.
