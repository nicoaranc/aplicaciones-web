from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import cross_origin
from utils.validations import *
from database import db
from werkzeug.utils import secure_filename
from PIL import Image
import hashlib
import filetype
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGHT'] = 16 * 1000 * 1000

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File exceeds the maximum file size allowed', 413


@app.route("/", methods=["GET"])
def index():
     if request.method == "GET":
        return render_template("index.html")
    

@app.route("/agregar-producto", methods=["GET", "POST"])
def agregarProducto():
    if request.method == "POST":
        nom_text = request.form.get("nombre")
        email_text =  request.form.get("email")
        tipo_text = request.form.get("tipo_producto")
        
        if tipo_text == 'Fruta':
            tipo_text = 'fruta'
            prod_text = request.form.getlist('fruit')

        elif tipo_text == 'Verdura':
            tipo_text = 'verdura'
            prod_text =  request.form.getlist('verd')  
        descrip_text = request.form.get("desc-producto")
        num_text = request.form.get("num")
        imgs_text = request.files.getlist("photo")
        reg_text = request.form.get("regiones")
        com_text = request.form.get("comunas")
        error = ""



        if validate_producto(nom_text, email_text, reg_text, com_text, tipo_text, prod_text, imgs_text, num_text):
            id_comuna = db.get_comuna_by_nombre(com_text)
            db.upload_producto(tipo_text, descrip_text, id_comuna[0], nom_text, email_text, num_text)
            prod = db.get_id_last_prod()
            prod_id = prod[0]

            for fruta_o_verdura in prod_text:
                elem = db.get_fruta_verdura_by_name(fruta_o_verdura)
                id_fruta_verd = elem[0]
                db.upload_frut_verd(prod_id, id_fruta_verd)

            for foto in imgs_text:

                sizes = [(120,120), (640, 480), (1280, 1024)]

                _filename = hashlib.sha256(
                    secure_filename(foto.filename) 
                    .encode("utf-8") 
                    ).hexdigest()
                _extension = filetype.guess(foto).extension
                img_filename = f"{_filename}.{_extension}"

                foto.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))                    

                ruta = f"uploads/{img_filename}" 

                db.upload_foto(ruta, img_filename, prod_id)

                img_filename = _filename

                ruta = "static/" + ruta


                for size in sizes:
                    nombre_archivo = img_filename + '_' + str(size[0]) + '_' + str(size[1]) + '.' + _extension
                    with Image.open(ruta) as img:
                        resized_img = img.resize(size)
                        resized_img.save(os.path.join(app.config["UPLOAD_FOLDER"], nombre_archivo))
            aviso = "El producto se subió exitosamente"
            return render_template("index.html", confirmacion = aviso)
        else:
            error += 'Uno de los campos no es valido'
        return render_template("agregar/agregar-producto.html", error = error)    
            
    elif request.method == "GET":
        return render_template("agregar/agregar-producto.html")

@app.route("/agregar-pedido", methods=["GET", "POST"])
def agregarPedido():
    if request.method == "POST":
        nom_text = request.form.get("nombre")
        email_text =  request.form.get("email")
        tipo_text = request.form.get("tipo_producto")
        
        if tipo_text == 'Fruta':
            tipo_text = 'fruta'
            prod_text = request.form.getlist('fruit')

        elif tipo_text == 'Verdura':
            tipo_text = 'verdura'
            prod_text =  request.form.getlist('verd')  
        descrip_text = request.form.get("desc-producto")
        num_text = request.form.get("num")
        reg_text = request.form.get("regiones")
        com_text = request.form.get("comunas")
        error = ""


        if validate_pedido(nom_text, email_text, reg_text, com_text, tipo_text, prod_text, num_text):
            id_comuna = db.get_comuna_by_nombre(com_text)
            db.upload_pedido(tipo_text, descrip_text, id_comuna[0], nom_text, email_text, num_text)
            prod = db.get_id_last_ped()
            prod_id = prod[0]

            for fruta_o_verdura in prod_text:
                elem = db.get_fruta_verdura_by_name(fruta_o_verdura)
                id_fruta_verd = elem[0]
                db.upload_frut_verd_ped(prod_id, id_fruta_verd)


            aviso = "El pedido se subió exitosamente"
            return render_template("index.html", confirmacion = aviso)
        else:
            error += 'Uno de los campos no es valido'
        return render_template("agregar/agregar-pedido.html", error = error)    
            
    elif request.method == "GET":
        return render_template("agregar/agregar-pedido.html")


@app.route("/ver-productos", methods=["GET", "POST"])
def verProductos():
    if request.method == "GET":
        data = []
        move = request.args.get('arg')
        pos = request.args.get('b')
        move = int(move)
        pos = int(pos)
        pos = pos + move
        cantidad = db.get_all_productos()[0]
        for prod in db.get_productos(pos):
            lista = []
            prod_id, prod_tipo, _, prod_comuna, _, _, _ = prod
            comuna, reg_id = db.get_comuna_by_id(prod_comuna)
            _, region = db.get_region_by_id(reg_id)
            elementos = db.get_elemen_by_prod(prod_id)
            for elemento in elementos:
                _, elem_id = elemento
                _, elem_nom = db.get_elem_by_id(elem_id)
                lista.append(elem_nom)
            
            fotos = db.get_foto_by_prod(prod_id)
            imagenes = []
            imagenes_orig = []
            for foto in fotos:
                _, ruta_arch, _, _ = foto
                imagenes_orig.append(url_for('static', filename=ruta_arch))


                find_ext = 0
                ext = ''
                for letra in ruta_arch:
                    if letra == '.':
                        find_ext = 1
                        ext += letra
                    else:
                        if find_ext:
                            ext += letra
                
                ruta_arch = str(ruta_arch)
                ruta_arch = ruta_arch.removesuffix(ext)

                
                ruta_arch+='_120_120'+ext
                imagenes.append(url_for('static', filename=ruta_arch))

            data.append({
                "id": prod_id,
                "tipo": prod_tipo,
                "productos": lista,
                "region": region,
                "comuna": comuna,
                "archivos": imagenes,
                "fuente": imagenes_orig
            })

    return render_template("ver/ver-productos.html", data=data, quantity= cantidad-pos-5, posit=pos)


