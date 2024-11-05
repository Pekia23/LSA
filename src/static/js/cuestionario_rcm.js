// Definición de nodos (preguntas y respuestas)
const nodos = {
    "inicio": {
        pregunta: "Ejecutar cuestionario RCM",
        respuestas: {
            "Sí": "P1",
            "No": "fin"
        }
    },
    "P1": {
        pregunta: "¿Será evidente a los operarios la pérdida de función causada por este modo de fallos actuando por sí solo con circunstancias normales?",
        respuestas: {
            "Sí": "P7",
            "No": "P2"
        }
    },
    "P2": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea a condición?",
        respuestas: {
            "Sí": "R1",
            "No": "P3"
        }
    },
    "P3": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea de reacondicionamiento cíclico?",
        respuestas: {
            "Sí": "R2",
            "No": "P4"
        }
    },
    "P4": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea de sustitución cíclica?",
        respuestas: {
            "Sí": "R3",
            "No": "P5"
        }
    },
    "P5": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea en búsqueda de fallas?",
        respuestas: {
            "Sí": "R4",
            "No": "P6"
        }
    },
    "P6": {
        pregunta: "¿Podrá la falla múltiple afectar a la seguridad o al medio ambiente?",
        respuestas: {
            "Sí": "R5",
            "No": "R6"
        }
    },
    "P7": {
        pregunta: "¿Este modo de falla puede generar una pérdida de función u otros daños que pudieran lesionar o matar a alguien?",
        respuestas: {
            "Sí": "P8",
            "No": "P12"
        }
    },
    "P8": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea a condición?",
        respuestas: {
            "Sí": "R1",
            "No": "P9"
        }
    },
    "P9": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea de reacondicionamiento cíclico?",
        respuestas: {
            "Sí": "R2",
            "No": "P10"
        }
    },
    "P10": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea de sustitución cíclica?",
        respuestas: {
            "Sí": "R3",
            "No": "P11"
        }
    },
    "P11": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una combinación de tareas?",
        respuestas: {
            "Sí": "R7",
            "No": "R5"
        }
    },
    "P12": {
        pregunta: "¿Produce este modo de falla una pérdida de función u otros daños que pudieran infringir cualquier normativa o reglamento de medio ambiente?",
        respuestas: {
            "Sí": "P8",
            "No": "P16"
        }
    },
    "P16": {
        pregunta: "¿Ejerce el modo de falla un efecto adverso directo sobre la capacidad operacional?",
        respuestas: {
            "Sí": "P17",
            "No": "P17"
        }
    },
    "P17": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea a condición?",
        respuestas: {
            "Sí": "R1",
            "No": "P18"
        }
    },
    "P18": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea de reacondicionamiento?",
        respuestas: {
            "Sí": "R2",
            "No": "P19"
        }
    }, 
    "P19": {
        pregunta: "¿Es técnicamente factible y merece la pena realizar una tarea de sustitución cíclica?",
        respuestas: {
            "Sí": "R3",
            "No": "R8"
        }
    }, 

    "R1": {
        pregunta: "Tarea a condición",
        respuestas: {
            "Fin": "fin"
        }
    },
    "R2": {
        pregunta: "Tarea de reacondicionamiento",
        respuestas: {
            "Fin": "fin"
        }
    },
    "R3": {
        pregunta: "Tarea de sustitución",
        respuestas: {
            "Fin": "fin"
        }
    },
    "R4": {
        pregunta: "Tareas de búsqueda de fallas",
        respuestas: {
            "Fin": "fin"
        }
    },
    "R5": {
        pregunta: "El rediseño es obligatorio",
        respuestas: {
            "Fin": "fin"
        }
    },
    "R6": {
        pregunta: "Ningún mantenimiento programado",
        respuestas: {
            "Fin": "fin"
        }
    },
    "R7": {
        pregunta: "Hacer combinación de tareas",
        respuestas: {
            "Fin": "fin"
        }
    },
    "R8": {
        pregunta:"Ningún Mantenimiento proactivo" ,
        respuestas: {
            "Fin": "fin"
        }
    },
    "fin": {
        pregunta: "Fin del cuestionario.",
        respuestas: {}
    }
};

// Variables para controlar el flujo del cuestionario
let currentNode = "inicio";
let questionHistory = []; // Historial de las preguntas anteriores
let contadorRespuestas = 1; // Iniciamos un contador para ir llenando los inputs secuencialmente
let respuestas = {}; // Almacena las respuestas asociadas a cada pregunta

