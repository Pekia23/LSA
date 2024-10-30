
editar = document.getElementById('codigo_modo_falla').getAttribute('data-editar');

console.log(editar)
if (editar == 'True') {
    window.onload = event => {
        console.log("Hola, mundo")
        // console.log(event.target)
        actualizarDetallesFalla()
        actualizarNombreFalla()
        actualizarValoresConOnChange('Severidad')
        actualizarValoresConOnChange('Riesgo')
        actualizarCalculos()
    }
}



function actualizarDetallesFalla() {
    const mecanismoId = document.getElementById('mecanismo_falla').value;
    
    // Realizar una petición GET al backend con el id del mecanismo seleccionado
    fetch(`/LSA/obtener-detalles-falla/${mecanismoId}`)
        .then(response => response.json())
        .then(data => {
            const detalleFallaSelect = document.getElementById('detalle_falla');
            detalleFallaSelect.innerHTML = '<option value="" disabled selected>---- Selecciona Detalle de Falla ----</option>';

            
            // Recorrer los detalles y agregarlos como opciones al select

            data.forEach(detalle => {
                const option = document.createElement('option');
                option.value = detalle.id;
                option.text = detalle.nombre;
                detalleFallaSelect.appendChild(option);
            });


            // Si estamos en modo de edición, seleccionar la opción correspondiente
            if (editar === 'True') {
                // Obtener el valor del detalle de falla desde el atributo data-detallefalla
                const detalleFallaGuardado = detalleFallaSelect.getAttribute('data-detallefalla');
                console.log(detalleFallaGuardado)
                // Verificar si el valor almacenado coincide con alguna de las opciones y seleccionarla
                if (detalleFallaGuardado) {
                    // Iterar sobre las opciones para seleccionar la que coincida
                    for (let option of detalleFallaSelect.options) {
                        if (option.text === detalleFallaGuardado || option.value === detalleFallaGuardado) {
                            option.selected = true;
                            break;
                        }
                    }
                }
            }

        })
        .catch(error => console.error('Error al cargar los detalles de falla:', error));
}




function actualizarNombreFalla() {//documentred onload

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

function actualizarValoresConOnChange(nombreClasePadre) {
    const contenedorDiv = document.querySelector(`.${nombreClasePadre}`);
    if (!contenedorDiv) {
        console.error(`No se encontró ningún contenedor con la clase: ${nombreClasePadre}`);
        return;
    }
    // Buscar todos los selects dentro del contenedor que tienen el atributo onchange
    const selectsConOnChange = contenedorDiv.querySelectorAll('select[onchange]');
    console.log(selectsConOnChange)
    //mostrar alerta si no se encuentran atributos con onchange
    if (selectsConOnChange.length === 0) {
        console.warn('No se encontraron selects con el atributo onchange en el contenedor con la clase:', nombreClasePadre);
        return;
    }
    selectsConOnChange.forEach(selectElement => {
        const inputId = `${selectElement.id}_valor`;
        const inputElement = document.getElementById(inputId);

        if (inputElement) {
            actualizarValor(selectElement.id, inputId);
        }
    });
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

 // Declarar la lista de riesgos globalmente para que esté disponible para cualquier función
const listaRiesgos = JSON.parse(document.getElementById('id_riesgo').getAttribute('data-riesgos'));
function actualizarCalculos() {
    // Cálculos previos para obtener el valor de RPN
    var consecuenciaSeveridad = parseFloat(document.getElementById('fallo_oculto_valor').value) || 0;

    var seguridadFisica = parseFloat(document.getElementById('seguridad_fisica_valor').value) || 0;
    var medioAmbiente = parseFloat(document.getElementById('medio_ambiente_valor').value) || 0;
    var impactoOperacional = parseFloat(document.getElementById('impacto_operacional_valor').value) || 0;
    var costosReparacion = parseFloat(document.getElementById('costos_reparacion_valor').value) || 0;
    var flexibilidadOperacional = parseFloat(document.getElementById('flexibilidad_operacional_valor').value) || 0;

    //calculo original
    var Severidad = consecuenciaSeveridad * 0.05 + seguridadFisica * 0.2 + medioAmbiente * 0.1 + impactoOperacional * 0.3 + costosReparacion * 0.3+ flexibilidadOperacional * 0.05;
    document.getElementById('calculo_severidad').value = Severidad;

    var ocurrencia = parseFloat(document.getElementById('ocurrencia_valor').value) || 0;
    var deteccion = parseFloat(document.getElementById('probabilidad_deteccion_valor').value) || 0;

    var ocurrencia_matematica = ocurrencia*2;
    document.getElementById('ocurrencia_matematica').value = ocurrencia_matematica;

    var rpn = (Severidad * ocurrencia * deteccion)/100;
    document.getElementById('rpn').value = rpn;

    // Leer la lista de riesgos desde el atributo data-riesgos
    const riesgosInput = document.getElementById('riesgo');
    const listaRiesgos = JSON.parse(riesgosInput.getAttribute('data-riesgos'));

    // Determinar el riesgo según el RPN
    let nombreRiesgo;
    if (rpn >= 75) {
        nombreRiesgo = 'MUY CRITICO';
    } else if (rpn >= 50) {
        nombreRiesgo = 'CRITICO';
    } else if (rpn >= 25) {
        nombreRiesgo = 'SEMI-CRITICO';
    } else {
        nombreRiesgo = 'NO CRITICO';
    }

    // Buscar el id del riesgo correspondiente en la lista de riesgos
    const idRiesgo = listaRiesgos.find(riesgo => riesgo.nombre === nombreRiesgo)?.id || null;

    // Asignar el nombre del riesgo al campo de texto
    document.getElementById('riesgo').value = nombreRiesgo;

    // Guardar el id del riesgo en el campo oculto para enviar al backend
    document.getElementById('id_riesgo').value = idRiesgo;

    // Debug: Mostrar en la consola para verificar
    console.log("Riesgo seleccionado:", nombreRiesgo);
    console.log("ID del riesgo calculado:", idRiesgo);
}

// Puedes enlazar esta función a los eventos 'onchange' de los campos necesarios
document.getElementById('fallo_oculto_valor').addEventListener('input', actualizarCalculos);
document.getElementById('seguridad_fisica_valor').addEventListener('input', actualizarCalculos);
document.getElementById('medio_ambiente_valor').addEventListener('input', actualizarCalculos);
document.getElementById('impacto_operacional_valor').addEventListener('input', actualizarCalculos);
document.getElementById('costos_reparacion_valor').addEventListener('input', actualizarCalculos);
document.getElementById('flexibilidad_operacional_valor').addEventListener('input', actualizarCalculos);
////////////////////////////////////////////////////////////////////////////////////////////////////
document.getElementById('ocurrencia_valor').addEventListener('input', actualizarCalculos);

document.getElementById('probabilidad_deteccion_valor').addEventListener('input', actualizarCalculos);


