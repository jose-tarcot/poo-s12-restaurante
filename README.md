# restaurante_app — Semana 12

**Estudiante:** José Alberto Tarco Tipán
**Materia:** Programación Orientada a Objetos
**Institución:** Universidad Estatal Amazónica
**Entrega:** Semana 12 — Organización modular con colecciones orientadas al rendimiento

---

## 1. Descripción general

Esta entrega continúa el proyecto `restaurante_app` iniciado en semanas anteriores. El sistema gestiona el menú (productos con tiempo de preparación), clientes por mesa y operaciones de pedido. En la Semana 12 no se agregan nuevas funcionalidades: el objetivo es **mejorar internamente la forma en que el sistema busca, consulta y valida información**, incorporando estructuras auxiliares en memoria que evitan recorrer las listas completas en operaciones frecuentes.

---

## 2. Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py          ← único archivo modificado en Semana 12
├── main.py
└── README.md
```

---

## 3. Mejoras aplicadas en Semana 12

Todos los cambios se realizaron exclusivamente en `servicios/restaurante.py`.

### Índice de productos por código — `dict[str, Producto]`

`buscar_producto()` antes recorría toda la lista con un `for` hasta encontrar el código. Ahora usa `_productos_por_codigo.get(codigo)`, acceso directo en O(1). El índice se actualiza al registrar o eliminar un producto, y se reconstruye desde JSON al iniciar el programa.

### Índice de usuarios por identificación — `dict[str, Usuario]`

`buscar_usuario()` antes recorría `_usuarios` completa. Ahora usa `_usuarios_por_identificacion.get(identificacion)` en O(1). Útil especialmente para validar la mesa del cliente antes de procesar un pedido.

### Índice de ventas por usuario — `dict[str, list[Venta]]`

`consultar_ventas_usuario()` antes filtraba toda `_ventas` con un bucle. Ahora accede directamente a la lista de ventas del usuario mediante `_ventas_por_usuario.get(id)` en O(1). El índice se actualiza al registrar cada pedido.

### Set de categorías activas — `set[str]`

`_categorias_activas` se mantiene actualizado al registrar, actualizar o eliminar productos. `obtener_categorias_registradas()` devuelve su copia sin necesidad de reconstruirlo en cada consulta.

### Reconstrucción de índices al iniciar

El método `_reconstruir_indices()` se invoca en `__init__` tras cargar los datos desde JSON, garantizando que los índices reflejen el estado persistido desde la sesión anterior.

---

## 4. Colecciones utilizadas y su responsabilidad

| Colección | Tipo | Responsabilidad |
|---|---|---|
| `_productos` | `list` | Almacenar, recorrer en orden y persistir productos |
| `_usuarios` | `list` | Almacenar, recorrer en orden y persistir usuarios |
| `_ventas` | `list` | Almacenar, recorrer en orden y persistir pedidos |
| `_productos_por_codigo` | `dict` | Búsqueda rápida de producto por código |
| `_usuarios_por_identificacion` | `dict` | Búsqueda rápida de cliente por identificación |
| `_ventas_por_usuario` | `dict` | Consulta rápida de pedidos por cliente |
| `_categorias_activas` | `set` | Categorías únicas activas; validación de pertenencia |

---

## 5. Ejecución

```bash
cd restaurante_app
python main.py
```

Requiere **Python 3.10 o superior**.

---

## 6. Pruebas realizadas

**Búsqueda por código:** se registró un producto de parrilla con tiempo de preparación y se buscó por su código. El índice respondió directamente sin recorrer la lista.

**Búsqueda de cliente por mesa:** se buscó un cliente registrado por su identificación; el índice devolvió el objeto en O(1).

**Consulta de pedidos por usuario:** se realizaron dos pedidos para el mismo cliente y se consultaron sus ventas; el índice devolvió solo sus registros sin filtrar toda la colección.

**Sincronización tras eliminar:** se eliminó un producto y se verificó que el dict y el set de categorías quedaron coherentes con la lista principal.

**Reconstrucción desde JSON:** tras cerrar y reabrir el programa, los índices se reconstruyeron correctamente desde los tres archivos JSON y todas las búsquedas respondieron como se esperaba.
