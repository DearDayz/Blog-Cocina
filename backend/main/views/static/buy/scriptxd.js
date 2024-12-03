
//ver si esta abriendo el script
console.log("script.js cargado");
console.log("HOLAAAA")

window.addEventListener('load', function() {
    // Mostrar el modal automáticamente cuando la página se carga
    var myModal = new bootstrap.Modal(document.getElementById('invoiceModal'));
    if (myModal) {
        myModal.show();
    }
    console.log("no hubo error");
});

document.getElementById("downloadPdfDirect").addEventListener("click", function () {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Título de la factura
    doc.setFontSize(16);
    doc.text("Factura de Compra", 20, 20);

    // Datos del cliente
    doc.setFontSize(12);
    doc.text("Fecha: 17/11/2024", 20, 30);
    doc.text("Nombre del Cliente: Juan Pérez", 20, 40);

    // Tabla de productos
    doc.autoTable({
        startY: 50,
        head: [['Producto', 'Cantidad', 'Precio Unitario', 'Total']],
        body: [
            ['Producto A', '2', '$10.00', '$20.00'],
            ['Producto B', '1', '$15.00', '$15.00'],
            ['Producto C', '3', '$7.50', '$22.50'],
        ],
        foot: [['', '', 'Total', '$57.50']],
    });

    // Guardar el archivo PDF
    doc.save("Factura.pdf");
});