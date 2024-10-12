const Regresar_anterior = document.getElementById('boton_regresarrr');

Regresar_anterior.addEventListener('click',function(){
    window.location.href = 'Cliente.html';
})

function previewImage(event) {
    const fileInput = event.target;
    const imgPreview = document.getElementById('imgPreview');

    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            imgPreview.src = e.target.result;
            imgPreview.style.display = 'block';
        };
        reader.readAsDataURL(fileInput.files[0]);
    }
}