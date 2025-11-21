// Lista de preguntas del cuestionario
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
    }
    // Agrega más preguntas según necesites
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
    current.options.forEach((option, index) => {
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
    
    // Animación de entrada
    const questionCard = document.querySelector('.question-card');
    questionCard.style.animation = 'none';
    setTimeout(() => {
        questionCard.style.animation = 'fadeIn 0.5s ease-in';
    }, 10);
}

// Función para ir a la siguiente pregunta
function nextQuestion() {
    // Obtener respuesta seleccionada
    const selectedOption = document.querySelector('input[name="answer"]:checked');
    
    if (!selectedOption) {
        alert('Por favor selecciona una opción');
        return;
    }
    
    // Guardar respuesta
    answers.push({
        question: currentQuestionIndex + 1,
        answer: selectedOption.value,
        questionText: questions[currentQuestionIndex].question
    });
    
    // Limpiar selección
    selectedOption.checked = false;
    
    // Avanzar a la siguiente pregunta
    currentQuestionIndex++;
    
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        // Cuestionario completado
        finishQuestionnaire();
    }
}

// Función para finalizar el cuestionario
function finishQuestionnaire() {
    console.log('Respuestas del usuario:', answers);
    
    // Calcular puntaje
    const totalScore = answers.reduce((sum, ans) => sum + parseInt(ans.answer), 0);
    
    console.log('Puntaje total:', totalScore);
    
    // Aquí puedes mostrar resultados, enviar a servidor, etc.
    alert(`Cuestionario completado!\nPuntaje total: ${totalScore}`);
    
    // Opcional: mostrar resultados en la página
    showResults(totalScore);
}

// Función para mostrar resultados (opcional)
function showResults(score) {
    const questionCard = document.querySelector('.question-card');
    questionCard.innerHTML = `
        <h3 class="question-number">Resultados</h3>
        <h4 class="question-title">Tu puntaje es: ${score}</h4>
        <div class="options-box">
            <p style="color: white; font-size: 18px; line-height: 1.8;">
                Basado en tus respuestas, te recomendamos...
                <br><br>
                ${getRecommendation(score)}
            </p>
        </div>
    `;
}

// Función para obtener recomendación basada en el puntaje
function getRecommendation(score) {
    if (score <= 8) {
        return "Un perfil de inversión conservador con instrumentos de bajo riesgo como bonos gubernamentales y CETES.";
    } else if (score <= 12) {
        return "Un perfil de inversión moderado con una combinación de bonos y acciones de empresas estables.";
    } else if (score <= 14) {
        return "Un perfil de inversión moderado-agresivo con mayor exposición a acciones y fondos de inversión.";
    } else {
        return "Un perfil de inversión agresivo con instrumentos de alto rendimiento como acciones individuales y derivados.";
    }
}

// Event Listener para el botón
btnNext.addEventListener('click', nextQuestion);

// Inicializar el cuestionario
showQuestion();