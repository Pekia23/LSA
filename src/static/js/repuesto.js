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
                alert(result.message);
            } else {
                alert('Repuesto agregado correctamente');
            }
            window.location.href = '/LSA/mostrar-repuesto';
        })
        .catch(error => {
            console.error('Error al guardar repuesto:', error);
            alert('Error al guardar repuesto: ' + error.message);
        });
    });
});
