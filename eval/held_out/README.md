# held_out/

Este directorio esta en `.gitignore`. Loggro lo provee al momento de evaluarte con un archivo `cases.json` que tu `eval.py` lee.

No intentes anadir cases aqui. Si lo haces, Loggro lo nota en `git log` y resta puntos en `honesty_criterion`.

Si quieres probar tu pipeline contra casos propios, ponelos en otra ruta y pasale `--dataset` a `eval.py`:

```bash
python eval/eval.py --track d --dataset mis_casos/cases.json
```
