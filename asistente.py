class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historial = []
        self.nombre = None

    def responder(self, mensaje):
        self.historial.append({"usuario": mensaje})

        texto = mensaje.lower()
        if 'hola' in texto or 'buenas' in texto:
            respuesta = f"¡Hola! Bienvenido a {self.nombre_negocio}."
            self.historial.append({"asistente": respuesta})
            return respuesta

        return "" 
