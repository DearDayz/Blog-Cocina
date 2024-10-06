/* PANEL PRINCIPAL */

//funcion que se ejcuta con el boton registro
function despuesBotonRegistro(){
    let fragmento = document.createDocumentFragment()
    let tablaRegistro = document.querySelector("#tablaRegistro")
    if(listaReservas.length != 0){
        listaReservas.forEach(reserva =>{
            //creamos las entradas de esta fila
            let fila = document.createElement("TR")
            fila.classList.add(reserva.identificador)
            let tdPasajero = document.createElement("TD")
            let tdEquipajeRegistrado = document.createElement("TD")
            let tdEquipajeMano = document.createElement("TD")
            let tdCantidadAsientos = document.createElement("TD")
            let tdAsientos = document.createElement("TD")

            //parte de los botones
            // Crear elementos HTML
            var tdEliminar = document.createElement('td');
            var botonEliminar = document.createElement('button');

            // Agregar clases a los botones
            botonEliminar.className = 'boton-eliminar';

            // Agregar texto a los botones
            botonEliminar.textContent = 'X';
            tdEliminar.appendChild(botonEliminar)

            //rellenamos los datos
            tdPasajero.textContent = reserva.nombre
            tdEquipajeRegistrado.textContent = reserva.equipajeRegistrado
            tdEquipajeMano.textContent = reserva.equipajeMano
            tdCantidadAsientos.textContent = reserva.cantidadAsientos
            tdAsientos.textContent = reserva.asiento

            //agregamos los datos a la fila
            fila.appendChild(tdPasajero)
            fila.appendChild(tdEquipajeRegistrado)
            fila.appendChild(tdEquipajeMano)
            fila.appendChild(tdCantidadAsientos)
            fila.appendChild(tdAsientos)
            fila.appendChild(tdEliminar)
            fragmento.appendChild(fila)
        })
    } //aqui termina el if

    //Agregamos el evento a los botones
    tablaRegistro.innerHTML = ""
    tablaRegistro.appendChild(fragmento)
    let botonesEliminar = document.querySelectorAll(".boton-eliminar")
    botonesEliminar.forEach(eliminar => {
        eliminar.addEventListener("click", ()=>{
            let confimarcion = window.confirm("Esta seguro que desea eliminar el registro?")
            if(!confimarcion){
                return null
            }
            let filaPadre = eliminar.parentElement.parentElement
            let ticket = filaPadre.className
            let reservaBorrar = null
            listaReservas.forEach(reserva=>{
                if (reserva.identificador == ticket){
                    reservaBorrar = reserva
                }
            });
            let asientosReserva = reservaBorrar.asiento
            asientosReserva = asientosReserva.trim()
            asientosReserva = asientosReserva.split(" ")
            asientosReserva.forEach(valorAsiento =>{
                asientosHTML.forEach(asiento =>{
                    if(asiento.getAttribute("data-value") == valorAsiento){
                        asiento.classList.remove("ocupado")
                    }
                })
            })
            listaReservas = listaReservas.filter(item => item!=reservaBorrar)
            tablaRegistro.removeChild(filaPadre)
        })
    })

}

//boton reservar panel principal
let botonReservarPanelPrincipal = document.querySelector(".boton_reservar")
botonReservarPanelPrincipal.addEventListener("click", ()=>{
    let panelPrincipal = document.querySelector(".section_img")
    panelPrincipal.style.display = "none"
    let panelReserva = document.querySelector(".reservation-panel")
    panelReserva.style.display = "block"
})

//boton registro panel principal
let botonRegistroPanelPrincipal = document.querySelector(".boton_registro")
botonRegistroPanelPrincipal.addEventListener("click", ()=>{
    let panelPrincipal = document.querySelector(".section_img")
    panelPrincipal.style.display = "none"
    let panelRegistro = document.querySelector(".registro-panel")
    panelRegistro.style.display = "block"
    despuesBotonRegistro()

})