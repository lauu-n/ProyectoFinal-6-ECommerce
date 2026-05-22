class AFDProcesoCompra:
    def __init__(self):
        self.estados = {"inicio", "buscando", "carrito", "pago", "confirmado", "cancelado"}
        self.alfabeto = {"agregar", "quitar", "pagar", "confirmar", "cancelar"}
        self.transiciones = {
            "inicio": {"agregar": "buscando"},
            "buscando": {"agregar": "buscando", "quitar": "buscando", "pagar": "carrito"},
            "carrito": {"pagar": "pago", "cancelar": "cancelado"},
            "pago": {"confirmar": "confirmado", "cancelar": "cancelado"},
            "confirmado": {"cancelar": "cancelado"},
            "cancelado": {}
        }
        self.estado_actual = "inicio"
    
    def procesar(self, evento):
        if evento not in self.alfabeto:
            raise ValueError(f"Evento {evento} no permitido")
        if evento in self.transiciones[self.estado_actual]:
            self.estado_actual = self.transiciones[self.estado_actual][evento]
        else:
            raise Exception(f"Transición no válida desde {self.estado_actual} con {evento}")
        return self.estado_actual
    
    def aceptar(self):
        return self.estado_actual in {"confirmado", "cancelado"}