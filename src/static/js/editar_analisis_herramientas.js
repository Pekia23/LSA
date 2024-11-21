document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('editar-analisis-herramienta-form');
    const analisisId = form.getAttribute('data-analisis-id');

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevenir comportamiento predeterminado del formulario

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
                            // Llama a la función redirigirSegunURLAnterior
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

    function redirigirSegunURLAnterior() {
        const urlAnterior = document.referrer; // URL previa
        const idEquipoInfo = document.getElementById('id_equipo_info')?.value; // Asegura que no falle si el elemento no existe
    
        // Verifica que idEquipoInfo tenga un valor válido
        if (!idEquipoInfo) {
            console.error("El id_equipo_info no está definido o es inválido.");
            return; // Detén la ejecución si no hay idEquipoInfo
        }
    
        // Verifica si la URL anterior contiene la parte esperada, ignorando los parámetros
        if (urlAnterior.includes('/LSA/mostrar-herramientas-especiales-ext')) {
            // Redirige con el id dinámico
            window.location.href = `/LSA/mostrar-herramientas-especiales-ext?id_equipo_info=${idEquipoInfo}`;
        } else {
            // Redirige a una vista por defecto si no coincide
            window.location.href = '/LSA/mostrar-herramientas-especiales';
        }
    }
});
