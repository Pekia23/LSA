document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('editar-analisis-herramienta-form');
    const analisisId = form.getAttribute('data-analisis-id');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Confirmación con SweetAlert2 antes de actualizar
        Swal.fire({
            title: '¿Estás seguro?',
            text: "Se actualizará la información del análisis de herramienta.",
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
                fetch('/api/analisis-herramientas/' + analisisId, {
                    method: 'PUT',
                    body: formData
                })
                .then(response => response.json())
                .then(result => {
                    if (result.message) {
                        // Alerta de éxito
                        Swal.fire({
                            title: 'Actualizado',
                            text: result.message,
                            icon: 'success',
                            confirmButtonText: 'OK'
                        }).then(() => {
                            // Lógica de redirección según la URL anterior
                            redirigirSegunURLAnterior();
                        });
                    } else {
                        // Alerta de error
                        Swal.fire({
                            title: 'Error',
                            text: 'Error al actualizar análisis de herramienta',
                            icon: 'error',
                            confirmButtonText: 'OK'
                        });
                    }
                })
                .catch(error => {
                    console.error('Error al actualizar análisis de herramienta:', error);
                    // Alerta de error en caso de excepción
                    Swal.fire({
                        title: 'Error',
                        text: 'Error al actualizar análisis de herramienta: ' + error.message,
                        icon: 'error',
                        confirmButtonText: 'OK'
                    });
                });
            }
        });
    });

    // Función para redirigir según la URL anterior
    function redirigirSegunURLAnterior() {
        const urlAnterior = document.referrer;
        const idEquipoInfo = document.getElementById('id_equipo_info').value;
        console.log(idEquipoInfo)
        // Lógica de redirección según la URL anterior
        if (urlAnterior.includes(`LSA/mostrar-herramientas-especiales-ext?id_equipo_info=${idEquipoInfo}`)) {
            // Redirige a una vista específica
            window.location.href = `LSA/mostrar-herramientas-especiales-ext?id_equipo_info=${idEquipoInfo}`;
        }
    }
});
