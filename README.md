# 📝 CRUD de Productos con FastAPI

Un API simple para gestionar productos de ferretería, implementando operaciones CRUD (Create, Read, Update, Delete) usando **FastAPI**.

---

## 🚀 Características
- **Endpoints RESTful** para gestionar productos.
- **Operaciones básicas**:
  - Obtener todos los productos.
  - Obtener un producto por ID.
  - Crear un nuevo producto.
  - Actualizar un producto existente.
  - Eliminar un producto.
- Datos almacenados en memoria (lista de diccionarios).

---

## 📌 Endpoints

| Método | Ruta                | Descripción                          |
|--------|---------------------|--------------------------------------|
| GET    | `/productos/`       | Obtener todos los productos.         |
| GET    | `/productos/{id}`   | Obtener un producto por ID.          |
| POST   | `/productos/`       | Crear un nuevo producto.             |
| PUT    | `/productos/{id}`   | Actualizar un producto existente.    |
| DELETE | `/productos/{id}`   | Eliminar un producto.                |

---

## 🛠 Ejemplos de Uso

### 1. Obtener todos los productos
```bash
curl -X GET http://127.0.0.1:8000/productos/
```

### 2. Obtener un producto por ID
```bash
curl -X GET http://127.0.0.1:8000/productos/1
```
### 3. Crear un nuevo producto
```bash
curl -X POST http://127.0.0.1:8000/productos/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 6,
    "nombre": "Llave Inglesa",
    "precio": 12.99,
    "stock": 25,
    "proveedor": "Truper",
    "categoria": "Herramientas"
  }'
```
### 4. Actualizar un producto
```bash
curl -X PUT http://127.0.0.1:8000/productos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "precio": 11.99,
    "stock": 15
  }'
```
### 5. Eliminar un producto
```bash
curl -X DELETE http://127.0.0.1:8000/productos/1
```

## ⚙️ Requisitos e Instalación

1. Python 3.7+

2. Instalar FastAPI y Uvicorn:

```bash
pip install fastapi uvicorn
```
3. Ejecutar la aplicación:

```bash
uvicorn main:app --reload
```
4. Documentación interactiva:

```bash
Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc
```

## 📂 Estructura del Proyecto
```text
fastapi-crud/
├── main.py          # Código principal del API
├── README.md        # Documentación
└── requirements.txt # Dependencias (FastAPI, Uvicorn)
```
## 📜 Notas
Los datos se guardan en memoria (se pierden al reiniciar el servidor).

Para producción, considera usar una base de datos (SQLite, PostgreSQL, etc.).

## LICENSE

MIT License

