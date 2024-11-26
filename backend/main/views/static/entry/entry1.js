
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

            //Obtenemos el id de la receta de la url
            const path = window.location.pathname; // Obtiene la ruta de la URL actual
            const lastNumber = path.match(/(\d+)$/); // Busca el último número en la ruta
            const number = lastNumber ? parseInt(lastNumber[0]) : null; // Convierte a número o null si no encuentra
            console.log(number);
            // Guardar la valoración en tu base de datos
            $.post(createValoracionUrl, {puntuacion: rating, csrfmiddlewaretoken: csrfToken, id_receta: number})
            .done(response => {
                // Manejo de la respuesta exitosa
                console.log("Respuesta del servidor:", response);
            })
            .fail(error => {
                // Manejo de errores
                console.error("Error en la solicitud:", error);
            })
        });
    });

// Variable global para mantener el valor dinámico
let valorActual = 1; // Valor inicial

function funcionDeMierda(cambio) {
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
    /* QUE WEBOOOOOOOOOOOOOOOOOO */
}

function modificarCantidad(cambio, id) {

    // Obtener el campo input
    const campo = document.getElementById("cantidad-" + id);
    
    let valorActual = parseFloat(campo.value) + parseFloat(cambio)
    // Asegurarse de que el valor no sea menor que 1
    if (valorActual < 1) {
        valorActual = 1;
    }
    // Actualizar el valor del input usando setAttribute para modificar el atributo 'value'
    campo.setAttribute("value", valorActual.toFixed(1));

    // Ver el valor actualizado en la consola
    console.log("Nuevo valor de input", campo.value); // Esto debería mostrar el valor en consola
}