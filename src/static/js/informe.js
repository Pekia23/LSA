function convertHTMLpdf(divElement) {
    const element = document.getElementById(divElement);
    const nombreEquipo = document.getElementById("botonPDF").getAttribute("data-nombre-equipo") || "Informe";
    const options = {
        filename: `informe_${nombreEquipo}.pdf`,
        image: { type: 'jpeg', quality: 0.90 },
        html2canvas: { scale: 1.5 }, // Ajuste para mejor calidad de imagen
        jsPDF: { unit: 'in', format: 'a1', orientation: 'landscape' }, // Configuración de tamaño y orientación
        margin: [0.8, 0.8, 0.8, 0.8] // Agregar márgenes
    };

    // Seleccionar todos los botones o elementos a ocultar
    const noPrintElements = document.querySelectorAll('.no-print');

    // Ocultar los elementos antes de generar el PDF
    noPrintElements.forEach(el => el.style.display = 'none');

    // Obtener todas las pestañas y guardar la pestaña activa
    const tabs = document.querySelectorAll('.tab-pane');
    const activeTab = document.querySelector('.tab-pane.active');

    // Mostrar temporalmente todas las pestañas para la generación del PDF
    tabs.forEach(tab => {
        tab.classList.add('show', 'active'); // Agregar clases para que sean visibles
    });

    if (element) {
        html2pdf().set(options).from(element).save().then(() => {
            // Restaurar la visibilidad original de las pestañas
            tabs.forEach(tab => {
                tab.classList.remove('show', 'active'); // Remover clases para ocultar las no activas
            });
            // Restaurar solo la pestaña que estaba activa originalmente
            if (activeTab) {
                activeTab.classList.add('show', 'active');
            }
        }).catch(error => {
            console.error("Error al generar el PDF:", error);
            // Restaurar la visibilidad original en caso de error
            tabs.forEach(tab => {
                tab.classList.remove('show', 'active');
            });
            if (activeTab) {
                activeTab.classList.add('show', 'active');
            }
        });
    } else {
        console.error("Elemento no encontrado:", divElement);
    }
}

// Agrega el evento de clic al enlace o botón para generar el PDF
document.getElementById("botonPDF").addEventListener("click", function (event) {
    event.preventDefault(); // Previene el comportamiento predeterminado del enlace
    convertHTMLpdf("reporte"); // Llama a la función con el ID del contenedor principal
});
