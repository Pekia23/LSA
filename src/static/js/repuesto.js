document.addEventListener('DOMContentLoaded', function() {
    // Capturar el evento submit del formulario de Repuesto
    const form = document.getElementById('repuesto-form');

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Evitar el comportamiento predeterminado del formulario

        // Capturar los datos del formulario
        const data = {
            parte_numero: document.getElementById('parte_numero').value,
            nombre_herramienta: document.getElementById('nombre_herramienta').value,
            valor: document.getElementById('valor').value,
            dibujo_seccion: document.getElementById('dibujo_seccion').value,
            notas: document.getElementById('notas').value
        };

        // Enviar los datos mediante fetch
        fetch('/api/repuesto', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // Convertir a JSON
        })
        .then(response => response.json())
        .then(result => {
            console.log('Repuesto guardado:', result);
            alert('Repuesto agregado correctamente');
            // Redirigir a la lista de repuestos
            window.location.href = '/LSA/repuestos';
        })
        .catch(error => {
            console.error('Error al guardar repuesto:', error);
        });
    });
});
