class MEFPedido:
    def __init__(self):
        self.estados = ["confirmado", "empacando", "en_bodega", "en_transito", "entregado", "devuelto"]
        self.eventos = {
            "confirmado": ["empaquetar"],
            "empacando": ["enviar_a_bodega"],
            "en_bodega": ["despachar"],
            "en_transito": ["entregar", "devolver"],
            "entregado": [],
            "devuelto": []
        }
        self.estado_actual = "confirmado"
        self.log = []
    
    def transitar(self, evento):
        if evento not in self.eventos.get(self.estado_actual, []):
            raise Exception(f"Evento {evento} no permitido en estado {self.estado_actual}")
        nuevos_estados = {
            ("confirmado", "empaquetar"): "empacando",
            ("empacando", "enviar_a_bodega"): "en_bodega",
            ("en_bodega", "despachar"): "en_transito",
            ("en_transito", "entregar"): "entregado",
            ("en_transito", "devolver"): "devuelto"
        }
        self.estado_actual = nuevos_estados[(self.estado_actual, evento)]
        self.log.append(f"{evento} -> {self.estado_actual}")
        return self.estado_actual