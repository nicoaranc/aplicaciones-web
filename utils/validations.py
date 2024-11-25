import re
import filetype
from database import db


def validate_prod_img(prod_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if prod_img is None:
        return False


    # check if the browser submitted an empty file
    if prod_img.filename == "":
        return False  
    # check file extension
    ftype_guess = filetype.guess(prod_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
        
    return True

def validate_imagenes(imagenes):
    for imagen in imagenes:
        if not validate_prod_img(imagen):
            return False
    return True

def validate_tipo(tipo):
    ALLOWED_TYPES = {"fruta", "verdura"}
    if tipo is None:
        return False
    
    if tipo not in ALLOWED_TYPES:
        return False
    
    return True

def validate_frut_verd(productos): 
    for frut_verd in productos:
        if not db.get_fruta_verdura_by_name(frut_verd):
            return False
    return True


def validate_region(region):

    if region is None:
        return False
    
    reg = db.get_region_by_nombre(region)

    if not reg:
        return False
    
    return True

def validate_comuna(region, comuna):

    if comuna is None or region is None:
        return False
    
    reg = db.get_region_by_nombre(region)
    if not reg:
        return False
    
    com = db.get_comuna_by_nombre(comuna)
    if not com:
        return False
    
    if com[2] != reg[0]:
        return False

    return True

def validate_nombre(nombre):
    return nombre and (len(nombre) > 2 and len(nombre) < 81)

def validate_email(email):
    return "@" in email

def validate_num(numero):
    if numero is None:
        return True
    else:
        if len(numero) < 16:
            return True
        else:
            return False

def validate_producto(nombre, email, region, comuna, tipo, producto, imagenes, numero):
    nom = validate_nombre(nombre)
    em = validate_email(email)
    reg = validate_region(region)
    com = validate_comuna(region, comuna)
    tip = validate_tipo(tipo)
    prod = validate_frut_verd(producto)
    img = validate_imagenes(imagenes)
    num = validate_num(numero)
    return nom and em and reg and com and tip and img and prod and num

def validate_pedido(nombre, email, region, comuna, tipo, producto, numero):
    nom = validate_nombre(nombre)
    em = validate_email(email)
    reg = validate_region(region)
    com = validate_comuna(region, comuna)
    tip = validate_tipo(tipo)
    prod = validate_frut_verd(producto)
    num = validate_num(numero)
    return nom and em and reg and com and tip and prod and num
