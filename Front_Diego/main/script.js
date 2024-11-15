 // Obtener todos los botones del menú desplegable
 const themeButtons = document.querySelectorAll('.dropdown-item');

 themeButtons.forEach(button => {
   button.addEventListener('click', () => {
     // Cambiar el valor del atributo data-bs-theme en el header
     const selectedTheme = button.getAttribute('data-bs-theme-value');
     document.getElementById('theme-header').setAttribute('data-bs-theme', selectedTheme);

     // Actualizar el estado activo de los botones
     themeButtons.forEach(btn => btn.classList.remove('active'));
     button.classList.add('active');

     // Cambiar la clase aria-pressed
     themeButtons.forEach(btn => btn.setAttribute('aria-pressed', 'false'));
     button.setAttribute('aria-pressed', 'true');
   });
 });