document.addEventListener('DOMContentLoaded', function() {
    // Manejo del botón Editar en la sección de análisis de herramientas
    const editButtonsAnalisis = document.querySelectorAll('.btn-editar-analisis');
    editButtonsAnalisis.forEach(function(button) {
        button.addEventListener('click', function() {
            const herramientaId = this.getAttribute('data-id');
            window.location.href = '/LSA/editar-analisis-herramienta/' + herramientaId;
        });
    });

    // Manejo del botón Eliminar en la sección de análisis de herramientas
    const deleteButtonsAnalisis = document.querySelectorAll('.btn-eliminar-analisis');
    deleteButtonsAnalisis.forEach(function(button) {
        button.addEventListener('click', function() {
            const herramientaId = this.getAttribute('data-id');
            if (confirm('¿Estás seguro de que deseas eliminar esta herramienta?')) {
                fetch('/api/analisis-herramientas/' + herramientaId, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(result => {
                    if (result.message) {
                        alert(result.message);
                        this.closest('tr').remove();
                    } else {
                        alert('Error al eliminar herramienta');
                    }
                })
                .catch(error => {
                    console.error('Error al eliminar herramienta:', error);
                    alert('Error al eliminar herramienta: ' + error.message);
                });
            }
        });
    });

    // Manejo del botón Editar en la sección de herramientas especiales
    const editButtonsEspecial = document.querySelectorAll('.btn-editar');
    editButtonsEspecial.forEach(function(button) {
        button.addEventListener('click', function() {
            const herramientaId = this.getAttribute('data-id');
            window.location.href = '/LSA/editar-herramienta-especial/' + herramientaId;
        });
    });

    // Manejo del botón Eliminar en la sección de herramientas especiales
    const deleteButtonsEspecial = document.querySelectorAll('.btn-eliminar');
    deleteButtonsEspecial.forEach(function(button) {
        button.addEventListener('click', function() {
            const herramientaId = this.getAttribute('data-id');
            if (confirm('¿Estás seguro de que deseas eliminar esta herramienta?')) {
                fetch('/api/herramientas-especiales/' + herramientaId, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(result => {
                    if (result.message) {
                        alert(result.message);
                        this.closest('tr').remove();
                    } else {
                        alert('Error al eliminar herramienta');
                    }
                })
                .catch(error => {
                    console.error('Error al eliminar herramienta:', error);
                    alert('Error al eliminar herramienta: ' + error.message);
                });
            }
        });
    });
});
