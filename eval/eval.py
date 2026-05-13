"""eval.py: Skeleton del eval harness del reto VE-1770.

Tu trabajo: implementar `run_track` para tu track. El resto es plumbing.

Uso:
    python eval/eval.py --dry-run                      # valida estructura
    python eval/eval.py --track d                      # corre contra dataset held_out (provisto por Loggro)
    python eval/eval.py --track d --dataset path/cases.json   # corre contra custom dataset

Lee eval/README.md para el contrato completo.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_dataset(path: Path) -> list[dict[str, Any]]:
    """Carga un dataset de casos. Retorna [] si no existe (CI publico).

    El formato del held_out es secreto. Loggro lo provee al momento de evaluarte.
    """
    if not path.exists():
        return []
    with path.open() as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected list at {path}, got {type(data).__name__}")
    return data


def run_track(track: str, cases: list[dict[str, Any]]) -> dict[str, Any]:
    """Tu pipeline contra los casos. IMPLEMENTAR.

    Debe retornar:
        {
            "total": int,                # total de casos procesados
            "passed": int,               # cuantos pasaron el criterio
            "reasoning_quality": float,  # promedio 0-1
            "details": [
                {"case_id": str, "passed": bool, "reasoning_quality": float, "notes": str}
            ]
        }

    Criterio para "passed":
        - Track A: respuesta clasificada con groundtruth_intent correcto
        - Track B: insight identificado matchea con groundtruth de la anomalia plantada
        - Track C: pieza generada pasa brand voice review automatico (sin em-dashes, sin palabras prohibidas, dentro de longitud por canal)
        - Track D: insights.json conforme al schema y matchea fields clave del groundtruth
    """
    raise NotImplementedError(
        f"Implementa run_track('{track}', cases) en eval/eval.py. "
        "Tu pipeline debe correr aqui contra cada case. Ver docstring."
    )


def threshold_check(result: dict[str, Any]) -> bool:
    """Threshold publicado para avanzar: 3/5 casos pasaron + reasoning_quality >= 0.7."""
    passed = result.get("passed", 0)
    rq = result.get("reasoning_quality", 0.0)
    return passed >= 3 and rq >= 0.7


def main() -> int:
    parser = argparse.ArgumentParser(description="Eval harness del reto VE-1770")
    parser.add_argument(
        "--track",
        choices=["a", "b", "c", "d"],
        help="Track que entregaste (a, b, c, o d)",
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("eval/held_out/cases.json"),
        help="Path al dataset de casos. Default: eval/held_out/cases.json (provisto por Loggro)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Solo valida estructura del eval harness, no corre nada",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Opcional: escribe el resultado JSON a este archivo",
    )

    args = parser.parse_args()

    if args.dry_run:
        print("[dry-run] eval.py skeleton OK")
        print("[dry-run] Para correr real: implementa run_track en eval/eval.py")
        print("[dry-run] Y corre: python eval/eval.py --track {a|b|c|d}")
        return 0

    if not args.track:
        print("[error] --track requerido cuando no se usa --dry-run", file=sys.stderr)
        return 1

    cases = load_dataset(args.dataset)
    if not cases:
        print(
            f"[warning] No hay casos en {args.dataset}.",
            "El held_out es secreto y Loggro lo provee al evaluarte.",
            file=sys.stderr,
        )
        return 0

    print(f"[info] Corriendo eval para track {args.track.upper()} con {len(cases)} casos...")
    result = run_track(args.track, cases)

    output_json = json.dumps(result, indent=2, ensure_ascii=False)
    print(output_json)

    if args.output:
        args.output.write_text(output_json + "\n")
        print(f"[info] Resultado guardado en {args.output}", file=sys.stderr)

    if threshold_check(result):
        print("[pass] Threshold cumplido (>=3/5 + reasoning >= 0.7)", file=sys.stderr)
        return 0
    else:
        print("[fail] Threshold no cumplido", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
