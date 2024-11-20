// Código para el subtítulo dinámico
const phrases = ["Aprender", "Crear", "Colaborar"];
let i = 0;

setInterval(() => {
    document.getElementById("dynamic-subtitle").textContent = `Un Enfoque Basado en Proyectos para ${phrases[i]}`;
    i = (i + 1) % phrases.length;
}, 2000); // Cambia cada 2 segundos
