import requests
import smtplib
import os
from email.mime.text import MIMEText

EMAIL_ORIGEN = os.environ["EMAIL_ORIGEN"]
EMAIL_DESTINO = os.environ["EMAIL_DESTINO"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

LINK_RESERVA = "https://ww3.e-com.cl/pagos/licenciasweb_v4/index.asp?id=37"

FECHAS = [
    "16/02/2026",
    "17/02/2026",
    "18/02/2026",
    "19/02/2026",
    "20/02/2026",
    "23/02/2026",
    "24/02/2026",
    "25/02/2026",
    "26/02/2026",
    "27/02/2026"
]

URL = "https://ww3.e-com.cl/pagos/licenciasweb_v4/Controlador/cont_horario_tramites.asp"

BASE_DATA = {
    "rut": "16374820-7",
    "id": "37",
    "tramite": "1",
    "clase": "1",
    "Turno": "10"
}

import time
import requests

for fecha in FECHAS:
    data = BASE_DATA.copy()
    data["fecha"] = fecha

    try:
        response = requests.post(
            URL,
            data=data,
            timeout=30  # ⬅️ más paciencia
        )

        texto = response.text.lower()

        if "no existen horas asignadas" not in texto:
            enviar_correo(fecha)
            print(f"Correo enviado para fecha {fecha}")
            break
        else:
            print(f"{fecha}: todo copado")

    except requests.exceptions.Timeout:
        print(f"⚠️ Timeout al consultar {fecha}, sigo con la siguiente...")
        continue

    except Exception as e:
        print(f"⚠️ Error inesperado en {fecha}: {e}")
        continue

