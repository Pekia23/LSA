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
            Swal.fire({
                title: 'Generando PDF...',
                text: 'Por favor espera mientras se genera el documento.',
                allowOutsideClick: false,
                didOpen: () => {
                    Swal.showLoading(); // Muestra el indicador de carga
                }
            });
            const pdfBlob1 = await generatePDF("section", false); // Genera el primer PDF
            const pdfBlob2 = await generateSpecialPDF("special-fmea", false); // Genera el segundo PDF
            if (pdfBlob1 && pdfBlob2) {
                const combinedPdfBlob = await combinePDFs(pdfBlob1, pdfBlob2);
                Swal.close(); // Cierra el aviso de carga
                downloadOrOpenPDF(combinedPdfBlob, true); // Descargar el PDF combinado
            }
        } else {
            Swal.fire({
                title: 'Generando PDF...',
                text: 'Por favor espera mientras se genera el documento.',
                allowOutsideClick: false,
                didOpen: () => {
                    Swal.showLoading(); // Muestra el indicador de carga
                }
            });
            const pdfBlob1 = await generatePDF("section", false); // Genera el primer PDF
            const pdfBlob2 = await generateSpecialPDF("special-fmea", false); // Genera el segundo PDF
            if (pdfBlob1 && pdfBlob2) {
                const combinedPdfBlob = await combinePDFs(pdfBlob1, pdfBlob2);
                Swal.close(); // Cierra el aviso de carga
                downloadOrOpenPDF(combinedPdfBlob, false); // Descargar el PDF combinado
            }
        }
    });
});

function addNumberingToTitles(container, initialH2Counter = 1) {
    const titleSelectors = ['h2', 'h3']; // Niveles de encabezado a numerar
    let h2Counter = initialH2Counter - 1; // Configura el valor inicial para <h2>
    let h3Counter = 0; // Contador para <h3>

    // Itera por los encabezados en el orden en que aparecen
    const titles = container.querySelectorAll(titleSelectors.join(','));
    titles.forEach(title => {
        if (title.tagName.toLowerCase() === 'h2') {
            // Incrementa el contador de <h2> y reinicia el de <h3>
            h2Counter++;
            h3Counter = 0;
            title.textContent = `${h2Counter}. ${title.textContent}`; // Numeración para <h2>
        } else if (title.tagName.toLowerCase() === 'h3') {
            // Incrementa el contador de <h3>
            h3Counter++;
            title.textContent = `${h2Counter}.${h3Counter} ${title.textContent}`; // Numeración para <h3>
        }
    });
}

async function createCoverPage() {
    // Fetch equipment information (name, brand, model)
    const botonPDF = document.getElementById("botonPDF");
    const nombre = botonPDF.getAttribute("data-nombre-equipo");
    const marca = botonPDF.getAttribute("data-marca-equipo");
    const modelo = botonPDF.getAttribute("data-modelo-equipo");
    
    // Create a PDF document using PDFLib
    const pdfDoc = await PDFLib.PDFDocument.create();

    // Add a page with dimensions A2 (converted to points)
    const a2Width = 1190.55; // Width in points
    const a2Height = 1683.78; // Height in points
    const page = pdfDoc.addPage([a2Width, a2Height]);

    // Load the cover image
    const imageBytes = await fetch('/static/img/portada.png').then(res => res.arrayBuffer());
    const coverImage = await pdfDoc.embedPng(imageBytes);

    // Get image dimensions for scaling
    const { width, height } = coverImage;

    // Scale the image to fill the page
    const scale = Math.max(a2Width / width, a2Height / height);
    const scaledWidth = width * scale;
    const scaledHeight = height * scale;

    // Draw the image centered on the page
    page.drawImage(coverImage, {
        x: (a2Width - scaledWidth) / 2,
        y: (a2Height - scaledHeight) / 2,
        width: scaledWidth,
        height: scaledHeight,
    });

    // Add dynamic text (Equipment Name, Brand, Model)
    const font = await pdfDoc.embedFont(PDFLib.StandardFonts.HelveticaBold);
    const fontSize = 55;
    const fontSizes = 40;
    const textColor = PDFLib.rgb(0 / 255, 74 / 255, 173 / 255); // RGB: (0, 74, 173)

    page.drawText("INFORME DE ANÁLISIS DE ", {
        x: 105,
        y: a2Height - 1150,
        size: fontSize,
        font,
        color: textColor,
    });

    page.drawText("DE SOPORTE LOGÍSTICO ", {
        x: 105,
        y: a2Height - 1200,
        size: fontSize,
        font,
        color: textColor,
    });

    page.drawText("(LSA)", {
        x: 105,
        y: a2Height - 1250,
        size: fontSize,
        font,
        color: textColor,
    });
    
    page.drawText(`Nombre: ${nombre}`, {
        x: 105,
        y: a2Height - 1330,
        size: fontSizes,
        font,
        color: textColor,
    });

    page.drawText(`Marca: ${marca}`, {
        x: 105,
        y: a2Height - 1380,
        size: fontSizes,
        font,
        color: textColor,
    });

    page.drawText(`Modelo: ${modelo}`, {
        x: 105,
        y: a2Height - 1430,
        size: fontSizes,
        font,
        color: textColor,
    });

    // Export the document as a Blob
    return new Blob([await pdfDoc.save()], { type: 'application/pdf' });
}

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
        addNumberingToTitles(container);
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
        addNumberingToTitles(container,5);
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
     // Crear la portada
    const coverPageBlob = await createCoverPage();
    const coverPagePdf = await PDFLib.PDFDocument.load(await coverPageBlob.arrayBuffer());
    const coverPage = await pdfDoc.copyPages(coverPagePdf, [0]);
    const pdf1 = await PDFLib.PDFDocument.load(await blob1.arrayBuffer());
    const pdf2 = await PDFLib.PDFDocument.load(await blob2.arrayBuffer());

    const copiedPages1 = await pdfDoc.copyPages(pdf1, pdf1.getPageIndices());
    const copiedPages2 = await pdfDoc.copyPages(pdf2, pdf2.getPageIndices());

    pdfDoc.addPage(coverPage[0]);
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
