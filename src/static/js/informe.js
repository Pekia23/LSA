
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
            generatePDF("reporte", true); // El segundo parámetro indica que se debe descargar
        } else {
            // Solo visualizar el PDF sin descargar
            generatePDF("reporte", false); // No descargar, solo visualizar
        }
    });
});

function generatePDF(divElement, shouldDownload) {
    const element = document.getElementById(divElement);
    const nombreEquipo = document.getElementById("botonPDF").getAttribute("data-nombre-equipo") || "Informe";
    
    const options = {
        filename: `informe_${nombreEquipo}.pdf`,
        image: { type: 'jpeg', quality: 0.90 },
        html2canvas: { scale: 1.5 },
        jsPDF: { unit: 'in', format: 'a1', orientation: 'landscape' },
        margin: [0.5, 0.5, 0.5, 0.5]
    };

    const noPrintElements = document.querySelectorAll('.no-print');
    noPrintElements.forEach(el => el.style.display = 'none');

    const tabs = document.querySelectorAll('.tab-pane');
    const activeTab = document.querySelector('.tab-pane.active');
    tabs.forEach(tab => tab.classList.add('show', 'active'));

    if (element) {
        html2pdf().set(options).from(element).outputPdf('blob').then((pdfBlob) => {
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

            // Restaurar la visibilidad original de las pestañas
            noPrintElements.forEach(el => el.style.display = '');
            tabs.forEach(tab => tab.classList.remove('show', 'active'));
            if (activeTab) activeTab.classList.add('show', 'active');
        }).catch(error => {
            console.error("Error al generar el PDF:", error);
            noPrintElements.forEach(el => el.style.display = '');
            tabs.forEach(tab => tab.classList.remove('show', 'active'));
            if (activeTab) activeTab.classList.add('show', 'active');

        });
    } else {
        console.error("Elemento no encontrado:", divElement);
    }
}

