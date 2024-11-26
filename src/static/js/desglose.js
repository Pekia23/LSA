document.addEventListener('DOMContentLoaded', function () {
    const searchbox = document.getElementById('searchbox');
    const buscarBtn = document.getElementById('buscarBtn');
    const resultados = document.getElementById('resultados');
    const volverBtn = document.getElementById('volverBtn');
    let currentView = 'grupo';  // Para saber en qué vista estamos (grupo, subgrupo, sistema, equipo)

    // Variables para almacenar los IDs actuales
    let currentGroupId = null;
    let currentSubgroupId = null;
    let currentSystemId = null;

    // Actualizar el placeholder inicialmente
    actualizarPlaceholder();

    // Buscar por nombre (contextual)
    buscarBtn.addEventListener('click', function () {
        let query = searchbox.value.trim();
        if (query === '') {
            Swal.fire({
                icon: 'warning',
                title: 'Campo vacío',
                text: 'Por favor, ingrese un término de búsqueda.',
                confirmButtonText: 'OK'
            });
            return;
        }

        let apiUrl = '';
        let type = '';

        if (currentView === 'grupo') {
            // Búsqueda global de equipos
            apiUrl = `/api/buscar_equipos?busqueda=${encodeURIComponent(query)}`;
            type = 'equipo';
        } else if (currentView === 'subgrupo') {
            if (!currentGroupId) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Sin grupo seleccionado',
                    text: 'Por favor, seleccione un grupo constructivo.',
                    confirmButtonText: 'OK'
                });
                return;
            }
            apiUrl = `/api/buscar_subgrupos?busqueda=${encodeURIComponent(query)}&id_grupo=${currentGroupId}`;
            type = 'subgrupo';
        } else if (currentView === 'sistema') {
            if (!currentSubgroupId) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Sin subgrupo seleccionado',
                    text: 'Por favor, seleccione un subgrupo.',
                    confirmButtonText: 'OK'
                });
                return;
            }
            apiUrl = `/api/buscar_sistemas?busqueda=${encodeURIComponent(query)}&id_subgrupo=${currentSubgroupId}`;
            type = 'sistema';
        } else if (currentView === 'equipo') {
            if (!currentSystemId) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Sin sistema seleccionado',
                    text: 'Por favor, seleccione un sistema.',
                    confirmButtonText: 'OK'
                });
                return;
            }
            apiUrl = `/api/buscar_equipos?busqueda=${encodeURIComponent(query)}&id_sistema=${currentSystemId}`;
            type = 'equipo';
        }

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                resultados.innerHTML = '';
                if (data.length === 0) {
                    resultados.innerHTML = '<p>No se encontraron resultados.</p>';
                } else {
                    data.forEach(item => {
                        let card = document.createElement('div');
                        card.classList.add('card', 'dynamic-card');  // Añadir las clases 'card' y 'dynamic-card'

                        card.setAttribute('data-id', item.id);
                        card.setAttribute('data-type', type);

                        if (type === 'grupo' || type === 'subgrupo' || type === 'sistema') {
                            card.innerHTML = `<p>${item.numeracion ? item.numeracion + ' - ' : ''}${item.nombre}</p>`;
                        } else if (type === 'equipo') {
                            card.innerHTML = `<p>${item.nombre_equipo}</p>`;
                        }

                        resultados.appendChild(card);
                    });
                }
            })
            .catch(error => {
                Swal.fire({
                    icon: 'error',
                    title: 'Error en la búsqueda',
                    text: 'Hubo un error al realizar la búsqueda. Inténtalo de nuevo más tarde.',
                    confirmButtonText: 'OK'
                });
                console.error('Error en la búsqueda:', error);
            });
    });

    // Lógica para manejar el click en los cuadros
    document.addEventListener('click', function (event) {
        if (event.target.closest('.card')) {
            const card = event.target.closest('.card');
            const id = card.getAttribute('data-id');
            const type = card.getAttribute('data-type');

            if (type === 'grupo') {
                currentGroupId = id;
                currentSubgroupId = null;
                currentSystemId = null;

                fetch(`/api/subgrupos/${id}`)
                    .then(response => response.json())
                    .then(data => mostrarTarjetas(data, 'subgrupo'))
                    .catch(error => console.error('Error:', error));
            } else if (type === 'subgrupo') {
                currentSubgroupId = id;
                currentSystemId = null;

                fetch(`/api/sistemas/${id}`)
                    .then(response => response.json())
                    .then(data => mostrarTarjetas(data, 'sistema'))
                    .catch(error => console.error('Error:', error));
            } else if (type === 'sistema') {
                currentSystemId = id;

                fetch(`/api/equipos/${id}`)
                    .then(response => response.json())
                    .then(data => mostrarTarjetas(data, 'equipo'))
                    .catch(error => console.error('Error:', error));
            } else if (type === 'equipo') {
                const nombre_equipo = card.querySelector('p').textContent.trim(); // Obtener el nombre del equipo desde la tarjeta
                
                // Hacer una petición POST al backend para mostrar la información del equipo
                fetch('/LSA/mostrar-general', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ nombre_equipo: nombre_equipo }) // Enviar nombre_equipo al backend
                })
                .then(response => {
                    if (response.redirected) {
                        window.location.href = response.url; // Seguir la redirección del backend
                    } else {
                        console.error('Error en la redirección');
                    }
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Error en la redirección',
                        text: 'Hubo un error al procesar la redirección. Inténtalo de nuevo más tarde.',
                        confirmButtonText: 'OK'
                    });
                    console.error('Error en la petición POST:', error);
                });
            }
        }
    });

    function mostrarTarjetas(data, type) {
        resultados.innerHTML = ''; // Limpiar los resultados anteriores

        data.forEach(item => {
            let card = document.createElement('div');
            card.classList.add('card');
    
            card.setAttribute('data-id', item.id);
            card.setAttribute('data-type', type);
    
            if (type === 'grupo') {
                card.classList.add('card');
                let imageSrc = item.numeracion == 200 ? 'img/1.png' :
                               item.numeracion == 300 ? 'img/2.png' :
                               item.numeracion == 400 ? 'img/3.png' :
                               item.numeracion == 500 ? 'img/4.png' :
                               item.numeracion == 600 ? 'img/5.png' : 'img/6.png';
                card.innerHTML = `<img src="/static/${imageSrc}" alt="Grupo"><p>${item.nombre}</p>`;
            } else if (type === 'subgrupo' || type === 'sistema') {
                card.classList.add('dynamic-card');
                card.innerHTML = `<h1>${item.numeracion}</h1><p>${item.nombre}</p>`;
            } else if (type === 'equipo') {
                // Verificar cuál es el nombre de la propiedad del equipo
                card.classList.add('dynamic-card');
                const nombreEquipo = item.nombre_equipo || item.nombre || item.equipo || 'Nombre no disponible';
                card.innerHTML = `<p>${nombreEquipo}</p>`;
            }
    
            resultados.appendChild(card);
        });
    
        currentView = type;
        actualizarPlaceholder();
    
        // Mostrar o esconder botón de volver
        volverBtn.classList.toggle('hidden', currentView === 'grupo');
    }
    

    // Función para actualizar el placeholder del buscador
    function actualizarPlaceholder() {
        if (currentView === 'grupo') {
            searchbox.placeholder = 'Buscar equipos';
        } else if (currentView === 'subgrupo') {
            searchbox.placeholder = 'Buscar subgrupos';
        } else if (currentView === 'sistema') {
            searchbox.placeholder = 'Buscar sistemas';
        } else if (currentView === 'equipo') {
            searchbox.placeholder = 'Buscar equipos';
        }
    }

    // Manejar el botón de volver
    volverBtn.addEventListener('click', function () {
        if (currentView === 'subgrupo') {
            currentView = 'grupo';
            currentSubgroupId = null;
            currentSystemId = null;

            fetch(`/api/grupos`)
                .then(response => response.json())
                .then(data => mostrarTarjetas(data, 'grupo'))
                .catch(error => console.error('Error:', error));
        } else if (currentView === 'sistema') {
            currentView = 'subgrupo';
            currentSystemId = null;

            fetch(`/api/subgrupos/${currentGroupId}`)
                .then(response => response.json())
                .then(data => mostrarTarjetas(data, 'subgrupo'))
                .catch(error => console.error('Error:', error));
        } else if (currentView === 'equipo') {
            currentView = 'sistema';

            fetch(`/api/sistemas/${currentSubgroupId}`)
                .then(response => response.json())
                .then(data => mostrarTarjetas(data, 'sistema'))
                .catch(error => console.error('Error:', error));
        }

        // Actualizar el placeholder según la vista actual
        actualizarPlaceholder();
    });
});