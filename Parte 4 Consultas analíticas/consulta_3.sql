SELECT c.id AS cliente_id, 
       c.nombre AS cliente_nombre, 
       SUM(i.monto_venta) AS total_ventas
FROM Clientes c
JOIN Ordenes o ON c.id = o.cliente_id
JOIN Items i ON o.id = i.orden_id
GROUP BY c.id, c.nombre;