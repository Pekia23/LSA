function actualizarDetallesFalla() {
    const mecanismoId = document.getElementById('mecanismo_falla').value;
    
    // Realizar una petición GET al backend con el id del mecanismo seleccionado
    fetch(`/LSA/obtener-detalles-falla/${mecanismoId}`)
        .then(response => response.json())
        .then(data => {
            const detalleFallaSelect = document.getElementById('detalle_falla');
            detalleFallaSelect.innerHTML = '<option value="" disabled selected>---- Selecciona Detalle de Falla ----</option>';
            data.forEach(detalle => {
                const option = document.createElement('option');
                option.value = detalle.id;
                option.text = detalle.nombre;
                detalleFallaSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error al cargar los detalles de falla:', error));
}

function actualizarNombreFalla() {
    var codigoModoFallaId = document.getElementById("codigo_modo_falla").value;

    // Realiza una petición para obtener el nombre del modo de falla y el consecutivo
    fetch(`/LSA/obtener-nombre-falla/${codigoModoFallaId}`)
        .then(response => response.json())
        .then(data => {
            // Actualizar el nombre del modo de falla
            document.getElementById("nombre_modo_falla").value = data.nombre;

            // Actualizar el campo del consecutivo de modo de falla
            document.getElementById("consecutivo_modo_falla").value = data.consecutivo;

            // Guardar el id_consecutivo_modo_falla en un campo oculto
            document.getElementById("id_consecutivo_modo_falla").value = data.id_consecutivo_modo_falla;
        })
        .catch(error => console.error('Error al actualizar el nombre y consecutivo:', error));
}
function actualizarValor(selectId, inputId) {
    // Obtener el select y la opción seleccionada
    var selectElement = document.getElementById(selectId);
    var selectedOption = selectElement.options[selectElement.selectedIndex];

    // Obtener el valor del atributo data-valor de la opción seleccionada
    var valor = selectedOption.getAttribute('data-valor');

    // Verificar que el valor existe antes de asignarlo al input
    if (valor) {
        document.getElementById(inputId).value = valor;
    }
    actualizarCalculos()
}



// Función para actualizar los cálculos automáticos
function actualizarCalculos() {
    // Obtener los valores numéricos de las casillas anteriores
    var consecuenciaSeveridad = parseFloat(document.getElementById('consecuencia_severidad_valor').value) || 0;
    var seguridadFisica = parseFloat(document.getElementById('seguridad_fisica_valor').value) || 0;
    var medioAmbiente = parseFloat(document.getElementById('medio_ambiente_valor').value) || 0;
    var impactoOperacional = parseFloat(document.getElementById('impacto_operacional_valor').value) || 0;
    var costosReparacion = parseFloat(document.getElementById('costos_reparacion_valor').value) || 0;
    var flexibilidadOperacional = parseFloat(document.getElementById('flexibilidad_operacional_valor').value) || 0;

    // Obtener valores de severidad, ocurrencia y detección
    var Severidad = consecuenciaSeveridad + seguridadFisica + medioAmbiente + impactoOperacional + costosReparacion + flexibilidadOperacional;
    document.getElementById('calculo_severidad').value = Severidad;
    var ocurrencia = document.getElementById('ocurrencia_valor').value;
    var deteccion = document.getElementById('deteccion_valor').value;

    // Aquí va la lógica de la ecuación para calcular "Ocurrencia Matemática"
    var ocurrencia_matematica = ocurrencia * 2; // Por ejemplo: ocurrencia_matematica podría ser una fórmula basada en el valor de ocurrencia.
    document.getElementById('ocurrencia_matematica').value = ocurrencia_matematica;

    // Aquí va la lógica para calcular el RPN (Risk Priority Number)
    var rpn = Severidad * ocurrencia * deteccion;// Ejemplo de fórmula: RPN = severidad * ocurrencia * detección
    document.getElementById('rpn').value = rpn;

    // Aquí va la lógica de la ecuación para determinar el "Riesgo"
    var riesgo = (rpn > 100) ? 'Alto' : 'Bajo'; // Podría basarse en valores de severidad, ocurrencia, detección, y algún umbral.
    document.getElementById('riesgo').value = riesgo;
}

// Puedes enlazar esta función a los eventos 'onchange' de los campos necesarios
document.getElementById('consecuencia_severidad_valor').addEventListener('input', actualizarCalculos);
document.getElementById('seguridad_fisica_valor').addEventListener('input', actualizarCalculos);
document.getElementById('medio_ambiente_valor').addEventListener('input', actualizarCalculos);
document.getElementById('impacto_operacional_valor').addEventListener('input', actualizarCalculos);
document.getElementById('costos_reparacion_valor').addEventListener('input', actualizarCalculos);
document.getElementById('flexibilidad_operacional_valor').addEventListener('input', actualizarCalculos);
////////////////////////////////////////////////////////////////////////////////////////////////////
document.getElementById('ocurrencia_valor').addEventListener('input', actualizarCalculos);
document.getElementById('deteccion_valor').addEventListener('input', actualizarCalculos);


