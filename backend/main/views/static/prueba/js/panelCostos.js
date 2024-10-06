/* Panel de costos */
let botonVolverPanelCostos = document.querySelector(".boton-volver-reserva")
botonVolverPanelCostos.addEventListener("click" , ()=>{
    let panelCostos = document.querySelector(".costos-panel")
    panelCostos.style.display = "none"
    let panelReserva = document.querySelector(".reservation-panel")
    panelReserva.style.display = "block"
})

let botonAceptarPanelCostos = document.querySelector(".boton-aceptar")
botonAceptarPanelCostos.addEventListener("click" , ()=>{
    let panelCostos = document.querySelector(".costos-panel")
    panelCostos.style.display = "none"
    let panelPago = document.querySelector(".payment-method")
    panelPago.style.display = "flex"

})