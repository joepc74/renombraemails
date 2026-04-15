import extract_msg, email, os, re
from email import policy
from email.utils import parsedate_to_datetime

def obtener_fecha_msg(ruta_archivo):
    # Cargamos el archivo .msg
    msg = extract_msg.Message(ruta_archivo)

    # Extraemos la fecha
    # .date suele devolver el valor del campo 'Date' del header
    fecha_envio = msg.date

    # print(f"Asunto: {msg.subject}")
    # print(f"Fecha de envío: {fecha_envio}")

    # Es importante cerrar el objeto para liberar el archivo
    msg.close()
    return fecha_envio

def obtener_fecha_eml(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        # Usamos policy.default para que el objeto sea más fácil de manejar
        msg = email.message_from_binary_file(f, policy=policy.default)

    # Extraemos la cabecera 'Date'
    fecha_str = msg['date']

    # Convertimos el string de la fecha a un objeto datetime de Python
    fecha_dt = parsedate_to_datetime(fecha_str)

    # print(f"Fecha original (string): {fecha_str}")
    # print(f"Fecha como objeto datetime: {fecha_dt}")

    return fecha_dt

if __name__ == "__main__":
    # Obtengo todos los archivos .eml y .msg del directorio actual
    import os
    archivos = [f for f in os.listdir('.') if f.endswith('.eml') or f.endswith('.msg')]
    for archivo in archivos:
        # Si el archivo comienza por YYYYMMDD HHMMSS lo ignoro
        if re.match(r'^\d{8} \d{6}', archivo):
            print(f"Archivo {archivo} ya renombrado, se ignora.")
            continue
        if archivo.endswith('.eml'):
            print(f"Procesando {archivo}...")
            fecha=obtener_fecha_eml(archivo)
        elif archivo.endswith('.msg'):
            print(f"Procesando {archivo}...")
            fecha=obtener_fecha_msg(archivo)
        # Renombro el archivo con el formato YYYYMMDD HHMMSS nombreoriginal.ext
        nuevo_nombre = f"{fecha.strftime('%Y%m%d %H%M%S')} {archivo}"
        os.rename(archivo, nuevo_nombre)
        print(f"Archivo {archivo} renombrado a {nuevo_nombre}.")
