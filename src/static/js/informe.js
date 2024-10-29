function convertHTMLpdf(divElement) {
    const element = document.getElementById(divElement);
    const options = {
        filename: "informe_{{ equipo.nombre_equipo }}.pdf",  // corregido 'filename'
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },  // ajustado para html2canvas
        jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
    };

    if (element) {
        html2pdf().set(options).from(element).save();
    } else {
        console.error("Elemento no encontrado:", divElement);
    }
}

// Agrega el evento de clic al enlace
document.getElementById("botonPDF").addEventListener("click", function (event) {
    event.preventDefault(); // Previene el comportamiento predeterminado del enlace
    convertHTMLpdf("reporte"); // Llama a la función con el ID del div
});
