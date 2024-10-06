// receta-prueba.js
if (window.recetaData) {
    console.log(window.recetaData); // Debería mostrar la receta sin errores.
    
    const recetaCard = document.getElementById('card');
    recetaCard.textContent = `${recetaData.nombre}`
    // Crear un nuevo elemento de imagen
    const imgElement = document.createElement('img');

    // Establecer la URL de la imagen
    imgElement.src = recetaData.imagen;

    // (Opcional) Establecer atributos adicionales
    imgElement.alt = 'Descripción de la imagen'; // Texto alternativo
    imgElement.style.width = '300px'; // Cambia el tamaño según necesites
    imgElement.style.height = 'auto'; // Mantiene la proporción
    recetaCard.appendChild(imgElement)

} else {
    console.error("No se encontró recetaData.");
}






