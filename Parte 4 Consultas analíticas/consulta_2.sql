SELECT s.id AS sucursal_id, 
       s.nombre AS sucursal_nombre, 
       SUM(st.cantidad) AS cantidad_total
FROM Sucursales s
JOIN Stocks st ON s.id = st.sucursal_id
GROUP BY s.id, s.nombre;