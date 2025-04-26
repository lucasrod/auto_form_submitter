# 🚀 Project‑Specific Instructions — **auto_form_submitter**

Automatiza de extremo a extremo la obtención de turnos consulares en *prenotami.esteri.it* usando **Python 3.11** + **Playwright**. Todo el desarrollo sigue **TDD**: cada nueva funcionalidad entra primero como test que falla, luego código hasta que pasa.

---

## 📁 Estructura de Carpetas

```text
auto_form_submitter/
├── config/
│   ├── .env.testing      # credenciales dummy (desarrollo)
│   ├── .env.prod         # credenciales reales  (producción)
│   ├── urls.json         # última URL detectada + timestamp
│   └── form_payload_templates.json
├── data/                 # plantillas/fixtures
├── logs/                 # scraper.log, incidents.csv
├── src/
│   ├── auth/login_handler.py
│   ├── services/
│   │   ├── services_scraper.py
│   │   └── booking_handler.py
│   ├── otp/otp_handler.py
│   └── utils/
│       ├── browser.py
│       ├── env_loader.py  # carga .env dinámico
│       └── email_client.py
└── tests/                # suite pytest (TDD) con fixtures globales
```

---

## ⚙️ Flujos Principales

| Modo            | Descripción                                                                                       | Ejecutar con                                    |
|-----------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------|
| **TESTING**     | Rellena formularios, solicita OTP, **no** hace submit final. Usa endpoint `…/Booking/5126`.         | `ENVIRONMENT=TESTING python src/main.py`        |
| **PRODUCTION**  | Busca link en `/Services`, persiste en `urls.json`, rellena y **envía** con OTP real. Endpoint `…/Booking/5544`. | `ENVIRONMENT=PROD    python src/main.py`        |

`utils/env_loader.py` selecciona **.env.testing** o **.env.prod** dependiendo de `ENVIRONMENT` (var de shell o en `config/.env`).

---

## 🔑 Componentes Críticos

| Módulo | Responsabilidad clave |
|--------|-----------------------|
| **`utils/env_loader.py`** | Carga dinámica de variables: `ENVIRONMENT`→`.env.*` ; accesible por todos los módulos. |
| **`services/services_scraper.py`** | Navega a `/Services`, toma **fila 6 / columna 4**. Persiste URL & timestamp en `config/urls.json`. Reintenta con back‑off y registra caída si aparece HTML de “Unavailable” o si redirige a `/Home/Login`. |
| **`otp/otp_handler.py`** | Clic en *Send OTP*, lee Gmail vía IMAP (`imap.gmail.com:993`), extrae código `\d{6}`. |
| **`services/booking_handler.py`** | Rellena formulario usando plantillas JSON, gestiona campos opcionales, marca privacidad, envía (solo en PROD). |
| **`auth/login_handler.py`** | Login Playwright headless, evasión básica anti‑bot, espera `/UserArea`. |

---

## 🔁 Manejo de Caídas / Alta Demanda

1. Detectar html `<title>Unavailable</title>` **o** página `Index - Prenot@Mi` con tabla pero sin botón “Prenota”.
2. Registrar en `logs/incidents.csv`: `timestamp,url,status`.
3. Aplicar back‑off exponencial (30 s → 60 → 120 …).
4. Tras recuperación, registrar evento *UP* y continuar workflow.

---

## 🧪 Pruebas Clave (TDD)

- `test_env.py`    → variables cargadas por `env_loader`.
- `test_auth.py`   → login ok (Pytest‑Playwright, headless true).
- `test_services_scraper.py` → parseo HTML fixture, extrae URL correcta (5126 | 5544).
- `test_booking_handler.py`  → relleno dinámico con plantilla dummy.
- `test_site_down.py`        → simula HTML “Unavailable”, verifica logging & back‑off.

`tests/conftest.py` carga el entorno una sola vez por sesión.

---

## 🔧 Instalación Rápida

```bash
conda create -n auto_form_submitter python=3.11 -y
conda activate auto_form_submitter
pip install -r requirements.txt
playwright install  # descarga browsers
```

---

## 📜 Comandos Útiles

```bash
# Dry‑run (sin submit final)
ENVIRONMENT=TESTING python src/main.py

# Ejecutar suite completa de tests (TDD always green)
ENVIRONMENT=TESTING pytest -q
```

---

## 🗺️ Backlog Activo (resumen)

1. **Scraper robusto de Services** con multi‑idioma (ITA/SPA) y reintentos.
2. **Logger de caídas** y alerta cuando el sitio vuelva online.
3. **Finalizar cliente IMAP** (manejo de OAuth tokens y re‑login automático).
4. **Notificaciones Telegram** opcionales para nuevas citas o incidentes.
5. **Proxy/Rotación IP** para futuras defensas anti‑bot.
6. **Pack CLI (Typer)** → `autoform --prod`.
7. **Dockerfile slim** listo para VPS.