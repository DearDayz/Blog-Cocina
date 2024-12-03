$(document).ready(function(argument) {
    $(".logoCorazon").dblclick(function () {
        const dataId = $(this).data('id'); 
        const csrfToken = getCookie("csrftoken")
        const icon = document.getElementById(`heart-icon-${dataId}`); 
      $.post(
        `/users/v2/favorites/${dataId}/`,
        {csrfmiddlewaretoken: csrfToken}
      )
      .done (response => {
        if (response) {
            console.log("Receta agregada a favoritos");
            // Hacer animacion de corazón
            if (!icon.classList.contains("fa-solid")) {
                $(this).next().animate({'width': '52.5%', 'height':'75%'}, 200);
                setTimeout(function () {
                  $(".popCorazon").animate({'width': '0', 'height': '0'}, 200);
                }, 1000);
              }

            // Cambiar el icono a un corazón relleno (rojo)
            icon.classList.remove("fa-regular", "fa-heart");
            icon.classList.add("fa-solid", "fa-heart");  // Cambiar a corazón relleno

            // Cambiar el color del corazón a rojo
            icon.style.color = "red";  // Cambiar color al hacer clic

            

        } else if (!response) {
            console.log("Rceta eliminada de favoritos");

            // Cambiar el icono a un corazón vacío (gris)
            icon.classList.remove("fa-solid", "fa-heart");
            icon.classList.add("fa-regular", "fa-heart");  // Cambiar a corazón vacío

            // Cambiar el color del corazón a gris
            icon.style.color = "gray";
        }
        else {
            console.error('Error: No se esperaba este estado:', response.status);
        }
      })
      .fail(err => {
        console.error(err)
      })
    });
  });



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

            // Hacer animacion de corazón
            const imagenes = document.querySelectorAll(".logoCorazon");
            imagenes.forEach((imagen) => {
                if (imagen.getAttribute('data-id') == button.id) {
                    $(imagen).next().animate({'width': '52.5%', 'height':'75%'}, 200);
                    setTimeout(function () {
                    $(".popCorazon").animate({'width': '0', 'height': '0'}, 200);
                    }, 1000);
                }
            })
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