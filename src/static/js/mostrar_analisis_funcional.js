function get_id(id) {
    // Seleccionar todos los elementos con la clase 'componentes'
    let componentes = document.querySelectorAll('.componentes');
    // Seleccionar el elemento específico usando la clase 'comp_' + id
    let table_comp = document.querySelector(`.comp_${id}`);

    // Iterar sobre cada elemento en 'componentes'
    componentes.forEach(element => {
        // Si el elemento no coincide con 'table_comp', se oculta
        if (element !== table_comp) {
            element.hidden = true;
        }
    });

    // Alternar visibilidad del elemento específico
    table_comp.hidden = !table_comp.hidden;
}

// Función para confirmar la eliminación utilizando SweetAlert2
function confirmarEliminacion(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto

    Swal.fire({
        title: '¿Estás seguro?',
        text: "Esta acción no se puede deshacer",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Si el usuario confirma, se envía el formulario
            event.target.closest('form').submit();
        }
    });
}

// Función para confirmar la edición utilizando SweetAlert2
function confirmarEdicion(event) {
    event.preventDefault(); // Prevenir la redirección por defecto

    Swal.fire({
        title: '¿Deseas editar este análisis?',
        text: "Se guardarán los cambios realizados.",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, continuar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Redirigir si el usuario confirma
            window.location.href = event.target.href;
        }
    });
}

// Agregar los event listeners para eliminar y editar
document.addEventListener('DOMContentLoaded', () => {
    const botonesEliminar = document.querySelectorAll('form button.btn-danger');
    botonesEliminar.forEach(boton => {
        boton.addEventListener('click', confirmarEliminacion);
    });

    const botonesEditar = document.querySelectorAll('a.boton');
    botonesEditar.forEach(boton => {
        boton.addEventListener('click', confirmarEdicion);
    });
});