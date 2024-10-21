document.addEventListener('DOMContentLoaded', function() {
    // Capturar el evento submit del formulario de Análisis Funcional
    const form = document.getElementById('analisis-funcional-form');

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Evitar el comportamiento predeterminado del formulario

        // Capturar los datos del formulario
        const data = {
            sistema: document.getElementById('sistema').value,
            subsistema: document.getElementById('subsistema').value,
            verbo: document.getElementById('verbo').value,
            accion: document.getElementById('accion').value,
            estandar_desempeño: document.getElementById('estandar_desempeño').value,
            componentes: [] // Array para capturar los componentes
        };

        // Capturar los componentes dinámicos del formulario
        document.querySelectorAll('.componente-item').forEach(function(item) {
            const idComponente = item.querySelector('p').textContent; // Obtener el nombre del componente
            const verboComponente = item.querySelector(`[input[name^="verbo_"]`).value;
            const accionComponente = item.querySelector(`[input[name^="accion_"]`).value;

            // Agregar cada componente al array de componentes
            data.componentes.push({
                nombre_componente: idComponente,
                verbo: verboComponente,
                accion: accionComponente
            });
        });

        console.log('Datos enviados:', data);

        // Enviar los datos mediante fetch
        fetch('/api/analisis-funcional', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // Convertir a JSON
        })
        .then(response => response.json())
        .then(result => {
            console.log('Análisis funcional guardado:', result);
            alert('Análisis funcional agregado correctamente');
            // Redirigir a la página de mostrar
            window.location.href = '/LSA/equipo/mostrar-analisis-funcional';
        })
        .catch(error => {
            console.error('Error al guardar análisis funcional:', error);
        });
    });
});
