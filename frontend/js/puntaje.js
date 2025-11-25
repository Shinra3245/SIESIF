document.addEventListener('DOMContentLoaded', () => {
    // 1. Recuperar los datos del análisis
    const data = localStorage.getItem('siesif_resultado');

    if (!data) {
        console.warn("No se encontraron datos en localStorage. Redirigiendo...");
        // Si no hay datos, podrías redirigir al inicio
        // window.location.href = 'index.html';
        return;
    }

    const resultado = JSON.parse(data);
    console.log("Datos recuperados en puntaje.html:", resultado); // DEBUG: Ver qué llegó

    // Normalizar el perfil (quitar espacios y minusculas)
    const perfilBackend = resultado.perfil.trim().toLowerCase();

    // 2. Resaltar el perfil obtenido
    highlightProfile(perfilBackend);

    // 3. Mostrar los instrumentos recomendados
    renderInstruments(resultado.recomendaciones);
});

function highlightProfile(perfilBuscado) {
    const perfiles = document.querySelectorAll('.profile-item');
    let encontrado = false;

    perfiles.forEach(item => {
        const tituloElement = item.querySelector('.profile-title');
        const descElement = item.querySelector('.profile-description'); // <--- Seleccionamos la descripción
        const numberElement = item.querySelector('.profile-number');    // <--- Seleccionamos el número

        if (!tituloElement) return;

        const tituloHtml = tituloElement.textContent.trim().toLowerCase();

        // Si coincide con el perfil del usuario
        if (tituloHtml === perfilBuscado) {
            encontrado = true;

            // 1. Estilos del contenedor (Ya estaban bien)
            item.style.border = "4px solid #c57d56";
            item.style.backgroundColor = "#fff3e0"; // Fondo claro
            item.style.transform = "scale(1.05)";
            item.style.transition = "all 0.3s ease";
            item.style.opacity = "1";
            item.style.borderRadius = "8px"; // Un toque estético extra
            item.style.padding = "20px";     // Espacio interno para que no se vea apretado

            // 2. CORRECCIÓN DE LEGIBILIDAD (Texto Oscuro)
            tituloElement.style.color = "#3e2723"; // Marrón muy oscuro para el título
            if (descElement) descElement.style.color = "#5d4037"; // Marrón medio para el texto
            if (numberElement) numberElement.style.color = "#c57d56"; // Terracota para el número grande

            setTimeout(() => {
                item.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 500);

        } else {
            // Estilos para los NO seleccionados (Mantener texto blanco)
            item.style.opacity = "0.4";
            item.style.transform = "scale(0.95)";
            item.style.border = "none";
            item.style.backgroundColor = "transparent";

            // Restaurar colores originales (Blanco)
            tituloElement.style.color = "white";
            if (descElement) descElement.style.color = "rgba(255, 255, 255, 0.9)";
            if (numberElement) numberElement.style.color = "rgba(255, 255, 255, 0.4)";
        }
    });

    if (!encontrado) {
        console.error("No se encontró perfil:", perfilBuscado);
    }
}

function renderInstruments(instrumentos) {
    const container = document.getElementById('recommendations-container');
    const grid = document.getElementById('instruments-grid');

    if (!container || !grid) {
        console.error("No se encontraron los contenedores de recomendaciones en el HTML.");
        return;
    }

    if (!instrumentos || instrumentos.length === 0) {
        container.style.display = 'none';
        return;
    }

    container.style.display = 'block'; // Mostrar la sección

    grid.innerHTML = instrumentos.map(inst => {
        // Generar nombre de clase basado en el riesgo (ej: 'risk-bajo', 'risk-alto')
        const riesgoClass = `risk-${inst.riesgo.toLowerCase()}`;

        return `
        <div class="instrument-card">
            <h3 class="instrument-name">
                ${inst.nombre}
            </h3>
            
            <div class="badge-container">
                <span class="risk-badge ${riesgoClass}">
                    RIESGO: ${inst.riesgo.replace('_', ' ').toUpperCase()}
                </span>
                
                <span class="type-badge">
                    ${inst.tipo.replace('_', ' ').toUpperCase()}
                </span>
            </div>
            
            <p class="instrument-desc">
                ${inst.descripcion}
            </p>
            
            <div class="instrument-yield">
                📈 Rendimiento ref: <span>${inst.rendimiento_referencial}</span>
            </div>
        </div>
    `}).join('');
}