document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('repuesto-form');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch('/api/repuesto', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            // Utiliza el resultado si es necesario
            if (result.message) {
                Swal.fire({
                    icon: 'success',
                    title: '¡Éxito!',
                    text: result.message,
                    confirmButtonText: 'OK'
                }).then(() => {
                    window.location.href = '/LSA/mostrar-repuesto';
                });
            } else {
                Swal.fire({
                    icon: 'warning',
                    title: 'Repuesto no agregado',
                    text: 'Por favor, complete todos los campos obligatorios',
                    confirmButtonText: 'OK'
                }).then(() => {
                    window.location.href = '/LSA/registro-repuesto';
                });
            }
        })
        .catch(error => {
            console.error('Error al guardar repuesto:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Error al guardar repuesto: ' + error.message,
                confirmButtonText: 'OK'
            });
        });
    });
});

