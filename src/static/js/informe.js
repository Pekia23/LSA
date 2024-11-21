document.getElementById("botonPDF").addEventListener("click", function (event) {
    event.preventDefault();

    // Mostrar el pop-up de confirmación con SweetAlert
    Swal.fire({
        title: '¿Deseas descargar el PDF?',
        text: "Puedes visualizarlo antes o descargarlo directamente.",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, descargar',
        cancelButtonText: 'Solo visualizar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Generar y descargar el PDF
            generatePDF("section", true); // El segundo parámetro indica que se debe descargar
            generateSpecialPDF("special-fmea", true)
        } else {
            // Solo visualizar el PDF sin descargar
            generatePDF("section", false); // No descargar, solo visualizar
            generateSpecialPDF("special-fmea", false)
        }
    });
});

function generatePDF(className, shouldDownload) {
    // Seleccionar todos los elementos con la clase "section"
    Swal.fire({
        title: 'Generando PDF...',
        text: 'Por favor, espera mientras se genera el archivo.',
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading(); // Muestra un spinner mientras se procesa
        }
    });
    // Mostrar todas las pestañas temporalmente
    const tabPanes = document.querySelectorAll('.tab-pane');
    tabPanes.forEach(pane => pane.classList.add('show', 'active'));

    const elements = document.querySelectorAll(`.${className}`);
    
    if (elements.length === 0) {
        Swal.close(); // Cierra el aviso si no se encuentran elementos
        Swal.fire({
            title: 'Error',
            text: 'No se encontraron elementos para generar el PDF.',
            icon: 'error',
        });
        return;
    }

    // Crear un contenedor temporal para juntar los elementos seleccionados
    const container = document.createElement("div");
    container.setAttribute("id", "pdf-container");
    elements.forEach(element => {
        const clone = element.cloneNode(true); // Clonar los elementos para preservar el original
        container.appendChild(clone);
    });

    document.body.appendChild(container); // Añadir el contenedor temporal al body

    const nombreEquipo = document.getElementById("botonPDF").getAttribute("data-nombre-equipo") || "Informe";
    const options = {
        filename: `informe_${nombreEquipo}.pdf`,
        image: { type: 'jpeg', quality: 0.90 },
        html2canvas: { scale: 1.5 },
        jsPDF: { unit: 'mm', format: 'a2', orientation: 'portrait' },
        margin: [20, 20, 20, 20]
    };

    // Ocultar elementos no imprimibles
    const noPrintElements = document.querySelectorAll('.no-print');
    noPrintElements.forEach(el => el.style.display = 'none');

    // Generar el PDF
    html2pdf().set(options).from(container).outputPdf('blob').then((pdfBlob) => {
        const pdfUrl = URL.createObjectURL(pdfBlob);
        if (shouldDownload) {
            // Descargar el PDF
            const link = document.createElement('a');
            link.href = pdfUrl;
            link.download = `informe_${nombreEquipo}.pdf`;
            link.click();
        } else {
            // Solo abrir el PDF en una nueva pestaña para visualizar
            window.open(pdfUrl, '_blank');
        }
        Swal.close();
        // Restaurar visibilidad de los elementos ocultos
        noPrintElements.forEach(el => el.style.display = '');
        document.body.removeChild(container); // Eliminar el contenedor temporal
        // Restaurar el estado original de las pestañas
        tabPanes.forEach(pane => pane.classList.remove('show', 'active'));
        const activeTab = document.querySelector('.nav-link.active');
        if (activeTab) activeTab.click(); // Volver a la pestaña activa original
    }).catch(error => {
        console.error("Error al generar el PDF:", error);
        Swal.fire({
            title: 'Error',
            text: 'Ocurrió un problema al generar el PDF.',
            icon: 'error',
        });
        noPrintElements.forEach(el => el.style.display = '');
        document.body.removeChild(container); // Asegurar la limpieza en caso de error
    });
}

function generateSpecialPDF(className, shouldDownload) {

    const elements = document.querySelectorAll(`.${className}`);
    if (elements.length === 0) {
        Swal.close();
        Swal.fire({
            title: 'Error',
            text: 'No se encontraron elementos para generar el PDF de análisis especial.',
            icon: 'error',
        });
        return;
    }

    const container = document.createElement("div");
    container.setAttribute("id", "special-pdf-container");
    elements.forEach(element => {
        const clone = element.cloneNode(true);
        container.appendChild(clone);
    });

    document.body.appendChild(container);

    const nombreEquipo = document.getElementById("botonPDF").getAttribute("data-nombre-equipo") || "Informe";
    const options = {
        filename: `analisis_especial_${nombreEquipo}.pdf`,
        image: { type: 'jpeg', quality: 0.95 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a1', orientation: 'landscape' },
        margin: [10, 10, 10, 10]
    };

    html2pdf().set(options).from(container).outputPdf('blob').then((pdfBlob) => {
        const pdfUrl = URL.createObjectURL(pdfBlob);
        if (shouldDownload) {
            const link = document.createElement('a');
            link.href = pdfUrl;
            link.download = `analisis_especial_${nombreEquipo}.pdf`;
            link.click();
        }else {
            // Solo abrir el PDF en una nueva pestaña para visualizar
            window.open(pdfUrl, '_blank');
        }
        Swal.close();
        document.body.removeChild(container);
    }).catch(error => {
        console.error("Error al generar el PDF de análisis especial:", error);
        Swal.fire({
            title: 'Error',
            text: 'Ocurrió un problema al generar el PDF de análisis especial.',
            icon: 'error',
        });
    });
}