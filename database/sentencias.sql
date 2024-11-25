-- Producto
-- insertar producto
INSERT INTO producto (tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor) VALUES (?,?,?,?,?,?)
-- obtener listado de productos ordenados desde el mas reciente insertado al más antiguo
SELECT id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor FROM producto ORDER BY id DESC
-- obtener listado de productos ordenados desde el mas reciente insertado al más antiguo limitado
-- a los primeros 5
SELECT id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor FROM producto ORDER BY id DESC LIMIT 0, 5
-- idem anterior, pero los siguientes 5 (siguiente página)
SELECT id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor FROM producto ORDER BY id DESC LIMIT 5, 5
-- idem anterior pero obteniendo el nombre de comuna en lugar de ID
SELECT PRO.id, PRO.tipo, PRO.descripcion, COM.nombre, PRO.nombre_productor, PRO.email_productor, PRO.celular_productor FROM producto PRO, comuna COM WHERE PRO.comuna_id = COM.id ORDER BY id DESC LIMIT 5, 5

-- producto_verdura_tipo
-- insertar
INSERT INTO producto_verdura_fruta (producto_id, tipo_verdura_fruta_id) VALUES (?,?)
-- obtener los tipos asociados a un producto
SELECT TVF.nombre FROM tipo_verdura_fruta TVF, producto_verdura_fruta PVF WHERE TVF.id=PVF.tipo_verdura_fruta_id AND PVF.producto_id=?

-- foto
-- insertar
INSERT INTO foto (ruta_archivo, nombre_archivo, producto_id) VALUES (?,?,?)
-- obtener fotos informadas para un producto
SELECT ruta_archivo, nombre_archivo FROM foto WHERE producto_id=?

-- obtener el último id insertado
SELECT LAST_INSERT_ID()