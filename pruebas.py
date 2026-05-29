# pruebas.py - Actualizado para el AFD simplificado
from afd import AFDProcesoCompra
from mef import MEFPedido

def test_afd():
    casos = [
        (["agregar", "agregar", "pagar", "confirmar"], "confirmado", "Compra exitosa"),
        (["agregar", "cancelar"], "cancelado", "Cancelación temprana"),
        (["agregar", "pagar", "cancelar"], "cancelado", "Cancelación en pago"),
        (["pagar"], "error", "Pagar sin productos (debe dar error)"),
        (["agregar", "pagar", "confirmar", "cancelar"], "cancelado", "Cancelar después de confirmar"),
    ]
    
    print("=== PRUEBAS DEL AFD ===\n")
    for eventos, esperado, nombre in casos:
        afd = AFDProcesoCompra()
        try:
            for e in eventos:
                afd.procesar(e)
            resultado = afd.estado_actual
            estado = "PASÓ" if resultado == esperado else f"FALLÓ (esperaba {esperado}, obtuvo {resultado})"
            print(f"{nombre}: {estado}")
        except Exception as e:
            if esperado == "error":
                print(f"{nombre}: PASÓ (error correctamente lanzado)")
            else:
                print(f"{nombre}: FALLÓ (error inesperado: {e})")

def test_mef():
    print("\n~ PRUEBAS DE LA MEF ~\n")
    p = MEFPedido()
    try:
        p.transitar("empaquetar")
        p.transitar("enviar_a_bodega")
        p.transitar("despachar")
        p.transitar("entregar")
        if p.estado_actual == "entregado":
            print("Flujo completo hasta entregado: PASÓ")
        else:
            print(f"Flujo completo: FALLÓ (terminó en {p.estado_actual})")
    except Exception as e:
        print(f"Flujo completo: FALLÓ ({e})")
    
    # Prueba de devolución
    p2 = MEFPedido()
    try:
        p2.transitar("empaquetar")
        p2.transitar("enviar_a_bodega")
        p2.transitar("despachar")
        p2.transitar("devolver")
        if p2.estado_actual == "devuelto":
            print("Devolución desde en_tránsito: PASÓ")
        else:
            print(f"Devolución: FALLÓ (terminó en {p2.estado_actual})")
    except Exception as e:
        print(f"Devolución: FALLÓ ({e})")

if __name__ == "__main__":
    test_afd()
    test_mef()
