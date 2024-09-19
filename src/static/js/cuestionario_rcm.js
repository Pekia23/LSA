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
            "No": "R8"
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
            "Sí": "R7",
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

// Función para mostrar el nodo actual
function mostrarPregunta(nodeId) {
    const nodo = nodos[nodeId]; // Obtenemos el nodo actual basado en la respuesta
    const questionText = document.getElementById("questionText");

    // Actualizamos el texto de la pregunta
    questionText.textContent = nodo.pregunta;

    // Si es el nodo de fin, ocultamos los botones
    if (nodeId === "fin") {
        document.getElementById("yesBtn").style.display = "none";
        document.getElementById("noBtn").style.display = "none";
        document.getElementById("backBtn").style.display = "none";
        return;
    }

    // Mostrar los botones "Sí" y "No" si el nodo tiene respuestas
    document.getElementById("yesBtn").style.display = "inline-block";
    document.getElementById("noBtn").style.display = "inline-block";

    // Si ya hay preguntas en el historial, mostrar el botón "Volver"
    if (questionHistory.length > 0) {
        document.getElementById("backBtn").style.display = "inline-block";
    } else {
        document.getElementById("backBtn").style.display = "none";
    }

    // Actualizamos los eventos de los botones según la lógica del nodo
    document.getElementById("yesBtn").onclick = function() {
        questionHistory.push(currentNode); // Guardamos la pregunta actual antes de avanzar
        currentNode = nodo.respuestas["Sí"]; // Actualizamos al nodo siguiente según "Sí"
        mostrarPregunta(currentNode);
    };

    document.getElementById("noBtn").onclick = function() {
        questionHistory.push(currentNode); // Guardamos la pregunta actual antes de avanzar
        currentNode = nodo.respuestas["No"]; // Actualizamos al nodo siguiente según "No"
        mostrarPregunta(currentNode);
    };

    // Evento para volver a la pregunta anterior
    document.getElementById("backBtn").onclick = function() {
        if (questionHistory.length > 0) {
            currentNode = questionHistory.pop(); // Volver al último nodo del historial
            mostrarPregunta(currentNode);
        }
    };
}

// Iniciar el cuestionario cuando se abra el modal
document.getElementById("startQuizBtn").addEventListener("click", function () {
    currentNode = "inicio"; // Reiniciar el cuestionario al inicio
    questionHistory = []; // Limpiar el historial cuando se reinicia
    mostrarPregunta(currentNode);
});