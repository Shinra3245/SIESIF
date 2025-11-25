// Lista de preguntas del cuestionario (13 preguntas completas para validar la lógica)
const questions = [
    {
        number: 1,
        question: "¿El plazo en el cual piensa lograr sus objetivos de inversión es?",
        options: [
            { value: "1", text: "a) Menos de 1 año (1)" },
            { value: "2", text: "b) Entre 1 y 3 años (2)" },
            { value: "3", text: "c) Entre 3 y 5 años (3)" },
            { value: "4", text: "d) Más de 5 años (4)" }
        ]
    },
    {
        number: 2,
        question: "¿Cuál es su nivel de experiencia en inversiones?",
        options: [
            { value: "1", text: "a) Ninguna experiencia (1)" },
            { value: "2", text: "b) Poca experiencia (2)" },
            { value: "3", text: "c) Experiencia moderada (3)" },
            { value: "4", text: "d) Mucha experiencia (4)" }
        ]
    },
    {
        number: 3,
        question: "¿Qué porcentaje de sus ahorros está dispuesto a invertir?",
        options: [
            { value: "1", text: "a) Menos del 10% (1)" },
            { value: "2", text: "b) Entre 10% y 25% (2)" },
            { value: "3", text: "c) Entre 25% y 50% (3)" },
            { value: "4", text: "d) Más del 50% (4)" }
        ]
    },
    {
        number: 4,
        question: "¿Cuál es su tolerancia al riesgo?",
        options: [
            { value: "1", text: "a) Muy baja (1)" },
            { value: "2", text: "b) Baja (2)" },
            { value: "3", text: "c) Media (3)" },
            { value: "4", text: "d) Alta (4)" }
        ]
    },
    {
        number: 5,
        question: "¿Qué haría si su inversión pierde 10% de valor en un mes?",
        options: [
            { value: "1", text: "a) Vender todo inmediatamente (1)" },
            { value: "2", text: "b) Vender una parte (2)" },
            { value: "3", text: "c) Esperar a que se recupere (3)" },
            { value: "4", text: "d) Comprar más (4)" }
        ]
    },
    {
        number: 6,
        question: "¿Cuál es su fuente principal de ingresos?",
        options: [
            { value: "1", text: "a) Inestable / Variable (1)" },
            { value: "2", text: "b) Pensiones / Ayudas (2)" },
            { value: "3", text: "c) Salario fijo / Estable (3)" },
            { value: "4", text: "d) Altos ingresos / Negocios (4)" }
        ]
    },
    {
        number: 7,
        question: "¿Qué tan importante es la liquidez (disponibilidad de efectivo) para usted?",
        options: [
            { value: "1", text: "a) Muy importante, necesito el dinero ya (1)" },
            { value: "2", text: "b) Importante (2)" },
            { value: "3", text: "c) Poco importante (3)" },
            { value: "4", text: "d) Nada importante, puedo esperar (4)" }
        ]
    },
    {
        number: 8,
        question: "¿Cuál es su objetivo principal?",
        options: [
            { value: "1", text: "a) Proteger mi dinero (1)" },
            { value: "2", text: "b) Ganarle a la inflación (2)" },
            { value: "3", text: "c) Crecer mi capital moderadamente (3)" },
            { value: "4", text: "d) Maximizar ganancias agresivamente (4)" }
        ]
    },
    {
        number: 9,
        question: "¿Tiene dependientes económicos?",
        options: [
            { value: "1", text: "a) Sí, muchos (1)" },
            { value: "2", text: "b) Sí, algunos (2)" },
            { value: "3", text: "c) Pocos (3)" },
            { value: "4", text: "d) No (4)" }
        ]
    },
    {
        number: 10,
        question: "¿Entiende cómo funcionan los mercados financieros?",
        options: [
            { value: "1", text: "a) No entiendo nada (1)" },
            { value: "2", text: "b) Conceptos básicos (2)" },
            { value: "3", text: "c) Entiendo bien (3)" },
            { value: "4", text: "d) Soy experto (4)" }
        ]
    },
    {
        number: 11,
        question: "¿Cuánto tiempo puede dejar su dinero invertido sin tocarlo?",
        options: [
            { value: "1", text: "a) Menos de 6 meses (1)" },
            { value: "2", text: "b) 6 meses a 1 año (2)" },
            { value: "3", text: "c) 1 a 5 años (3)" },
            { value: "4", text: "d) Más de 5 años (4)" }
        ]
    },
    {
        number: 12,
        question: "¿Qué prefiere: seguridad o rendimiento?",
        options: [
            { value: "1", text: "a) 100% Seguridad (1)" },
            { value: "2", text: "b) Mayormente seguridad (2)" },
            { value: "3", text: "c) Balanceado (3)" },
            { value: "4", text: "d) Máximo rendimiento (4)" }
        ]
    },
    {
        number: 13,
        question: "¿Cómo reacciona ante las noticias financieras negativas?",
        options: [
            { value: "1", text: "a) Me asusto mucho (1)" },
            { value: "2", text: "b) Me preocupo (2)" },
            { value: "3", text: "c) Me mantengo informado (3)" },
            { value: "4", text: "d) Busco oportunidades (4)" }
        ]
    }
];

