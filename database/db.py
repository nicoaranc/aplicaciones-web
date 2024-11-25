import pymysql
import json

DB_NAME = 'tarea2'
DB_USERNAME = 'cc5002'
DB_PASSWORD = 'programacionweb'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_CHARSET = 'utf8'

with open('database/querys.json', 'r') as querys:
    QUERY_DICT = json.load(querys)

def get_conn():
    conn = pymysql.connect(
        db=DB_NAME,
        user=DB_USERNAME,
        passwd=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        charset=DB_CHARSET
    )
    return conn

def get_region_by_nombre(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM region WHERE nombre=%s;", nombre)
    user = cursor.fetchone()
    return user

def get_comuna_by_nombre(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, region_id FROM comuna WHERE nombre=%s;", nombre)
    user = cursor.fetchone()
    return user    


def get_productos(inicio):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto ORDER BY id DESC LIMIT %s, 5;"%inicio)
    productos = cursor.fetchall()
    return productos

def get_pedidos(inicio):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedido ORDER BY id DESC LIMIT %s, 5;"%inicio)
    pedidos = cursor.fetchall()
    return pedidos

def get_all_productos():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM producto;")
    cantidad = cursor.fetchone()
    return cantidad

def get_all_pedidos():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedido;")
    cantidad = cursor.fetchone()
    return cantidad

def get_comuna_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, region_id FROM comuna WHERE id=%s;", id)
    user = cursor.fetchone()
    return user    

def get_region_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM region WHERE id=%s;", id)
    user = cursor.fetchone()
    return user     

def get_elemen_by_prod(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto_verdura_fruta WHERE producto_id=%s", id)
    user = cursor.fetchall()
    return user

def get_elemen_by_ped(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedido_verdura_fruta WHERE pedido_id=%s", id)
    user = cursor.fetchall()
    return user

def get_foto_by_prod(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM foto WHERE producto_id=%s", id)
    user = cursor.fetchall()
    return user

def get_fruta_verdura_by_name(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipo_verdura_fruta WHERE nombre = %s", nombre)
    user = cursor.fetchone()
    return user

def get_id_last_prod():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id from producto ORDER BY id DESC LIMIT 1")
    user = cursor.fetchone()
    return user

def get_id_last_ped():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id from pedido ORDER BY id DESC LIMIT 1")
    user = cursor.fetchone()
    return user

def get_elem_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipo_verdura_fruta WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_desc_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT descripcion FROM producto WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_desc_by_id_ped(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT descripcion FROM pedido WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_type_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM producto WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_type_by_id_ped(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM pedido WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_name_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_productor FROM producto WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_email_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT email_productor FROM producto WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_email_by_id_ped(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT email_comprador FROM pedido WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_num_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT celular_productor FROM producto WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def get_num_by_id_ped(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT celular_comprador FROM pedido WHERE id=%s", id)
    user = cursor.fetchone()
    return user

def upload_producto(tipo, descripcion, comuna, nombre, email, celular):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["upload_producto"], (tipo, descripcion, comuna, nombre, email, celular))
    conn.commit()

def upload_frut_verd(prod_id, frut_verd_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO producto_verdura_fruta (producto_id, tipo_verdura_fruta_id) VALUES (%s, %s);", (prod_id, frut_verd_id))
    conn.commit()

def upload_foto(ruta, nombre, id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["upload_foto"], (ruta, nombre, id))
    conn.commit()

def upload_pedido(tipo, descripcion, comuna, nombre, email, celular):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["upload_pedido"], (tipo, descripcion, comuna, nombre, email, celular))
    conn.commit()

def upload_frut_verd_ped(ped_id, frut_verd_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedido_verdura_fruta (tipo_verdura_fruta_id, pedido_id) VALUES (%s, %s);", (frut_verd_id, ped_id))
    conn.commit()

def get_prod_by_type():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT b.nombre AS Nombre, COUNT(*) AS Conteo FROM producto_verdura_fruta a JOIN tipo_verdura_fruta b WHERE b.id = a.tipo_verdura_fruta_id GROUP BY b.nombre")
    user = cursor.fetchall()
    return user

def get_ped_by_comuna():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT a.nombre AS Comuna, COUNT(*) AS Conteo FROM comuna a JOIN pedido b WHERE b.comuna_id = a.id GROUP BY a.nombre")
    user = cursor.fetchall()
    return user