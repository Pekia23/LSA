document.addEventListener('DOMContentLoaded', function() {
    // Capturar el evento del botón "Agregar RCM"
    const btnAgregarRCM = document.getElementById('btn-agregar-rcm');
    btnAgregarRCM.addEventListener('click', function() {
        alert('RCM Agregado con éxito.');

        // Capturar los datos del formulario
        const data = {
            accion_recomendada: document.getElementById('accion_recomendada').value,
            intervalo_inicial: document.getElementById('intervalo_inicial').value
        };

        // Enviar los datos mediante fetch
        fetch('/api/rcm/segundo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // Convertir a JSON
        })
        .then(response => response.json())
        .then(result => {
            console.log('RCM guardado:', result);
            alert('RCM agregado correctamente');
        })
        .catch(error => {
            console.error('Error al guardar RCM:', error);
        });
    });
});