// Variables globales
let currentQuestionIndex = 0;
let answers = [];

// Elementos del DOM
const questionNumber = document.getElementById('questionNumber');
const questionTitle = document.getElementById('questionTitle');
const optionsContainer = document.getElementById('optionsContainer');
const btnNext = document.getElementById('btnNext');

// Función para mostrar la pregunta actual
function showQuestion() {
    const current = questions[currentQuestionIndex];
    
    // Actualizar número y título
    questionNumber.textContent = `${current.number}.`;
    questionTitle.textContent = current.question;
    
    // Limpiar opciones anteriores
    optionsContainer.innerHTML = '';
    
    // Crear nuevas opciones
    current.options.forEach((option) => {
        const label = document.createElement('label');
        label.className = 'option-item';
        
        const input = document.createElement('input');
        input.type = 'radio';
        input.name = 'answer';
        input.value = option.value;
        input.className = 'option-radio';
        
        const span = document.createElement('span');
        span.className = 'option-text';
        span.textContent = option.text;
        
        label.appendChild(input);
        label.appendChild(span);
        optionsContainer.appendChild(label);
    });
    
    // Añadir lógica de selección visual
    const optionItems = optionsContainer.querySelectorAll('.option-item');
    optionItems.forEach(item => {
        item.addEventListener('click', function() {
            optionItems.forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');
            const radio = this.querySelector('.option-radio');
            if (radio) radio.checked = true;
        });
    });
}

// Función para ir a la siguiente pregunta
function nextQuestion() {
    const selectedOption = document.querySelector('input[name="answer"]:checked');
    
    if (!selectedOption) {
        alert('Por favor selecciona una opción');
        return;
    }
    
    answers.push({
        question: questions[currentQuestionIndex].number,
        answer: selectedOption.value
    });
    
    currentQuestionIndex++;
    
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        finishQuestionnaire();
    }
}

// Función para finalizar y conectar con el Backend
async function finishQuestionnaire() {
    console.log('Enviando respuestas al Sistema Experto...');
    
    const btnNext = document.getElementById('btnNext');
    if(btnNext) {
        btnNext.textContent = "Analizando...";
        btnNext.disabled = true;
    }

    // Transformar respuestas al formato { "p1": 1, "p2": 3 ... }
    const respuestasBackend = {};
    answers.forEach(item => {
        respuestasBackend[`p${item.question}`] = parseInt(item.answer);
    });

    try {
        const response = await fetch('http://127.0.0.1:5000/api/evaluar-perfil', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ respuestas: respuestasBackend })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || `Error ${response.status}`);
        }

        const resultado = await response.json();
        console.log("Respuesta del Sistema Experto:", resultado);

        // Guardar resultado y redirigir
        localStorage.setItem('siesif_resultado', JSON.stringify(resultado));
        window.location.href = 'puntaje.html';

    } catch (error) {
        console.error('Error:', error);
        alert('Error al conectar con el servidor: ' + error.message);
        if(btnNext) {
            btnNext.textContent = "Reintentar";
            btnNext.disabled = false;
        }
    }
}

// Event Listener
btnNext.addEventListener('click', nextQuestion);

// Iniciar
showQuestion();