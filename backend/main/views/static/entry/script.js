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