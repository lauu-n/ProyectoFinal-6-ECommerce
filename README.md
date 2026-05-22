# Proyecto 6 - Plataforma de Compras con Rutas de Envío
Laura Niño

---

## Descripción del problema

Una tienda en línea requiere un sistema que:
  - Valide los pasos permitidos en el proceso de compra (búsqueda, carrito, pago, confirmación, cancelación).
  - Gestione el estado físico de cada pedido (confirmado, empacando, en bodega, en tránsito, entregado/devuelto).
  - Calcule rutas de envío óptimas entre bodegas y ciudades utilizando algoritmos de caminos mínimos.

---

## Componentes del proyecto

| Componente | Tecnología/Algoritmo | Propósito |
|------------|----------------------|------------|
| AFD | Autómata Finito Determinista | Validar secuencia de acciones del comprador |
| MEF | Máquina de Estado Finito | Controlar el ciclo de vida del pedido |
| Grafo | Lista de adyacencia | Representar red de bodegas y ciudades |
| Dijkstra | Algoritmo de caminos mínimos | Ruta más corta desde un origen |
| Floyd-Warshall | Programación dinámica | Matriz de distancias mínimas entre todos los pares |

---

## Estructura del código

```
proyecto6/
│
├── main.py # Simulación completa del flujo
├── afd.py # Clase AFDProcesoCompra
├── mef.py # Clase MEFPedido
├── grafo.py # Clase GrafoRutas (Dijkstra + Floyd-Warshall)
├── pruebas.py # Casos de prueba automatizados
└── README.md # Este archivo
```

---

## Requisitos para ejecutar
  - Python 3.6 o superior
  - No requiere librerías externas (solo biblioteca estándar)

---

## Instrucciones de ejecución

### 1. Ejecutar la simulación completa
```
python main.py
```

### 2. Ejecutar las pruebas
```
python pruebas.py
```