@app.route("/ver-pedidos", methods=["GET", "POST"])
def verPedidos():
    if request.method == "GET":
        data = []
        move = request.args.get('arg')
        pos = request.args.get('b')
        move = int(move)
        pos = int(pos)
        pos = pos + move
        cantidad = db.get_all_pedidos()[0]
        for prod in db.get_pedidos(pos):
            lista = []
            prod_id, prod_tipo, _, prod_comuna, prod_nombre, _, _ = prod
            comuna, reg_id = db.get_comuna_by_id(prod_comuna)
            _, region = db.get_region_by_id(reg_id)
            elementos = db.get_elemen_by_ped(prod_id)
            for elemento in elementos:
                elem_id, _ = elemento
                _, elem_nom = db.get_elem_by_id(elem_id)
                lista.append(elem_nom)
            

            data.append({
                "id": prod_id,
                "tipo": prod_tipo,
                "productos": lista,
                "region": region,
                "comuna": comuna,
                "nombre": prod_nombre
            })

        return render_template("ver/ver-pedidos.html", data=data, quantity= cantidad-pos-5, posit=pos)

@app.route("/informacion-producto", methods=["GET", "POST"])
def infoProducto():
    if request.method == "POST":
        return redirect(url_for("index"))
    elif request.method == "GET":
        data = []
        lista = []
        fotos = []
        fotos_ = []
        id = request.args.get('id')
        elementos = db.get_elemen_by_prod(id)
        for elemento in elementos:
            _, elem_id = elemento
            _, elem_nom = db.get_elem_by_id(elem_id)
            lista.append(elem_nom)


        imagenes = db.get_foto_by_prod(id)
        for imagen in imagenes:
            _, ruta_arch, _, _ = imagen
            ruta_arch = "/static/" + ruta_arch
            find_ext = 0
            ext = ''
            for letra in ruta_arch:
                if letra == '.':
                    find_ext = 1
                    ext += letra
                else:
                    if find_ext:
                        ext += letra
            ruta_arch = str(ruta_arch)
            ruta_arch = ruta_arch.removesuffix(ext)
            ruta_arch2 = ruta_arch
            ruta_arch = ruta_arch + '_640_480' + ext
            ruta_arch2 = ruta_arch2 + '_1280_1024' + ext
            fotos.append(ruta_arch)
            fotos_.append(ruta_arch2)
        region = request.args.get('region')
        comuna = request.args.get('comuna')
        tipo = db.get_type_by_id(id)[0]
        descripcion = db.get_desc_by_id(id)[0]
        if descripcion == "":
            descripcion = "NO HAY DESCRIPCIÓN"
        nombre = db.get_name_by_id(id)[0]
        email = db.get_email_by_id(id)[0]
        celular = db.get_num_by_id(id)[0]
        if celular == "":
            celular = "CELULAR NO REGISTRADO"
        data.append({
            "tipo": tipo,
            "productos": lista,
            "descripcion": descripcion,
            "region": region,
            "comuna": comuna,
            "vendedor": nombre,
            "email": email,
            "celular": celular,
            "fotos": fotos,
            "fotos_": fotos_
        })
        return render_template("informacion/informacion-producto.html", data=data)

@app.route("/informacion-pedido", methods=["GET", "POST"])
def infoPedido():
    if request.method == "POST":
        return redirect(url_for("index"))
    elif request.method == "GET":
        data = []
        lista = []
        id = request.args.get('id')
        elementos = db.get_elemen_by_ped(id)
        for elemento in elementos:
            elem_id, _ = elemento
            _, elem_nom = db.get_elem_by_id(elem_id)
            lista.append(elem_nom)
        region = request.args.get('region')
        comuna = request.args.get('comuna')
        nombre = request.args.get('nombre')
        tipo = db.get_type_by_id_ped(id)[0]
        descripcion = db.get_desc_by_id_ped(id)[0]
        if descripcion is None:
            descripcion = "NO HAY DESCRIPCIÓN"
        
        email = db.get_email_by_id_ped(id)[0]
        celular = db.get_num_by_id_ped(id)[0]
        if celular == "":
            celular = "CELULAR NO REGISTRADO"
        data.append({
            "tipo": tipo,
            "productos": lista,
            "descripcion": descripcion,
            "region": region,
            "comuna": comuna,
            "vendedor": nombre,
            "email": email,
            "celular": celular,
        })
        return render_template("informacion/informacion-pedido.html", data=data)

@app.route("/estadisticas", methods = ["GET"])
def verEstadisticas():
    if request.method == "GET":
        return render_template("charts.html")
    
@app.route("/get-estadisticas", methods = ["GET"])
@cross_origin(origin="localhost", supports_credential=True)
def getCharts():

    productos = db.get_prod_by_type()
    data_productos = [{
        "tipo": producto[0],
        "count": producto[1]
    } for producto in productos]


    pedidos = db.get_ped_by_comuna()
    data_pedidos = [{
        "comuna": pedido[0],
        "count" : pedido[1]
    } for pedido in pedidos]

    data = [data_productos, data_pedidos]

    print(data)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)