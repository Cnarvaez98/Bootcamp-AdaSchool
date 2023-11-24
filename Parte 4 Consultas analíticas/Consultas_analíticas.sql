-- Crear tablas
CREATE TABLE Categorias (
    id INTEGER PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE Productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    marca TEXT,
    categoria_id INTEGER,
    precio_unitario DECIMAL(10, 2),
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);

CREATE TABLE Sucursales (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    direccion TEXT
);

CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    telefono TEXT
);

CREATE TABLE Ordenes (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    sucursal_id INTEGER,
    fecha TEXT,
    total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (sucursal_id) REFERENCES Sucursales(id)
);

CREATE TABLE Stocks (
    id INTEGER PRIMARY KEY,
    sucursal_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (sucursal_id) REFERENCES Sucursales(id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);

CREATE TABLE Items (
    id INTEGER PRIMARY KEY,
    orden_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    monto_venta DECIMAL(10, 2),
    FOREIGN KEY (orden_id) REFERENCES Ordenes(id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);


