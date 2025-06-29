# 📈 Bot Trader

Este proyecto es un bot de trading que analiza acciones mediante indicadores técnicos utilizando `pandas_ta`, `pandas`, `numpy` y otros módulos de análisis.

---

## 🚀 Requisitos

- Python 3.11 (recomendado para compatibilidad con `pandas_ta`)
- Git (opcional para clonar el repositorio)
- Acceso a Polygon.io u otra fuente de datos (según configuración)

---

## 🛠️ Instalación

1. **Clonar el repositorio (si aplica)**

```bash
git clone https://github.com/tu_usuario/bot-trader.git
cd bot-trader
```

2. **Crear entorno virtual**

```bash
python -m venv .venv
```

3. **Activar entorno virtual**

- En **Windows**:

```bash
.\.venv\ScriptsActivate
```

- En **Linux/Mac**:

```bash
source .venv/bin/activate
```

4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

---

## 🐞 Fix obligatorio para `pandas_ta`

`pandas_ta` tiene un bug en `squeeze_pro.py` que rompe la importación con numpy >= 1.20.

### 🔧 Para solucionarlo:

1. Abrí este archivo:

```
<tu_python>\Lib\site-packages\pandas_ta\momentum\squeeze_pro.py
```

2. Cambiá esta línea:

```python
from numpy import NaN as npNaN
```

por:

```python
from numpy import nan as npNaN
```

Guardá y listo.

---

## ⚙️ Ejecución

Con el entorno activado:

```bash
python main.py
```

---

## 📁 Estructura del Proyecto (ejemplo)

```
bot-trader/
│
├── analysis/
│   └── signal_engine.py       # Lógica de indicadores y señales
├── data/
│   └── polygon_client.py      # Cliente para descargar datos de Polygon.io
├── main.py                    # Script principal
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Este archivo
└── .venv/                     # Entorno virtual (ignorado por git)
```

---

## 🧩 Dependencias clave

```txt
pandas==2.2.2
numpy==1.26.4
pandas_ta==0.3.14b0
```

Están incluidas en `requirements.txt`.

---

## 🧠 TODO (próximas features)

- [ ] Conectar con bot de Telegram
- [ ] Ejecutar señales en tiempo real
- [ ] Backtests automáticos
- [ ] Logging de entradas y salidas
- [ ] Reportes por correo o chat

---

## 🧾 License

MIT (o la que vos quieras usar)

---

## ✉️ Contacto

Hecho con código y mate por Juancho.
