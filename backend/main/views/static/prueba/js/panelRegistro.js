/* Panel de registro */
let botonVolerPanelRegistro = document.querySelector(".boton-volver-tabla-registro")
botonVolerPanelRegistro.addEventListener("click", ()=>{
    let panelRegistro = document.querySelector(".registro-panel")
    panelRegistro.style.display = "none"
    let panelPrincipal = document.querySelector(".section_img")
    panelPrincipal.style.display = "flex"
})