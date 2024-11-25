const info = () => {
    window.location.href = "../html/informacion-pedido.html";
}

// const menuInicial = () => {
//     window.location.href = "../html/index.html";
// }

const regresarMenu = document.getElementById("boton-regreso");
regresarMenu.addEventListener("click", menuInicial);