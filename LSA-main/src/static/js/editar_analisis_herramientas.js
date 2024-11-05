document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('editar-analisis-herramienta-form');
    const analisisId = form.getAttribute('data-analisis-id');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch('/api/analisis-herramientas/' + analisisId, {
            method: 'PUT',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            if (result.message) {
                alert(result.message);
                window.location.href = '/LSA/mostrar-herramientas-especiales';
            } else {
                alert('Error al actualizar análisis de herramienta');
            }
        })
        .catch(error => {
            console.error('Error al actualizar análisis de herramienta:', error);
            alert('Error al actualizar análisis de herramienta: ' + error.message);
        });
    });
});
