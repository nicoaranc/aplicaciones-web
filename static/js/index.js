




// --- Functions that redirect to different pages ---

const redirectAgregarProducto = () => {
    window.location.href = "../html/agregar-producto.html";
}

const redirectVerProductos = () => {
    window.location.href = "../html/ver-productos.html";
}

const redirectAgregarPedido = () => {
    window.location.href = "../html/agregar-pedido.html";
}

const redirectVerPedidos = () => {
    window.location.href = "../html/ver-pedidos.html";
}

// --- Event listeners ---

const agregarProductoPageButton = document.getElementById("agregar-producto-page");
agregarProductoPageButton.addEventListener("click", redirectAgregarProducto);

const verProductosPageButton = document.getElementById("productos-page");
verProductosPageButton.addEventListener("click", redirectVerProductos);

const agregarPedidoPageButton = document.getElementById("agregar-pedido-page");
agregarPedidoPageButton.addEventListener("click", redirectAgregarPedido);

const verPedidosPageButton = document.getElementById("pedidos-page");
verPedidosPageButton.addEventListener("click", redirectVerPedidos);