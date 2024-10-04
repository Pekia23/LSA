document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('herramientas-especiales-form');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch('/api/herramientas-especiales', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            console.log('Herramienta especial guardada:', result);
            alert('Herramienta especial agregada correctamente');
            window.location.href = '/LSA/mostrar-herramientas-especiales';
        })
        .catch(error => {
            console.error('Error al guardar herramienta especial:', error);
        });
    });
});
