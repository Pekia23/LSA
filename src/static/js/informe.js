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
            generatePDF(true);
        } else {
            generatePDF(false);
        }
    });
});

async function generatePDF(shouldDownload) {
    const doc = new jsPDF();

    const sections = [
        { id: 'section1', format: 'a4', orientation: 'portrait' },
        { id: 'section2', format: 'a3', orientation: 'landscape' },
        { id: 'section3', format: 'a5', orientation: 'portrait' }
    ];

    for (const section of sections) {
        const element = document.getElementById(section.id);

        if (element) {
            // Generar imagen de la sección usando html2canvas
            const canvas = await html2canvas(element, { scale: 2 });
            const imgData = canvas.toDataURL('image/jpeg', 0.9);

            // Establecer el formato y la orientación para la sección actual
            doc.setPageSize(section.format, section.orientation);

            // Calcular las dimensiones para la imagen
            const pageWidth = doc.internal.pageSize.getWidth();
            const pageHeight = doc.internal.pageSize.getHeight();
            const imgWidth = canvas.width;
            const imgHeight = canvas.height;
            const ratio = Math.min(pageWidth / imgWidth, pageHeight / imgHeight);

            const width = imgWidth * ratio;
            const height = imgHeight * ratio;

            // Agregar la imagen al PDF
            doc.addImage(imgData, 'JPEG', 0, 0, width, height);

            // Agregar una nueva página si no es la última sección
            if (section !== sections[sections.length - 1]) {
                doc.addPage();
            }
        }
    }

    // Descargar o visualizar el PDF según la opción elegida
    if (shouldDownload) {
        doc.save('reporte.pdf');
    } else {
        window.open(doc.output('bloburl'), '_blank');
    }
}
