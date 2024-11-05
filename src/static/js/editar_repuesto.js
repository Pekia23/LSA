document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('editar-repuesto-form');
    const repuestoId = form.getAttribute('data-repuesto-id');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

       
        const formData = new FormData(form);

        fetch('/api/repuesto/' + repuestoId, {
            method: 'POST',  // Usamos POST para la actualización
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            if (result.message) {
                alert(result.message);
            } else {
                alert('Repuesto actualizado correctamente');
            }
            window.location.href = '/LSA/mostrar-repuesto';
        })
        .catch(error => {
            console.error('Error al actualizar repuesto:', error);
            alert('Error al actualizar repuesto: ' + error.message);
        });
    });
});
