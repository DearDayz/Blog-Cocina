async function add_favorite(e) {
    const csrfToken = getCookie("csrftoken")
    await fetch(`http://127.0.0.1:8000/users/v2/favorites/${e.currentTarget.id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken 
        }
    })
    .then(async (res) => {
        console.log(res)
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