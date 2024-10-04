document.addEventListener('DOMContentLoaded', function() {
    // Manejo del formulario de Análisis de Herramientas
    const formAnalisis = document.getElementById('analisis-herramientas-form');

    formAnalisis.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(formAnalisis);

        fetch('/api/analisis-herramientas', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);
            // Redirigir o actualizar la página si es necesario
        })
        .catch(error => {
            console.error('Error al guardar análisis de herramientas:', error);
        });
    });

    // Manejo del formulario de Herramientas Especiales
    const formEspeciales = document.getElementById('herramientas-especiales-form');

    formEspeciales.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(formEspeciales);

        fetch('/api/herramientas-especiales', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);
            // Redirigir o actualizar la página si es necesario
        })
        .catch(error => {
            console.error('Error al guardar herramientas especiales:', error);
        });
    });
});
