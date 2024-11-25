document.addEventListener('DOMContentLoaded', function() {
    // Función para limpiar el formulario
    function limpiarFormulario(form) {
        form.reset(); // Limpiar todos los campos del formulario
    }

    // Manejo del formulario de Análisis de Herramientas
    const formAnalisis = document.getElementById('analisis-herramientas-form');

    formAnalisis.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevenir comportamiento predeterminado del formulario

        const formData = new FormData(formAnalisis);

        fetch('/api/analisis-herramientas', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(error => {
                    throw new Error(error.error || 'Error desconocido del servidor');
                });
            }
            return response.json();
        })
        .then(result => {
            // Mostrar mensaje de éxito con SweetAlert
            Swal.fire({
                icon: 'success',
                title: '¡Éxito!',
                text: result.message, // Mensaje devuelto por el servidor
            }).then(() => {
                // Limpiar el formulario después de enviar la información
                limpiarFormulario(formAnalisis);

                // Redirigir o actualizar la página si es necesario
                // window.location.reload(); // Descomentar si se desea recargar la página
            });
        })
        .catch(error => {
            // Mostrar mensaje de error con SweetAlert
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Error al guardar análisis de herramientas. Inténtalo nuevamente.',
            });
            console.error('Error al guardar análisis de herramientas:', error);
        });
    });

    // Manejo del formulario de Herramientas Especiales
    const formEspeciales = document.getElementById('herramientas-especiales-form');

    formEspeciales.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevenir comportamiento predeterminado del formulario

        const formData = new FormData(formEspeciales);

        fetch('/api/herramientas-especiales', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(error => {
                    throw new Error(error.error || 'Error desconocido del servidor');
                });
            }
            return response.json();
        })
        .then(result => {
            // Mostrar mensaje de éxito con SweetAlert
            Swal.fire({
                icon: 'success',
                title: '¡Éxito!',
                text: result.message, // Mensaje devuelto por el servidor
            }).then(() => {
                // Limpiar el formulario después de enviar la información
                limpiarFormulario(formEspeciales);

                // Redirigir o actualizar la página si es necesario
                // window.location.reload(); // Descomentar si se desea recargar la página
            });
        })
        .catch(error => {
            // Mostrar mensaje de error con SweetAlert
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Error al guardar herramientas especiales. Inténtalo nuevamente.',
            });
            console.error('Error al guardar herramientas especiales:', error);
        });
    });
});
