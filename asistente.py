class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historial = []
        self.nombre = None
        self.nombre_usuario = None
        self.preguntas_frecuentes = {
            'horario': 'Nuestro horario de atención es de lunes a sábado, de 9:00 a 18:00.',
            'ubicacion': 'Estamos ubicados en la avenida principal del centro.',
            'precios': 'Los precios varían según el servicio, pero ofrecemos opciones accesibles.'
        }
        self.precios_servicios = {
            'corte': 25,
            'manicure': 30,
            'pedicure': 35
        }

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta
        return 'No entendí tu pregunta.'

    def calcular_presupuesto(self):
        servicio = input('¿Qué servicio le interesa? ').strip().lower()
        if servicio not in self.precios_servicios:
            return 'Ese servicio no está disponible.'

        try:
            cantidad = int(input('¿Cuántas veces quiere agendarlo? ').strip())
        except ValueError:
            return 'Ingrese un número válido.'

        costo_total = self.precios_servicios[servicio] * cantidad
        return f'El costo total para {servicio} ({cantidad} vez/veces) es: ${costo_total}'

    def responder(self, mensaje):
        self.historial.append({"usuario": mensaje})

        texto = mensaje.strip()
        texto_normalizado = texto.lower()

        if any(palabra in texto_normalizado for palabra in ('adios', 'salir', 'chao')):
            if self.nombre_usuario:
                respuesta = f"¡Hasta luego {self.nombre_usuario}! Gracias por visitar {self.nombre_negocio}."
            else:
                respuesta = f"¡Hasta luego! Gracias por visitar {self.nombre_negocio}."
            self.historial.append({"asistente": respuesta})
            return respuesta

        if texto_normalizado.startswith('me llamo'):
            nombre = texto[8:].strip()
            if nombre:
                self.nombre_usuario = nombre.capitalize()
                respuesta = f"¡Hola {self.nombre_usuario}! Bienvenido a {self.nombre_negocio}."
                self.historial.append({"asistente": respuesta})
                return respuesta

        if any(palabra in texto_normalizado for palabra in ('calcular', 'presupuesto', 'costo')):
            respuesta = self.calcular_presupuesto()
            self.historial.append({"asistente": respuesta})
            return respuesta

        if 'hola' in texto_normalizado or 'buenas' in texto_normalizado:
            if self.nombre_usuario:
                respuesta = f"¡Hola {self.nombre_usuario}! Bienvenido a {self.nombre_negocio}."
            else:
                respuesta = f"¡Hola! Bienvenido a {self.nombre_negocio}."
            self.historial.append({"asistente": respuesta})
            return respuesta

        respuesta = self.buscar_faq(texto_normalizado)
        self.historial.append({"asistente": respuesta})
        return respuesta
