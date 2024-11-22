document.addEventListener('DOMContentLoaded', function () {
    // Función para seleccionar o deseleccionar todas las herramientas de seguridad
    document.getElementById('select-all-seguridad').addEventListener('change', function () {
        let checkboxes = document.querySelectorAll('#seguridad .form-check-input');
        checkboxes.forEach(checkbox => checkbox.checked = this.checked);
    });

    // Función para seleccionar o deseleccionar todas las herramientas de soporte
    document.getElementById('select-all-soporte').addEventListener('change', function () {
        let checkboxes = document.querySelectorAll('#soporte .form-check-input');
        checkboxes.forEach(checkbox => checkbox.checked = this.checked);
    });

    // Función para seleccionar o deseleccionar todas las herramientas generales
    document.getElementById('select-all-generales').addEventListener('change', function () {
        let checkboxes = document.querySelectorAll('#generales .form-check-input');
        checkboxes.forEach(checkbox => checkbox.checked = this.checked);
    });

    // Función para redirigir a la segunda vista del MTA
    document.getElementById('btn-siguiente').addEventListener('click', function () {
        window.location.href = 'registro-mta-2';  // Asegúrate de tener esta ruta configurada en Flask
    });
    
    const operarioOptions = {
        "1": [
            { value: "operario_1", text: "Nivel operador" },
            { value: "operario_2", text: "Técnicas de nivel aprendiz" }
        ],
        "2": [
            { value: "operario_3", text: "Técnico intermedio con curso básico del equipo" }
        ],
        "3": [
            { value: "operario_4", text: "Técnicos del más alto nivel" }
        ],
        "4": [
            { value: "operario_5", text: "Grupo de trabajo con experiencia" },
            { value: "operario_6", text: "Técnicos bajo dirección de un ingeniero" }
        ],
        "5": [
            { value: "operario_8", text: "Apoyo permanente del fabricante" },
            { value: "operario_9", text: "Apoyo de talleres especializados" }
        ]
    };

    const nivelSelect = document.getElementById('nivel_lora');
    const operarioSelect = document.getElementById('operario_lora');

    // Función para cargar todas las opciones inicialmente
    function loadAllOperarioOptions() {
        operarioSelect.innerHTML = ''; // Limpia el select

        Object.values(operarioOptions).flat().forEach(option => {
            const opt = document.createElement('option');
            opt.value = option.value;
            opt.textContent = option.text;
            operarioSelect.appendChild(opt);
        });
    }

    // Función para filtrar las opciones según el nivel
    function filterOperarioOptions() {
        const selectedNivel = nivelSelect.value;

        if (selectedNivel) {
            // Limpia las opciones actuales
            operarioSelect.innerHTML = '';

            // Agrega solo las opciones correspondientes al nivel seleccionado
            operarioOptions[selectedNivel].forEach(option => {
                const opt = document.createElement('option');
                opt.value = option.value;
                opt.textContent = option.text;
                operarioSelect.appendChild(opt);
            });
        }
    }

    // Escucha cambios en el nivel seleccionado
    nivelSelect.addEventListener('change', filterOperarioOptions);

    // Cargar todas las opciones al cargar la página
    loadAllOperarioOptions();
});

