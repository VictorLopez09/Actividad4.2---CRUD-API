from fastapi import FastAPI

app = FastAPI()

# Lista con un producto inicial
productos = [
    {
        "id": 1,
        "nombre": "Martillo",
        "precio": 10.5,
        "stock": 20,
        "proveedor": "Truper",
        "categoria": "Herramientas"
    },
    {
        "id": 2,
        "nombre": "Destornillador",
        "precio": 5.0,
        "stock": 50,
        "proveedor": "Stanley",
        "categoria": "Herramientas"
    },
    {
        "id": 3,
        "nombre": "Pintura Blanca",
        "precio": 15.75,
        "stock": 30,
        "proveedor": "Comex",
        "categoria": "Pinturas"
    },
    {
        "id": 4,
        "nombre": "Clavos",
        "precio": 2.3,
        "stock": 200,
        "proveedor": "Truper",
        "categoria": "Fijaciones"
    },
    {
        "id": 5,
        "nombre": "Cinta Métrica",
        "precio": 8.0,
        "stock": 40,
        "proveedor": "Stanley",
        "categoria": "Herramientas"
    }
]

# Obtener todos los productos


@app.get("/productos/")
def obtener_productos():
    return productos

# Obtener un producto por ID


@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto
    return {"error": "Producto no encontrado"}

# Agregar un nuevo producto


@app.post("/productos/")
def crear_producto(producto: dict):
    productos.append(producto)
    return producto

# Eliminar un producto


@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    global productos
    productos = [p for p in productos if p["id"] != producto_id]
    return {"mensaje": "Producto eliminado"}