// Función para mostrar el nodo actual
function mostrarPregunta(nodeId) {
    const nodo = nodos[nodeId]; // Obtenemos el nodo actual basado en la respuesta
    const questionText = document.getElementById("questionText");

    // Actualizamos el texto de la pregunta
    questionText.textContent = nodo.pregunta;

    // Si es el nodo de fin, ocultamos todos los botones
    if (nodeId === "fin") {
        ocultarBotones(); // Aseguramos que todos los botones estén ocultos
        return;
    }

    if (["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"].includes(currentNode)) {
        guardarPreguntaEnCuestionarioRCM10(nodo.pregunta);
    }

    // Mostrar los botones "Sí" y "No" solo si el nodo tiene respuestas disponibles
    if (nodo.respuestas["Sí"] && nodo.respuestas["No"]) {
        document.getElementById("yesBtn").style.display = "inline-block";
        document.getElementById("noBtn").style.display = "inline-block";
    } else {
        ocultarBotones();
    }

    // Si ya hay preguntas en el historial, mostrar el botón "Volver"
    if (questionHistory.length > 0) {
        document.getElementById("backBtn").style.display = "inline-block";
    } else {
        document.getElementById("backBtn").style.display = "none";
    }



    // Actualizamos los eventos de los botones según la lógica del nodo
    document.getElementById("yesBtn").onclick = function() {
        if (currentNode !== "inicio") { // No guardar si es el nodo de inicio
            guardarRespuesta(currentNode, "Sí");
        }
        questionHistory.push(currentNode); // Guardamos la pregunta actual antes de avanzar
        currentNode = nodo.respuestas["Sí"]; // Actualizamos al nodo siguiente según "Sí"
        ocultarBotones(); // Ocultamos los botones inmediatamente
        mostrarPregunta(currentNode); // Mostramos la siguiente pregunta
    };

    document.getElementById("noBtn").onclick = function() {
        if (currentNode !== "inicio") { // No guardar si es el nodo de inicio
            guardarRespuesta(currentNode, "No");
        }
        questionHistory.push(currentNode); // Guardamos la pregunta actual antes de avanzar
        currentNode = nodo.respuestas["No"]; // Actualizamos al nodo siguiente según "No"
        ocultarBotones(); // Ocultamos los botones inmediatamente
        mostrarPregunta(currentNode); // Mostramos la siguiente pregunta
    };

    // Evento para volver a la pregunta anterior
    document.getElementById("backBtn").onclick = function() {
        if (questionHistory.length > 0) {
            const preguntaAnterior = questionHistory.pop(); // Volver al último nodo del historial
            volverAtras(preguntaAnterior); // Actualizamos la respuesta cuando se vuelve atrás
            currentNode = preguntaAnterior;
            mostrarPregunta(currentNode); // Mostramos la pregunta anterior
        }
    };
}

function guardarPreguntaEnCuestionarioRCM10(pregunta) {
    const inputElement = document.getElementById("cuestionario_rcm10");
    if (inputElement) {
        inputElement.value = pregunta;
    }
}

// Función para ocultar todos los botones
function ocultarBotones() {
    document.getElementById("yesBtn").style.display = "none";
    document.getElementById("noBtn").style.display = "none";
    document.getElementById("backBtn").style.display = "none";
}


// Función para guardar la respuesta
function guardarRespuesta(preguntaId, respuesta) {
    // Si ya respondimos esta pregunta antes, actualizamos su input

    if (respuestas[preguntaId]) {
        const inputId = respuestas[preguntaId]; // Obtenemos el id del input correspondiente
        const inputElement = document.getElementById(inputId);
        if (inputElement) {
            inputElement.value = respuesta; // Actualizamos la respuesta

        }
    } else {
        // Si es una nueva respuesta, llenamos el siguiente input secuencial
        const inputId = `cuestionario_rcm${contadorRespuestas}`; // Generamos el id del input correspondiente
        const inputElement = document.getElementById(inputId); // Obtenemos el input correspondiente
        
        if (inputElement) {
            inputElement.value = respuesta; // Guardamos la respuesta en el input
            respuestas[preguntaId] = inputId; // Almacenamos la relación de la pregunta con el input
            contadorRespuestas++; // Incrementamos el contador
        }
    }
}

// Función para retroceder en el cuestionario
function volverAtras(preguntaId) {
    const inputId = respuestas[preguntaId]; // Obtenemos el id del input asociado con la pregunta
    if (inputId) {
        const inputElement = document.getElementById(inputId);
        if (inputElement) {
            inputElement.value = ""; // Borramos la respuesta del input al retroceder
            contadorRespuestas--; // Reducimos el contador ya que volvemos atrás
        }
    }
}

// Iniciar el cuestionario cuando se abra el modal
document.getElementById("startQuizBtn").addEventListener("click", function () {
    currentNode = "inicio"; // Reiniciar el cuestionario al inicio
    questionHistory = []; // Limpiar el historial cuando se reinicia
    respuestas = {}; // Limpiar las respuestas anteriores
    contadorRespuestas = 1; // Reiniciar el contador
    mostrarPregunta(currentNode);
});
