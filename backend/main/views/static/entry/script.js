
const stars = document.querySelectorAll('.star');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            const rating = star.getAttribute('data-value'); // Obtener valor de la estrella
            stars.forEach(s => {
                s.classList.remove('selected'); // Limpiar selección
                if (s.getAttribute('data-value') <= rating) {
                    s.classList.add('selected'); // Marcar estrellas hasta la seleccionada
                }
            });
            console.log(`Valoración: ${rating}`); // Aquí puedes manejar la valoración como desees
        });
    });

// Variable global para mantener el valor dinámico
let valorActual = 1; // Valor inicial

function modificarValor(cambio) {
    // Calcular el nuevo valor sumando el cambio
    valorActual += cambio;

    // Asegurarse de que el valor no sea menor que 1
    if (valorActual < 1) {
        valorActual = 1;
    }

    // Obtener el campo input
    const campo = document.getElementById("campo");

    // Actualizar el valor del input usando setAttribute para modificar el atributo 'value'
    campo.setAttribute("value", valorActual);

    // Ver el valor actualizado en la consola
    console.log("Nuevo valor de input:", campo.value); // Esto debería mostrar el valor en consola
}