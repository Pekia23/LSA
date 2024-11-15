document.addEventListener('DOMContentLoaded', () => {
    // Cambio en grupo_constructivo
    const grupoConstructivo = document.getElementById('grupo_constructivo');
    const subgrupoConstructivo = document.getElementById('subgrupo_constructivo');
    const sistema = document.getElementById('sistema');
    const equipo = document.getElementById('equipo');
    const tipoEquipo = document.getElementById('tipo_equipo');
    const addPersonalBtn = document.getElementById('add_personal');
    const deletePersonalBtn = document.getElementById('delete_personal');
    const responsable = document.getElementById('responsable');

    grupoConstructivo.addEventListener('change', () => {
        const grupoId = grupoConstructivo.value;
        if (grupoId) {
            fetch(`/api/subgrupos/${grupoId}`)
                .then(response => response.json())
                .then(data => {
                    subgrupoConstructivo.innerHTML = '<option value="">Seleccione Subgrupo Constructivo</option>';
                    data.forEach(subgrupo => {
                        subgrupoConstructivo.innerHTML += `<option value="${subgrupo.id}">${subgrupo.nombre}</option>`;
                    });
                })
                .catch(error => console.error('Error al obtener subgrupos:', error));
        } else {
            subgrupoConstructivo.innerHTML = '<option value="">Seleccione Subgrupo Constructivo</option>';
        }
        sistema.innerHTML = '<option value="">Seleccione Sistema</option>';
        equipo.innerHTML = '<option value="">Seleccione Equipo</option>';
    });

    // Cambio en subgrupo_constructivo
    subgrupoConstructivo.addEventListener('change', () => {
        const subgrupoId = subgrupoConstructivo.value;
        if (subgrupoId) {
            fetch(`/api/sistemas/${subgrupoId}`)
                .then(response => response.json())
                .then(data => {
                    sistema.innerHTML = '<option value="">Seleccione Sistema</option>';
                    data.forEach(sistemaItem => {
                        sistema.innerHTML += `<option value="${sistemaItem.id}">${sistemaItem.nombre}</option>`;
                    });
                })
                .catch(error => console.error('Error al obtener sistemas:', error));
        } else {
            sistema.innerHTML = '<option value="">Seleccione Sistema</option>';
        }
        equipo.innerHTML = '<option value="">Seleccione Equipo</option>';
    });

    // Cambio en sistema
    sistema.addEventListener('change', () => {
        const sistemaId = sistema.value;
        if (sistemaId) {
            fetch(`/api/equipos/${sistemaId}`)
                .then(response => response.json())
                .then(data => {
                    equipo.innerHTML = '<option value="">Seleccione Equipo</option>';
                    data.forEach(equipoItem => {
                        equipo.innerHTML += `<option value="${equipoItem.id}">${equipoItem.nombre}</option>`;
                    });
                })
                .catch(error => console.error('Error al obtener equipos:', error));
        } else {
            equipo.innerHTML = '<option value="">Seleccione Equipo</option>';
        }
    });

    // Cambio en tipo de equipo
    tipoEquipo.addEventListener('change', () => {
        const tipoEquipoId = tipoEquipo.value;
        if (tipoEquipoId) {
            fetch(`/api/equipos_por_tipo/${tipoEquipoId}`)
                .then(response => response.json())
                .then(data => {
                    equipo.innerHTML = '<option value="">Seleccione Equipo</option>';
                    data.forEach(equipoItem => {
                        equipo.innerHTML += `<option value="${equipoItem.id}">${equipoItem.nombre}</option>`;
                    });
                })
                .catch(error => console.error('Error al obtener equipos:', error));
        } else {
            equipo.innerHTML = '<option value="">Seleccione Equipo</option>';
        }
    });

    // Manejar agregar personal
    addPersonalBtn.addEventListener('click', () => {
        const nombreCompleto = prompt('Ingrese el nombre completo del nuevo personal:');
        if (nombreCompleto) {
            fetch('/api/crear_personal', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'nombre_completo': nombreCompleto })
            })
                .then(response => response.json())
                .then(data => {
                    responsable.innerHTML += `<option value="${data.id}">${data.nombre_completo}</option>`;
                    responsable.value = data.id;
                })
                .catch(error => alert('Error al crear personal: ' + error.message));
        }
    });

    // Manejar eliminar personal
    deletePersonalBtn.addEventListener('click', () => {
        const idPersonal = responsable.value;
        const nombrePersonal = responsable.options[responsable.selectedIndex].text;
        if (idPersonal) {
            if (confirm(`¿Está seguro que desea eliminar a ${nombrePersonal}?`)) {
                fetch('/api/eliminar_personal', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ 'id_personal': idPersonal })
                })
                    .then(response => response.json())
                    .then(() => {
                        responsable.querySelector(`option[value="${idPersonal}"]`).remove();
                        responsable.value = '';
                        alert('Personal eliminado');
                    })
                    .catch(error => alert('Error al eliminar personal: ' + error.message));
            }
        } else {
            alert('Por favor, seleccione un personal para eliminar');
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Verificar si el nombre del equipo ya existe
    const nombreEquipoInput = document.getElementById('nombre_equipo');

    if (nombreEquipoInput) {
        nombreEquipoInput.addEventListener('blur', () => {
            const nombreEquipo = nombreEquipoInput.value.trim();

            if (nombreEquipo !== '') {
                const xhr = new XMLHttpRequest();
                xhr.open('POST', '/LSA/check_nombre_equipo', true);
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

                xhr.onload = () => {
                    if (xhr.status === 200) {
                        const response = JSON.parse(xhr.responseText);
                        if (response.exists) {
                            Swal.fire({
                                icon: 'warning',
                                title: 'Nombre duplicado',
                                text: 'El nombre del equipo ya existe. Por favor, elija otro nombre.',
                                confirmButtonText: 'OK'
                            });
                            nombreEquipoInput.value = '';
                            nombreEquipoInput.focus();
                        }
                    } else {
                        console.error('Error en la solicitud AJAX');
                    }
                };

                xhr.send('nombre_equipo=' + encodeURIComponent(nombreEquipo));
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const nombreEquipoInput = document.getElementById('nombre_equipo');
    const grupoConstructivo = document.getElementById('grupo_constructivo');
    const subgrupoConstructivo = document.getElementById('subgrupo_constructivo');
    const sistema = document.getElementById('sistema');
    const equipo = document.getElementById('equipo');
    const tipoEquipo = document.getElementById('tipo_equipo');
    const submitBtn = document.getElementById('submitBtn'); // Botón para enviar el formulario

    // Función de validación
    function validarFormulario() {
        if (!nombreEquipoInput.value.trim()) {
            mostrarAlerta('El nombre del equipo es obligatorio.');
            nombreEquipoInput.focus();
            return false;
        }

        if (!grupoConstructivo.value) {
            mostrarAlerta('Debe seleccionar un grupo constructivo.');
            grupoConstructivo.focus();
            return false;
        }

        if (!subgrupoConstructivo.value) {
            mostrarAlerta('Debe seleccionar un subgrupo constructivo.');
            subgrupoConstructivo.focus();
            return false;
        }

        if (!sistema.value) {
            mostrarAlerta('Debe seleccionar un sistema.');
            sistema.focus();
            return false;
        }

        if (!equipo.value) {
            mostrarAlerta('Debe seleccionar un equipo.');
            equipo.focus();
            return false;
        }

        if (!tipoEquipo.value) {
            mostrarAlerta('Debe seleccionar un tipo de equipo.');
            tipoEquipo.focus();
            return false;
        }

        // Si todo está lleno, devuelve verdadero
        return true;
    }

    // Mostrar alerta utilizando SweetAlert
    function mostrarAlerta(mensaje) {
        Swal.fire({
            icon: 'warning',
            title: 'Formulario incompleto',
            text: mensaje,
            confirmButtonText: 'OK'
        });
    }

    // Manejar el envío del formulario
    submitBtn.addEventListener('click', (event) => {
        if (!validarFormulario()) {
            event.preventDefault(); // Evita que se envíe el formulario si la validación falla
        }
    });
});
