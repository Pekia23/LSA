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