from grafo import GrafoRutas
from afd import AFDProcesoCompra
from mef import MEFPedido

# 1. Grafo de rutas
ciudades = ["Bogota", "Medellin", "Cali", "BodegaCentral"]
grafo = GrafoRutas(ciudades)
grafo.agregar_arista("BodegaCentral", "Bogota", 10)
grafo.agregar_arista("BodegaCentral", "Medellin", 20)
grafo.agregar_arista("BodegaCentral", "Cali", 30)
grafo.agregar_arista("Bogota", "Cali", 25)
grafo.agregar_arista("Medellin", "Bogota", 15)

# 2. AFD proceso
afd = AFDProcesoCompra()
print("=== Simulación de compra ===")
eventos = ["agregar", "agregar", "pagar", "confirmar"]
for e in eventos:
    estado = afd.procesar(e)
    print(f"Evento: {e} → Estado AFD: {estado}")

if afd.estado_actual == "confirmado":
    # 3. MEF pedido
    pedido = MEFPedido()
    print("\n=== Flujo MEF ===")
    for ev in ["empaquetar", "enviar_a_bodega", "despachar", "entregar"]:
        nuevo = pedido.transitar(ev)
        print(f"Evento MEF: {ev} → {nuevo}")

# 4. Dijkstra
print("\n=== Ruta más corta desde BodegaCentral ===")
distancias = grafo.dijkstra("BodegaCentral")
for ciudad, dist in distancias.items():
    print(f"  → {ciudad}: {dist} km")

# 5. Floyd-Warshall
print("\n=== Matriz de distancias mínimas (Floyd-Warshall) ===")
matriz = grafo.floyd_warshall()
for i, fila in enumerate(matriz):
    print(f"{ciudades[i]}: {fila}")