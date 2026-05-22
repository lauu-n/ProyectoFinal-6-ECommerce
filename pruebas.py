from afd import AFDProcesoCompra
from mef import MEFPedido

def test_afd():
    casos = [
        (["agregar", "pagar", "confirmar"], "confirmado"),
        (["agregar", "cancelar"], "cancelado"),
        (["agregar", "pagar", "cancelar"], "cancelado"),
        (["pagar"], "error"),  # no debería funcionar
    ]
    for eventos, esperado in casos:
        afd = AFDProcesoCompra()
        try:
            for e in eventos:
                afd.procesar(e)
            print(f"Eventos {eventos} → {afd.estado_actual} (esperado {esperado})")
        except:
            print(f"Eventos {eventos} → error (esperado {esperado})")

def test_mef():
    p = MEFPedido()
    try:
        p.transitar("empaquetar")
        p.transitar("enviar_a_bodega")
        p.transitar("despachar")
        p.transitar("entregar")
        print("MEF OK: entregado alcanzado")
    except:
        print("Error en MEF")

if __name__ == "__main__":
    test_afd()
    test_mef()