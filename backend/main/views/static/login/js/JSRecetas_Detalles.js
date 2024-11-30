let currentPage = 1;
const rowsPerPage = 7;

function displayTable() {
    const table = document.getElementById("dataTable");
    const rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr");

    // Calcular el número total de páginas
    const totalRows = rows.length;
    const totalPages = Math.ceil(totalRows / rowsPerPage);

    // Ocultar todas las filas
    for (let i = 0; i < totalRows; i++) {
        rows[i].style.display = "none";
    }

    // Mostrar solo las filas de la página actual
    for (let i = (currentPage - 1) * rowsPerPage; i < currentPage * rowsPerPage && i < totalRows; i++) {
        rows[i].style.display = "";
    }

    // Actualizar la información de la página
    document.getElementById("pageInfo").innerText = `Página ${currentPage} de ${totalPages}`;
}

function changePage(direction) {
    const totalRows = document.getElementById("dataTable").getElementsByTagName("tbody")[0].getElementsByTagName("tr").length;
    const totalPages = Math.ceil(totalRows / rowsPerPage);

    // Cambiar la página actual
    if (direction === -1 && currentPage > 1) {
        currentPage--;
    } else if (direction === 1 && currentPage < totalPages) {
        currentPage++;
    }

    displayTable();
}

// Inicializar la tabla al cargar
displayTable();

var abrir_modificacion = document.getElementById('abrir_modificacion');

async function delete_receta(e) {
    const csrfToken = getCookie("csrftoken")
    await fetch(`http://127.0.0.1:8000/blog-api/recetas/${e.currentTarget.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken 
        }
    })
    .then(async (res) => {
        location.reload();
        console.log(res)
    })
    .catch((err) => {
        console.error(err)
    })
}
async function delete_employee(e) {
    const csrfToken = getCookie("csrftoken")
    await fetch(`http://127.0.0.1:8000/users/v2/delete/${e.currentTarget.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken 
        },
    })
    .then(async (res) => {
        location.reload();
        console.log(res)
    })
    .catch((err) => {
        console.error(err)
    })
}

function employee_data(e) {
    window.location.pathname = `user-data/${e.currentTarget.id}`
}

function detalle_receta(e) {
    window.location.pathname = `vista-entry/${e.currentTarget.id}`
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