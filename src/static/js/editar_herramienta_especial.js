document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('editar-herramienta-form');
    const herramientaId = form.getAttribute('data-herramienta-id');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Confirmación con SweetAlert2 antes de actualizar
        Swal.fire({
            title: '¿Estás seguro?',
            text: "Se actualizará la información de la herramienta.",
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, actualizar',
            cancelButtonText: 'Cancelar',
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33'
        }).then((result) => {
            if (result.isConfirmed) {
                // Crear FormData para enviar los datos del formulario
                const formData = new FormData(form);

                // Realizar la petición de actualización
                fetch('/api/herramientas-especiales/' + herramientaId, {
                    method: 'PUT',
                    body: formData
                })
                .then(response => response.json())
                .then(result => {
                    if (result.message) {
                        Swal.fire({
                            title: 'Actualizado',
                            text: result.message,
                            icon: 'success',
                            confirmButtonText: 'OK'
                        }).then(() => {
                            window.location.href = '/LSA/mostrar-herramientas-especiales';
                        });
                    } else {
                        Swal.fire('Error', 'Error al actualizar herramienta', 'error');
                    }
                })
                .catch(error => {
                    console.error('Error al actualizar herramienta:', error);
                    Swal.fire('Error', 'Error al actualizar herramienta: ' + error.message, 'error');
                });
            }
        });
    });
});

