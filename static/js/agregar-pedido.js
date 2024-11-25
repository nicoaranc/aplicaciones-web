// --- Validation ---

const validateEmail = email => {
    const emailFormat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailFormat.test(email);
};

const validateProducerName = prodName => {
    return prodName && (prodName.length > 2 && prodName.length < 81);
};

const validateTipoProducto = tipo => {
    return tipo == "Fruta" || tipo == "Verdura";
};


const validateProductos = numero => {
    return numero > 0 && numero < 6;
}

const validateRegion = reg => {
    return regiones.includes(reg);
}

let validateTipo = false;

// --- ---


// --- Display options ---
const displayFrutas = () => {
    document.querySelectorAll("input[name='verd']:checked").forEach(verd => verd.checked = false)     
    document.getElementById("frutas").style = 'display:contents';
    document.getElementById("verduras").style = 'display:none';
    validateTipo = true;
};

const displayVerduras = () => {
    document.querySelectorAll("input[name='fruit']:checked").forEach(fruit => fruit.checked = false)
    document.getElementById("frutas").style = 'display:none';
    document.getElementById("verduras").style = 'display:contents';
    validateTipo = true;
};

const selectFrutas = document.getElementById("fruta");
selectFrutas.addEventListener("click", displayFrutas);

const selectVerduras = document.getElementById("verdura");
selectVerduras.addEventListener("click", displayVerduras);


const cargar = () => {
    cargarRegiones();
}

let regiones = ["Región Arica y Parinacota", "Región de Tarapacá", "Región de Antofagasta",
                "Región de Atacama", "Región de Coquimbo", "Región de Valparaíso", "Región Metropolitana de Santiago",
                "Región del Libertador Bernardo Ohiggins", "Región del Maule", "Región del Ñuble", "Región del Biobío",
                "Región de La Araucanía", "Región de Los Ríos", "Región de Los Lagos",
                "Región Aisén del General Carlos Ibáñez del Campo", "Región de Magallanes y la Antártica Chilena"];

const cargarRegiones = () => {
    const selectRegion = document.getElementById("regiones");

    for (valor in regiones) {
        const opcion = document.createElement("option");
        opcion.text = regiones[valor];
        opcion.value = regiones[valor];
        selectRegion.add(opcion);
    }
}

