document.getElementById("botonPDF").addEventListener("click", async function (event) {
    event.preventDefault();

    Swal.fire({
        title: '¿Deseas descargar el PDF?',
        text: "Puedes visualizarlo antes o descargarlo directamente.",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, descargar',
        cancelButtonText: 'Solo visualizar'
    }).then(async (result) => {
        if (result.isConfirmed) {
            const pdfBlob1 = await generatePDF("section", false); // Genera el primer PDF
            const pdfBlob2 = await generateSpecialPDF("special-fmea", false); // Genera el segundo PDF
            if (pdfBlob1 && pdfBlob2) {
                const combinedPdfBlob = await combinePDFs(pdfBlob1, pdfBlob2);
                downloadOrOpenPDF(combinedPdfBlob, true); // Descargar el PDF combinado
            }
        } else {
            const pdfBlob1 = await generatePDF("section", false); // Genera el primer PDF
            const pdfBlob2 = await generateSpecialPDF("special-fmea", false); // Genera el segundo PDF
            if (pdfBlob1 && pdfBlob2) {
                const combinedPdfBlob = await combinePDFs(pdfBlob1, pdfBlob2);
                downloadOrOpenPDF(combinedPdfBlob, false); // Descargar el PDF combinado
            }
        }
    });
});

async function generatePDF(className, shouldDownload) {
    // Generación del primer PDF como Blob
    return new Promise((resolve, reject) => {
        const elements = document.querySelectorAll(`.${className}`);
        if (elements.length === 0) {
            Swal.fire("Error", "No se encontraron elementos para generar el PDF.", "error");
            reject(null);
        }

        // Mostrar todos los tab-panes temporalmente
        const tabPanes = document.querySelectorAll('.tab-pane');
        tabPanes.forEach(pane => pane.classList.add('show', 'active'));

        // Ocultar los elementos no imprimibles
        const noPrintElements = document.querySelectorAll('.no-print');
        noPrintElements.forEach(el => el.style.display = 'none');

        // Crear contenedor temporal para clonar los elementos
        const container = document.createElement("div");
        elements.forEach(element => container.appendChild(element.cloneNode(true)));
        document.body.appendChild(container);

        const options = {
            filename: "temp1.pdf",
            image: { type: "jpeg", quality: 1 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: "mm", format: "a2", orientation: "portrait" },
            margin: [20, 20, 20, 20]
        };

        html2pdf().set(options).from(container).outputPdf('blob').then((pdfBlob) => {
            // Restaurar visibilidad de los botones y tabs
            noPrintElements.forEach(el => el.style.display = '');
            tabPanes.forEach(pane => pane.classList.remove('show', 'active'));
            resolve(pdfBlob);
        }).catch((error) => {
            console.error("Error al generar el PDF:", error);
            reject(null);
        }).finally(() => {
            document.body.removeChild(container);
        });
    });
}

async function generateSpecialPDF(className, shouldDownload) {
    // Generación del segundo PDF como Blob
    return new Promise((resolve, reject) => {
        const elements = document.querySelectorAll(`.${className}`);
        if (elements.length === 0) {
            Swal.fire("Error", "No se encontraron elementos para generar el PDF especial.", "error");
            reject(null);
        }

        // Mostrar todos los tab-panes temporalmente
        const tabPanes = document.querySelectorAll('.tab-pane');
        tabPanes.forEach(pane => pane.classList.add('show', 'active'));

        // Ocultar los elementos no imprimibles
        const noPrintElements = document.querySelectorAll('.no-print');
        noPrintElements.forEach(el => el.style.display = 'none');

        const container = document.createElement("div");
        elements.forEach(element => container.appendChild(element.cloneNode(true)));
        document.body.appendChild(container);

        const options = {
            filename: "temp2.pdf",
            image: { type: "jpeg", quality: 0.95 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: "mm", format: "a1", orientation: "landscape" },
            margin: [20, 20, 20, 20]
        };

        html2pdf().set(options).from(container).outputPdf('blob').then((pdfBlob) => {
            // Restaurar visibilidad de los botones y tabs
            noPrintElements.forEach(el => el.style.display = '');
            tabPanes.forEach(pane => pane.classList.remove('show', 'active'));
            resolve(pdfBlob);
        }).catch((error) => {
            console.error("Error al generar el PDF especial:", error);
            reject(null);
        }).finally(() => {
            document.body.removeChild(container);
        });
    });
}

async function combinePDFs(blob1, blob2) {
    // Combina los dos blobs de PDF
    const pdfDoc = await PDFLib.PDFDocument.create();
    const pdf1 = await PDFLib.PDFDocument.load(await blob1.arrayBuffer());
    const pdf2 = await PDFLib.PDFDocument.load(await blob2.arrayBuffer());

    const copiedPages1 = await pdfDoc.copyPages(pdf1, pdf1.getPageIndices());
    const copiedPages2 = await pdfDoc.copyPages(pdf2, pdf2.getPageIndices());

    copiedPages1.forEach(page => pdfDoc.addPage(page));
    copiedPages2.forEach(page => pdfDoc.addPage(page));

    const mergedPdfBlob = new Blob([await pdfDoc.save()], { type: 'application/pdf' });
    return mergedPdfBlob;
}

function downloadOrOpenPDF(blob, shouldDownload) {
    const nombreEquipo = document.getElementById("botonPDF").getAttribute("data-nombre-equipo") || "Informe";
    const url = URL.createObjectURL(blob);
    if (shouldDownload) {
        const link = document.createElement('a');
        link.href = url;
        link.download = `informe_${nombreEquipo}.pdf`;
        link.click();
    } else {
        window.open(url, '_blank');
    }
}
