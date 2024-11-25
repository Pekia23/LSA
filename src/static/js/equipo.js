document.addEventListener('DOMContentLoaded', function () {
    const eliminarButton = document.getElementById('btn-eliminar-equipo');

    if (eliminarButton) {
        eliminarButton.addEventListener('click', function () {
            const equipoId = eliminarButton.getAttribute('data-equipo-id');

            // Confirmación con SweetAlert2 antes de eliminar
            Swal.fire({
                title: '¿Estás seguro de que deseas eliminar este equipo?',
                text: "Esta acción no se puede deshacer.",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Sí, eliminar',
                cancelButtonText: 'Cancelar',
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Enviar la solicitud POST al backend
                    fetch('/LSA/eliminar-equipo', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ id_equipo_info: equipoId })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.message) {
                            Swal.fire({
                                title: 'Eliminado',
                                text: data.message,
                                icon: 'success',
                                confirmButtonText: 'OK'
                            }).then(() => {
                                // Redirigir o actualizar la página después de eliminar
                                window.location.href = '/LSA';
                            });
                        } else {
                            Swal.fire('Error', 'No se pudo eliminar el equipo', 'error');
                        }
                    })
                    .catch(error => {
                        console.error('Error al eliminar equipo:', error);
                        Swal.fire('Error', 'Ocurrió un error al eliminar el equipo', 'error');
                    });
                }
            });
        });
    }

     // Manejo del botón Editar Equipo
     const editarButton = document.querySelector('a.btn-primary.no-print');

     if (editarButton) {
         editarButton.addEventListener('click', function (event) {
             event.preventDefault();
             const url = this.href;
 
             // Confirmación con SweetAlert2 antes de editar
             Swal.fire({
                 title: '¿Deseas editar la información de este equipo?',
                 text: "Serás redirigido a la página de edición.",
                 icon: 'question',
                 showCancelButton: true,
                 confirmButtonText: 'Sí, editar',
                 cancelButtonText: 'Cancelar',
                 confirmButtonColor: '#3085d6',
                 cancelButtonColor: '#d33'
             }).then((result) => {
                 if (result.isConfirmed) {
                     // Redirigir si el usuario confirma
                     window.location.href = url;
                 }
             });
         });
     }
});
