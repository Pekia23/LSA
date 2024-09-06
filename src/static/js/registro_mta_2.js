document.addEventListener('DOMContentLoaded', function () {
    // Redirige a la primera vista de MTA cuando se presiona el botón 'Anterior'
    document.getElementById('btn-anterior').addEventListener('click', function () {
        window.location.href = '/mta/primera';  // Asegúrate de tener esta ruta configurada en Flask
    });

    // Acción para el botón de agregar MTA
    document.getElementById('btn-agregar-mta').addEventListener('click', function () {
        // Aquí puedes agregar la lógica para enviar los datos a la API o hacer otra acción
        alert("MTA agregado exitosamente");
    });
});
