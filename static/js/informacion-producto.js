const mostrar = (ruta) => {

    
    const modal = document.getElementById("mod");
    
    let find_ext = 0;
    let ext = '_640_480';
    for (var i = 0; i < ruta.length; i++){
        if (ruta[i] == "."){
            find_ext = 1;
            ext += ".";
        }
        else{
            if (find_ext == 1){
                ext += ruta[i];
            } 
        }
    }
    let ex2 = ext.replace('_640_480', '')
    let ruta2 = ruta.replace(ext, '');
    ruta2 += "_1280_1024" + ex2

    const imagen = document.createElement("img");
    
    // imagen.alt = "imagen";
    
    imagen.setAttribute("src", ruta2)
    imagen.setAttribute("alt", "producto")
    imagen.setAttribute("onclick", "destroy()")
    imagen.setAttribute("id", "imagen_grande")
    modal.appendChild(imagen)
    
    modal.style = 'display:contents'
    
    const info = document.getElementById("data")
    info.style = 'display:none'
}

const destroy = () => {
    const info = document.getElementById("data")
    info.style = 'display:contents'
    const modal = document.getElementById("mod");
    imagen = document.getElementById("imagen_grande")
    modal.removeChild(imagen)
    modal.style = 'display:none'
    
}


// const selectRegion = document.getElementById("regiones");
// const opcion = document.createElement("option");
// opcion.text = regiones[valor];
// opcion.value = regiones[valor];
// selectRegion.add(opcion);

// const mostrar = () => {
//     foto.style = 'display: none';
//     grande.style = 'display: flex';
// }

// const boton = document.getElementById("boton");
// boton.addEventListener("click", mostrar);

// const foto = document.getElementById("img");
// const grande = document.getElementById("img2");

// const menuInicial = () => {
//     window.location.href = "../html/index.html";
// }

// const regresarMenu = document.getElementById("boton-regreso");
// regresarMenu.addEventListener("click", menuInicial);
