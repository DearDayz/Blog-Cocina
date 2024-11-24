const para_ver_mas_detalles = document.getElementById('vermasdetalles');
const agregar_recetas = document.getElementById('Agregar_recetas');

para_ver_mas_detalles.addEventListener('click',function(){
    window.location.pathname = 'admin-view-recipes/';
})

agregar_recetas.addEventListener('click', function(){
    window.location.pathname = 'add-recipe/';
})
