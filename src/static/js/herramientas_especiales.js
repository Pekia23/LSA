document.addEventListener('DOMContentLoaded', function() {
    // Capturar el evento submit del formulario de Herramientas Especiales
    const form = document.getElementById('herramientas-especiales-form');

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Evitar el comportamiento predeterminado del formulario

        // Capturar los datos del formulario
        const data = {
            equipo: document.getElementById('equipo').value,
            nombre_herramienta: document.getElementById('nombre_herramienta').value,
            mtbf: document.getElementById('mtbf').value,
            notas: document.getElementById('notas').value,
            parte_numero: document.getElementById('parte_numero').value,
            valor: document.getElementById('valor').value,
            dibujo_seccion: document.getElementById('dibujo_seccion').value
        };

        // Enviar los datos mediante fetch
        fetch('/api/herramientas-especiales', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // Convertir a JSON
        })
        .then(response => response.json())
        .then(result => {
            console.log('Herramientas especiales guardadas:', result);
            alert('Herramientas especiales agregadas correctamente');
        })
        .catch(error => {
            console.error('Error al guardar herramientas especiales:', error);
        });
    });
});
