// Array de testimonios
const testimonials = [
    {
        text: "No sabía por dónde empezar, el mundo de las inversiones me parecía demasiado complejo. SIESIF me hizo un cuestionario claro y me dio opciones que realmente entendí, basadas en mi bajo riesgo y poco capital. ¡Por fin di el primer paso!",
        author: "Ana M., Estudiante"
    },
    {
        text: "Gracias a SIESIF pude diversificar mi portafolio de manera inteligente. El sistema analizó mi perfil y me sugirió inversiones que se ajustaban perfectamente a mis metas a mediano plazo. ¡Excelente herramienta!",
        author: "Carlos R., Profesionista"
    },
    {
        text: "Como persona mayor, me daba miedo invertir mis ahorros. SIESIF me mostró opciones seguras y conservadoras que me dieron tranquilidad. Ahora mi dinero trabaja para mí sin preocupaciones.",
        author: "María G., Jubilada"
    },
    {
        text: "Tenía algo de experiencia invirtiendo, pero SIESIF me abrió los ojos a nuevas oportunidades que no había considerado. El análisis personalizado fue clave para optimizar mis inversiones y aumentar mis rendimientos.",
        author: "Jorge L., Emprendedor"
    }
];

// Índice actual del testimonio
let currentIndex = 0;

// Elementos del DOM
const testimonialText = document.querySelector('.testimonial-text');
const testimonialAuthor = document.querySelector('.testimonial-author');
const dots = document.querySelectorAll('.dot');
const prevBtn = document.querySelector('.dot-btn.prev');
const nextBtn = document.querySelector('.dot-btn.next');

// Función para actualizar el testimonio
function updateTestimonial(index) {
    // Actualizar texto y autor con animación
    testimonialText.style.opacity = '0';
    testimonialAuthor.style.opacity = '0';
    
    setTimeout(() => {
        testimonialText.textContent = `"${testimonials[index].text}"`;
        testimonialAuthor.textContent = `-${testimonials[index].author}`;
        testimonialText.style.opacity = '1';
        testimonialAuthor.style.opacity = '1';
    }, 300);
    
    // Actualizar dots
    dots.forEach((dot, i) => {
        if (i === index) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
    
    currentIndex = index;
}

// Event listeners para los botones de navegación
prevBtn.addEventListener('click', () => {
    const newIndex = currentIndex === 0 ? testimonials.length - 1 : currentIndex - 1;
    updateTestimonial(newIndex);
});

nextBtn.addEventListener('click', () => {
    const newIndex = currentIndex === testimonials.length - 1 ? 0 : currentIndex + 1;
    updateTestimonial(newIndex);
});

// Event listeners para los dots
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        updateTestimonial(index);
    });
});

// Cambio automático cada 5 segundos
setInterval(() => {
    const newIndex = currentIndex === testimonials.length - 1 ? 0 : currentIndex + 1;
    updateTestimonial(newIndex);
}, 5000);

// Agregar estilos de transición al cargar (si no están en CSS)
if (!testimonialText.style.transition) {
    testimonialText.style.transition = 'opacity 0.3s ease';
}
if (!testimonialAuthor.style.transition) {
    testimonialAuthor.style.transition = 'opacity 0.3s ease';
}

// Soporte para teclado (accesibilidad)
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        prevBtn.click();
    } else if (e.key === 'ArrowRight') {
        nextBtn.click();
    }
});