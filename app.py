from flask import Flask
from pathlib import Path

app = Flask(__name__)
ARCHIVO_CONTADOR = Path(__file__).parent / 'data' / 'visits.txt'


def leer_contador() -> int:
    if not ARCHIVO_CONTADOR.exists():
        return 0
    return int(ARCHIVO_CONTADOR.read_text().strip() or 0)


def guardar_contador(valor: int) -> None:
    ARCHIVO_CONTADOR.parent.mkdir(parents=True, exist_ok=True)
    ARCHIVO_CONTADOR.write_text(str(valor))


@app.get('/')
def home():
    visitas = leer_contador() + 1
    guardar_contador(visitas)
    return f'''<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Práctica de Docker</title>
  <style>
    body {{ font-family: Arial, sans-serif; display:flex; justify-content:center; align-items:center; height:100vh; margin:0; background:#f5f7fa; }}
    .card {{ background:white; padding:40px; border-radius:14px; box-shadow:0 8px 30px rgba(0,0,0,.08); text-align:center; }}
    h1 {{ margin-bottom:12px; }}
    .count {{ font-size:48px; font-weight:bold; margin:16px 0; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Práctica de Docker</h1>
    <p>Esta página se ha visitado</p>
    <div class="count">{visitas}</div>
    <p>veces.</p>
  </div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
