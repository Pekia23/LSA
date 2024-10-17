document.addEventListener('DOMContentLoaded', function() {
    // Función para limpiar el formulario
    function limpiarFormulario(form) {
        form.reset();  // Limpiar todos los campos del formulario
    }

    // Manejo del formulario de Análisis de Herramientas
    const formAnalisis = document.getElementById('analisis-herramientas-form');

    formAnalisis.addEventListener('submit', function(e) {
        e.preventDefault();  // Prevenir comportamiento predeterminado del formulario

        const formData = new FormData(formAnalisis);

        fetch('/api/analisis-herramientas', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);  // Mostrar mensaje del resultado

            // Limpiar el formulario después de enviar la información
            limpiarFormulario(formAnalisis);

            // Redirigir o actualizar la página si es necesario
            // window.location.reload();  // Descomentar si se desea recargar la página
        })
        .catch(error => {
            console.error('Error al guardar análisis de herramientas:', error);
        });
    });

    // Manejo del formulario de Herramientas Especiales
    const formEspeciales = document.getElementById('herramientas-especiales-form');

    formEspeciales.addEventListener('submit', function(e) {
        e.preventDefault();  // Prevenir comportamiento predeterminado del formulario

        const formData = new FormData(formEspeciales);

        fetch('/api/herramientas-especiales', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);  // Mostrar mensaje del resultado

            // Limpiar el formulario después de enviar la información
            limpiarFormulario(formEspeciales);

            // Redirigir o actualizar la página si es necesario
            // window.location.reload();  // Descomentar si se desea recargar la página
        })
        .catch(error => {
            console.error('Error al guardar herramientas especiales:', error);
        });
    });
});
