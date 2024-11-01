function convertHTMLpdf(divElement) {
    const element = document.getElementById(divElement);
    const nombreEquipo = document.getElementById("botonPDF").getAttribute("data-nombre-equipo") || "Informe";
    const options = {
        filename: `informe_${nombreEquipo}.pdf`,
        image: { type: 'jpeg', quality: 0.90 },
        html2canvas: { scale: 1.5 },
        jsPDF: { unit: 'in', format: 'a1', orientation: 'landscape' },
        margin: [0.8, 0.8, 0.8, 0.8]
    };

    const noPrintElements = document.querySelectorAll('.no-print');
    noPrintElements.forEach(el => el.style.display = 'none');

    const tabs = document.querySelectorAll('.tab-pane');
    const activeTab = document.querySelector('.tab-pane.active');

    tabs.forEach(tab => {
        tab.classList.add('show', 'active');
    });

    if (element) {
        html2pdf().set(options).from(element).outputPdf('blob').then((pdfBlob) => {
            const pdfUrl = URL.createObjectURL(pdfBlob);
            window.open(pdfUrl, '_blank'); // Abre el PDF en una nueva pestaña

            // Restaurar la visibilidad original de las pestañas
            tabs.forEach(tab => tab.classList.remove('show', 'active'));
            if (activeTab) activeTab.classList.add('show', 'active');
        }).catch(error => {
            console.error("Error al generar el PDF:", error);
            tabs.forEach(tab => tab.classList.remove('show', 'active'));
            if (activeTab) activeTab.classList.add('show', 'active');
        });
    } else {
        console.error("Elemento no encontrado:", divElement);
    }
}

document.getElementById("botonPDF").addEventListener("click", function (event) {
    event.preventDefault();
    convertHTMLpdf("reporte");
});