const cargarComunas = () => {

    const selectComuna = document.getElementById("comunas")
    const largo = selectComuna.length;
    for (i = 1; i <= largo; i++){
        selectComuna[0] = null
    }

    const reg = document.getElementById("regiones").value

    if (reg == "Región Arica y Parinacota"){
        for (valor in arica){
            const opcion = document.createElement("option");
            opcion.text = arica[valor];
            opcion.value = arica[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región de Tarapacá"){
        for (valor in tarapaca){
            const opcion = document.createElement("option");
            opcion.text = tarapaca[valor];
            opcion.value = tarapaca[valor];
            selectComuna.add(opcion);
        }
    }

    if (reg == "Región de Antofagasta"){
        for (valor in antofagasta){
            const opcion = document.createElement("option");
            opcion.text = antofagasta[valor];
            opcion.value = antofagasta[valor];
            selectComuna.add(opcion);
        }
    }

    if (reg == "Región de Atacama"){
        for (valor in atacama){
            const opcion = document.createElement("option");
            opcion.text = atacama[valor];
            opcion.value = atacama[valor];
            selectComuna.add(opcion);
        }
    }

    if (reg == "Región de Coquimbo"){
        for (valor in coquimbo){
            const opcion = document.createElement("option");
            opcion.text = coquimbo[valor];
            opcion.value = coquimbo[valor];
            selectComuna.add(opcion);
        }
    }

    if (reg == "Región de Valparaíso"){
        for (valor in valparaiso){
            const opcion = document.createElement("option");
            opcion.text = valparaiso[valor];
            opcion.value = valparaiso[valor];
            selectComuna.add(opcion);
        }
    }

    if (reg == "Región Metropolitana de Santiago"){
        for (valor in metropolitana){
            const opcion = document.createElement("option");
            opcion.text = metropolitana[valor];
            opcion.value = metropolitana[valor];
            selectComuna.add(opcion);
        }
    }

    if (reg == "Región del Libertador Bernardo Ohiggins"){
        for (valor in ohiggins){
            const opcion = document.createElement("option");
            opcion.text = ohiggins[valor];
            opcion.value = ohiggins[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región del Maule"){
        for (valor in maule){
            const opcion = document.createElement("option");
            opcion.text = maule[valor];
            opcion.value = maule[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región del Ñuble"){
        for (valor in nuble){
            const opcion = document.createElement("option");
            opcion.text = nuble[valor];
            opcion.value = nuble[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región del Biobío"){
        for (valor in biobio){
            const opcion = document.createElement("option");
            opcion.text = biobio[valor];
            opcion.value = biobio[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región de La Araucanía"){
        for (valor in araucania){
            const opcion = document.createElement("option");
            opcion.text = araucania[valor];
            opcion.value = araucania[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región de Los Ríos"){
        for (valor in rios){
            const opcion = document.createElement("option");
            opcion.text = rios[valor];
            opcion.value = rios[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región de Los Lagos"){
        for (valor in lagos){
            const opcion = document.createElement("option");
            opcion.text = lagos[valor];
            opcion.value = lagos[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región Aisén del General Carlos Ibáñez del Campo"){
        for (valor in aysen){
            const opcion = document.createElement("option");
            opcion.text = aysen[valor];
            opcion.value = aysen[valor];
            selectComuna.add(opcion);
        }
    }
    if (reg == "Región de Magallanes y la Antártica Chilena"){
        for (valor in magallanes){
            const opcion = document.createElement("option");
            opcion.text = magallanes[valor];
            opcion.value = magallanes[valor];
            selectComuna.add(opcion);
        }
    }
}

const elegirRegion = document.getElementById("regiones");
elegirRegion.addEventListener("change", cargarComunas);


let arica = ["Arica", "Gral. Lagos", "Camarones", "Putre"];

let tarapaca = ["Alto Hospicio", "Iquique", "Camiña", "Colchane", "Huara", "Pica", "Pozo Almonte"];

let antofagasta = ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollague",
                    "San Pedro Atacama", "Maria Elena", "Tocopilla"];

let atacama = ["Chañaral", "Diego de Almagro", "Caldera", "Copiapo", "Tierra Amarilla", "Alto del Carmen",
                "Freirina", "Huasco", "Vallenar"];

let coquimbo = ["La Higuera", "La Serena", "Vicuña", "Paihuano", "Coquimbo", "Andacollo", "Rio Hurtado", 
                "Ovalle", "Monte Patria", "Punitaqui", "Combarbala", "Mincha", "Illapel", "Salamanca", "Los Vilos"];

let valparaiso = ["Petorca", "Cabildo", "Papudo", "La Ligua", "Zapallar", "Putaendo", "Santa Maria", "San Felipe", 
                    "Pencahue", "Catemu", "Llay Llay", "Nogales", "La Calera", "Hijuelas", "La Cruz", "Quillota",
                    "Olmue", "Limache", "Los Andes", "Rinconada", "Calle Larga", "San Esteban", "Puchuncavi", 
                    "Quintero", "Viña del Mar", "Villa Alemana", "Quilpue", "Valparaiso", "Juan Fernandez", 
                    "Casablanca", "Concon", "Isla de Pascua", "Algarrobo", "El Quisco", "El Tabo", "Cartagena", 
                    "San Antonio", "Santo Domingo"];

let metropolitana = ["Tiltil", "Colina", "Lampa", "Conchali", "Quilicura", "Renca", "Las Condes", "Pudahuel", 
                    "Quinta Normal", "Providencia", "Santiago", "La Reina", "Ñuñoa", "San Miguel", "Maipú", 
                    "La Cisterna", "La Florida", "La Granja", "Independencia", "Huechuraba", "Recoleta", "Vitacura", 
                    "Lo Barrenechea", "Macul", "Peñalolén", "San Joaquín", "La Pintana", "San Ramon", "El Bosque", 
                    "Pedro Aguirre Cerda", "Lo Espejo", "Estacion Central", "Cerrillos", "Lo Prado", "Cerro Navia", 
                    "San José de Maipo", "Puente Alto", "Pirque", "San Bernardo", "Calera de Tango", "Buin", "Paine", 
                    "Peñaflor", "Talagante", "El Monte", "Isla de Maipo", "Curacavi", "María Pinto", "Melipilla", 
                    "San Pedro", "Alhué", "Padre Hurtado"];

let ohiggins = ["Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machali", "Malloa",
                "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta Tilcoco", "Rancagua", "Rengo",
                "Requinoa", "San Vicente", "La Estrella", "Litueche", "Marchigue", "Navidad",
                "Paredones", "Pichilemu", "Chepica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla",
                "Peralillo", "Placilla", "Pumanque", "San Fernando", "Santa Cruz"];

let maule = ["Cauquenes", "Chanco", "Pelluhue", "Curico", "Hualañe", "Licanten", "Molina", "Rauco", "Romeral",
                "Sagrada Familia", "Teno", "Vichuquen", "Colbun", "Linares", "Longavi", "Parral", "Retiro",
                "San Javier", "Villa Alegre", "Yerbas Buenas", "Constitucion", "Curepto", "Empedrado",
                "Maule", "Pelarco", "Pencahue", "Rio Claro", "San Clemente", "San Rafael", "Talca"];

let nuble = ["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ranquil", "Trehuaco", "Bulnes",
                "Chillan Viejo", "Chillan", "El Carmen", "Pemuco", "Pinto", "Quillon", "San Ignacio", "Yungay",
                "Coihueco", "Ñiquen", "San Carlos", "San Fabian", "San Nicolas"];

let biobio = ['Tome', 'Florida', 'Penco', 'Talcahuano', 'Concepcion', 'Hualqui', 'Coronel', 'Lota', 'Santa Juana',
                'Chiguayante', 'San Pedro de la Paz', 'Hualpen', 'Cabrero', 'Yumbel', 'Tucapel', 'Antuco', 'San Rosendo',
                'Laja', 'Quilleco', 'Los Angeles', 'Nacimiento', 'Negrete', 'Santa Barbara', 'Quilaco', 'Mulchen',
                 'Alto Bio Bio', 'Arauco', 'Curanilahue', 'Los Alamos', 'Lebu', 'Cañete', 'Contulmo', 'Tirua'];

let araucania = ['Renaico', 'Angol', 'Collipulli', 'Los Sauces', 'Puren', 'Ercilla', 'Lumaco', 'Victoria', 'Traiguen',
                 'Curacautin', 'Lonquimay', 'Perquenco', 'Galvarino', 'Lautaro', 'Vilcun', 'Temuco', 'Carahue',
                 'Melipeuco', 'Nueva Imperial', 'Puerto Saavedra', 'Cunco', 'Freire', 'Pitrufquen', 'Teodoro Schmidt',
                 'Gorbea', 'Pucon', 'Villarrica', 'Tolten', 'Curarrehue', 'Loncoche', 'Padre Las Casas', 'Cholchol'];

let rios = ["Mariquina", "Lanco", "Mafil", "Valdivia", "Corral", "Paillaco", "Los Lagos", "Panguipulli",
            "La Union", "Rio Bueno", "Lago Ranco", "Futrono"];

let lagos = ['San Pablo', 'San Juan', 'Osorno', 'Puyehue', 'Rio Negro', 'Purranque', 'Puerto Octay', 'Frutillar',
            'Fresia', 'Llanquihue', 'Puerto Varas', 'Los Muermos', 'Puerto Montt', 'Maullin', 'Calbuco', 'Cochamo',
            'Ancud', 'Quemchi', 'Dalcahue', 'Curaco de Velez', 'Castro', 'Chonchi', 'Queilen', 'Quellon', 'Quinchao',
            'Puqueldon', 'Chaiten', 'Futaleufu', 'Palena', 'Hualaihue'];

let aysen = ["Aysen", "Cisnes", "Guaitecas", "Cochrane", "O'Higins", "Tortel", "Coyhaique", "Lago Verde",
                "Chile Chico", "Río Iba?ez"];

let magallanes = ["Antartica", "Laguna Blaca", "Punta Arenas", "Rio Verde", "San Gregorio",
                    "Porvenir", "Primavera", "Timaukel", "Puerto Natales", "Torres del Paine"];

let comunas = arica + tarapaca + antofagasta + atacama + coquimbo + valparaiso + metropolitana +
                ohiggins + maule + nuble + biobio + araucania + rios + lagos + aysen + magallanes;
/// --- Subir productos ---

const mod1 = document.getElementById("mod1"); 
const mod2 = document.getElementById("mod2"); 

const subir = () => {

    console.log("Validando envío...")

    let errores = "";
    let puede = true;

    if (!validateTipo){
        errores += "Se debe elegir un tipo de producto. \n";
        puede = false;
    }

    else if (validateTipo){
        const tipo_de_productos = document.querySelector('input[name="tipo_producto"]:checked').value
        if (!validateTipoProducto(tipo_de_productos)){
            errores += "Se debe elegir entre Fruta o Verdura. \n";
            puede = false;
        }
    }    

    const numero = document.querySelectorAll('input:checked').length - 1;
    if (!validateProductos(numero)){
        errores += "Se deben elegir entre 1 y 5 productos. \n";
        puede = false;
    }

    const region = document.getElementById("regiones").value
    if (!validateRegion(region)){
        errores += "Se debe seleccionar una región valida. \n";
        puede = false;
        errores += "Se debe seleccionar una comuna valida. \n";
    }

    const nombreCom = document.getElementById("nombre").value;
    if (!validateProducerName(nombreCom)) {
        errores += "El nombre debe tener un largo mínimo 3 y máximo 80. \n";
        puede = false;
    }

    const emailCom = document.getElementById("email").value;
    if (!validateEmail(emailCom)) {
        errores += "El email debe tener el formato correcto (xxxxxxxxx@xxxx.xxxx). \n";
        puede = false;
    }


    if (!puede){
        alert(errores);
    }


    else{
        mod1.style = 'display: block';
        const desconfirmacion = document.getElementById("desconfirmar");
        desconfirmacion.addEventListener("click", volverForm);
        const confirmacion = document.getElementById("confirmar");
        confirmacion.addEventListener("click", agregado);
    }

}

const volverForm = () => {
    mod1.style = 'display: none';
}

const agregado = () => {
    mod1.style = 'display: none';
    mod2.style = 'display: block';
    const menu = document.getElementById("volver");
    menu.addEventListener("click", menuInicial);
    
}

// const menuInicial = () => {
//     window.location.href = "../html/index.html";
// }



const subirProducto = document.getElementById("agregar");
subirProducto.addEventListener("click", subir);

// const regresarMenu = document.getElementById("boton-regreso");
// regresarMenu.addEventListener("click", menuInicial);