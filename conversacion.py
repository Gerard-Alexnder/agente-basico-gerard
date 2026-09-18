def iniciar_conversacion(asistente):
    print(f"Bienvenido a {asistente.nombre_negocio}.")

    while True:
        mensaje = input('Tu mensaje: ')
        respuesta = asistente.responder(mensaje)
        print(respuesta)

        if any(palabra in mensaje.lower() for palabra in ('adios', 'chao', 'salir')):
            break

    asistente.mostrar_historial()
