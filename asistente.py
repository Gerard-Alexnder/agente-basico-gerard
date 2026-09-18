class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historial = []
        self.nombre = None
        self.preguntas_frecuentes = {
            'horario': 'Nuestro horario de atención es de lunes a sábado, de 9:00 a 18:00.',
            'ubicacion': 'Estamos ubicados en la avenida principal del centro.',
            'precios': 'Los precios varían según el servicio, pero ofrecemos opciones accesibles.'
        }

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta
        return 'No entendí tu pregunta.'

    def responder(self, mensaje):
        self.historial.append({"usuario": mensaje})

        texto = mensaje.lower()
        if 'hola' in texto or 'buenas' in texto:
            respuesta = f"¡Hola! Bienvenido a {self.nombre_negocio}."
            self.historial.append({"asistente": respuesta})
            return respuesta

        respuesta = self.buscar_faq(texto)
        self.historial.append({"asistente": respuesta})
        return respuesta
