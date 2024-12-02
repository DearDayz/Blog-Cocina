async function add_favorite(e) {
    const csrfToken = getCookie("csrftoken")
    const button = e.currentTarget; // El botón clickeado
    const icon = document.getElementById(`heart-icon-${button.id}`);  // Icono del corazón
    await fetch(`/users/v2/favorites/${e.currentTarget.id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken 
        }
    })
    .then(async (res) => {
        if (res.status === 201) {
            console.log("Receta agregada a favoritos");

            // Cambiar el icono a un corazón relleno (rojo)
            icon.classList.remove("fa-regular", "fa-heart");
            icon.classList.add("fa-solid", "fa-heart");  // Cambiar a corazón relleno

            // Cambiar el color del corazón a rojo
            icon.style.color = "red";  // Cambiar color al hacer clic
        } else if (res.status === 204) {
            console.log("Rceta eliminada de favoritos");

            // Cambiar el icono a un corazón vacío (gris)
            icon.classList.remove("fa-solid", "fa-heart");
            icon.classList.add("fa-regular", "fa-heart");  // Cambiar a corazón vacío

            // Cambiar el color del corazón a gris
            icon.style.color = "gray";
        }
        else {
            console.error('Error: No se esperaba este estado:', res.status);
        }
    })
    .catch((err) => {
        console.error(err)
    })
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}