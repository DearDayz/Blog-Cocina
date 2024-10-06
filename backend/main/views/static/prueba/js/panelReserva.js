/* Panel de reserva*/
let botonVolerPanelReserva = document.querySelector(".boton-volver-seccion-reservacion")
botonVolerPanelReserva.addEventListener("click" , ()=>{
    let panelReservacion = document.querySelector(".reservation-panel")
    panelReservacion.style.display = "none"
    let panelPrincipal = document.querySelector(".section_img")
    panelPrincipal.style.display = "flex"
    borrarFormularioReserva()
})

//validaciones panel contacto
//hacemos la validacion para el input del nombre
inputContacto = document.querySelector("#contact")

inputContacto.addEventListener('input', function() {
    let filteredValue = '';
    // Recorrer cada caracter del valor actual del input
    for (let i = 0; i < this.value.length; i++) {
        let char = this.value[i];
        // Verificar si el caracter es una letra o un espacio
        if ((char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || char === ' ') {
            filteredValue += char; // Agregar el caracter al valor filtrado
        }
    }
    // Establecer el valor filtrado de vuelta en el input 
    this.value = filteredValue;
});

//hacemos la validacion para el input del pasaporte
inputPasaporte = document.querySelector("#passport");
inputPasaporte.addEventListener('input', function() {
    let value = this.value.trim(); // Obtener el valor del input y eliminar espacios en blanco al principio y al final
    let formattedValue = '';

    // Convertir los primeros tres caracteres a mayúsculas y filtrar solo letras
    for (let i = 0; i < Math.min(value.length, 3); i++) {
        let char = value[i];
        if (char >= 'a' && char <= 'z') {
            char = char.toUpperCase(); // Convertir a mayúsculas si es minúscula
        }
        if (char >= 'A' && char <= 'Z') {
            formattedValue += char;
        }
    }

    // Agregar los caracteres numéricos restantes hasta un máximo de 9 caracteres en total
    for (let i = 3; i < Math.min(value.length, 9); i++) {
        let char = value[i];
        if (char >= '0' && char <= '9') {
            formattedValue += char;
        }
    }

    // Limitar a un máximo de 9 caracteres
    formattedValue = formattedValue.substring(0, 9);

    // Actualizar el valor del input
    this.value = formattedValue;
});

//hacemos la validacion para el input del telefono
inputTelefono = document.querySelector("#phone")
inputTelefono.addEventListener('input', function(event) {
    let value = this.value.trim(); // Obtener el valor del input y eliminar espacios en blanco al principio y al final
    let formattedValue = '';

    // Filtrar y formatear solo caracteres numéricos
    for (let i = 0; i < value.length; i++) {
        let char = value[i];
        // Verificar si el caracter es un número del 0 al 9
        if (char >= '0' && char <= '9') {
            formattedValue += char;
        }
    }

    // Limitar el número de caracteres a 15
    formattedValue = formattedValue.substring(0, 15);

    // Añadir el prefijo '+' al inicio si no está presente
    if (!formattedValue.startsWith('+')) {
        formattedValue = '+' + formattedValue;
    }

    // Actualizar el valor del input
    this.value = formattedValue;
});


//sacamos el input del correo
inputCorreo = document.querySelector("#email")
function validarCorreoElectronico(correo) {
    // Expresión regular para validar un correo electrónico
    const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regexCorreo.test(correo);
}

//agregamos la funcion al boton borrar
inputBorrarReserva = document.querySelector("#botonBorrarReserva")
inputBorrarReserva.addEventListener("click" , borrarFormularioReserva
)

//Agregamos funcionalidad al input de tipo de asiento
inputTipoAsiento = document.querySelector("#tipoAsiento")
inputTipoAsiento.addEventListener("change", ()=>{
    //quitamos el estado de deshabilitado primero
    asientosHTML.forEach(asiento =>{
        asiento.classList.remove("deshabilitado")
    })
    //deshabilitamos los asientos
    inputAsientos.value = ""
    asientosHTML.forEach((asiento) =>{
            asiento.classList.remove("seleccionado")
    })
    let valorTipoAsiento = inputTipoAsiento.value;
    if (valorTipoAsiento == "Economico plus"){
        asientosHTML.forEach(asiento => {
            if (!asiento.classList.contains("plus")){
                asiento.classList.add("deshabilitado");
        }})
    }
    else if (valorTipoAsiento == "Economico bajo"){
        asientosHTML.forEach(asiento => {
            if(!asiento.classList.contains("bajo")){
                asiento.classList.add("deshabilitado")
            }
        })
    }
    else if(valorTipoAsiento == "Economico normal"){
        asientosHTML.forEach(asiento =>{
            if(asiento.classList.contains("bajo") || asiento.classList.contains("plus")){
                asiento.classList.add("deshabilitado")
            }
        })       
    }
})

//sacamos el resto de input's
inputEquipajeRegistrado = document.querySelector("#registered-luggage")
inputEquipajeMano = document.querySelector("#hand-luggage")

inputAdultos = document.querySelector("#adults")
inputNiños = document.querySelector("#children")
inputInfantes = document.querySelector("#infants")

//agregamos las validaciones al boton guardar del panel de reserva 
inputGuardarReserva = document.querySelector("#botonGuardarReserva")

//declaramos una variable que guardo el pago final de la reserva
pagoFinal = null
//agregamos el evento al boton guardar
inputGuardarReserva.addEventListener("click" ,()=>{
    if (inputContacto.value == ""){
        alert("El contacto es invalido")
        return null
    }
    else if(inputPasaporte.value.length < 9){
        alert("Pasaporte incompleto")
        return null
    }
    else if(inputTelefono.value.length == 0 || inputTelefono.value.length == 1){
        alert("telefono incompleto")
        return null
    }
    else if(!validarCorreoElectronico(inputCorreo.value)){
        alert("Correo invalido")
        return null
    }
    else if(inputAsientos.value.split(" ").length -1 != sumarPasajeros()){
        alert("Rellene los asientos")
        return null
    }
    else{
        if(inputAdultos.value == "0"){
            alert("Los niños e infantes deben de contar con una autorizacion de su representante al momento de presentarse al vuelo")
        }
        let tablaTipoClase = document.querySelector(".tipoClaseSeleccionada")
        console.log(tablaTipoClase)

        let panelReservacion = document.querySelector(".reservation-panel")
        panelReservacion.style.display = "none"
        let panelCostos = document.querySelector(".costos-panel")
        panelCostos.style.display = "block"


        //Primero obtenemos las entradas de las tablas
        let tablaMaletaRegistradaCosto = document.querySelector("#tablaMaletaRegistradaCosto")
        let tablaMaletaRegistrada = document.querySelector("#tablaMaletaRegistrada")
        let tablaMaletaRegistradaPago = document.querySelector("#tablaMaletaRegistradaPago")
        let tablaMaletaManoCosto = document.querySelector("#tablaMaletaManoCosto")
        let tablaMaletaMano = document.querySelector("#tablaMaletaMano")
        let tablaMaletaManoPago = document.querySelector("#tablaMaletaManoPago")
        let tablaAdultoCosto = document.querySelector("#tablaAdultoCosto")
        let tablaAdulto = document.querySelector("#tablaAdulto")
        let tablaAdultoPago = document.querySelector("#tablaAdultoPago")
        let tablaNiñoCosto = document.querySelector("#tablaNiñoCosto")
        let tablaNiño = document.querySelector("#tablaNiño")
        let tablaNiñoPago = document.querySelector("#tablaNiñoPago")
        let tablaInfanteCosto = document.querySelector("#tablaInfanteCosto")
        let tablaInfante = document.querySelector("#tablaInfante")
        let tablaInfantePago = document.querySelector("#tablaInfantePago")
        let tablaPago = document.querySelector("#tablaPago")


        

        //establecemos los valores de las tablas
        if(inputTipoAsiento.value == "Economico bajo"){
            tablaTipoClase.textContent = "Economico Ligero"
            tablaMaletaRegistradaCosto.textContent = "436.21"
            tablaMaletaManoCosto.textContent = "218.11"
            tablaAdultoCosto.textContent = "843.34"
            tablaNiñoCosto.textContent = "814.26"
            tablaInfanteCosto.textContent = "799.72"
            
        }
        if(inputTipoAsiento.value == "Economico normal"){
            tablaTipoClase.textContent = "Economico Medio"
            tablaMaletaRegistradaCosto.textContent = "436.21"
            tablaMaletaManoCosto.textContent = "218.11"
            tablaAdultoCosto.textContent = "996.02"
            tablaNiñoCosto.textContent = "981.48"
            tablaInfanteCosto.textContent = "966.94"
        }
        if(inputTipoAsiento.value == "Economico plus"){
            tablaTipoClase.textContent = "Economico Premium"
            tablaMaletaRegistradaCosto.textContent = "436.21"
            tablaMaletaManoCosto.textContent = "218.11"
            tablaAdultoCosto.textContent = "1235.93"
            tablaNiñoCosto.textContent = "1221.93"
            tablaInfanteCosto.textContent = "1206.85"
        
        }

        tablaMaletaRegistrada.textContent = inputEquipajeRegistrado.value
        tablaMaletaMano.textContent = inputEquipajeMano.value
        tablaAdulto.textContent = inputAdultos.value
        tablaNiño.textContent = inputNiños.value
        tablaInfante.textContent = inputInfantes.value


        tablaMaletaRegistradaPago.textContent = String((parseFloat(tablaMaletaRegistradaCosto.textContent)* parseFloat(tablaMaletaRegistrada.textContent)).toFixed(2))
        tablaMaletaManoPago.textContent = String((parseFloat(tablaMaletaManoCosto.textContent)* parseFloat(tablaMaletaMano.textContent)).toFixed(2))
        tablaAdultoPago.textContent = String((parseFloat(tablaAdultoCosto.textContent)* parseFloat(tablaAdulto.textContent)).toFixed(2))
        tablaNiñoPago.textContent = String((parseFloat(tablaNiñoCosto.textContent)* parseFloat(tablaNiño.textContent)).toFixed(2))
        tablaInfantePago.textContent =  String((parseFloat(tablaInfanteCosto.textContent)* parseFloat(tablaInfante.textContent)).toFixed(2))
        tablaPago.textContent = String((parseFloat(tablaMaletaRegistradaPago.textContent)+ parseFloat(tablaMaletaManoPago.textContent) + parseFloat(tablaAdultoPago.textContent) + parseFloat(tablaNiñoPago.textContent) + parseFloat(tablaInfantePago.textContent)).toFixed(2))
        pagoFinal = new String(tablaPago.textContent)
    }
});


/*FUNCIONALIDAD ASIENTOS */

//Obtenemos el span de los asientos HTML
asientosHTML = document.querySelectorAll(".seat")
inputAsientos = document.getElementById("seats")

//Obtenemos los inputs de la cantidad de pasajeros
const adultsInput = document.getElementById('adults');
const childrenInput = document.getElementById('children');
const infantsInput = document.getElementById('infants');
//Los almacenamos en una lista
let todosLosInputs = [adultsInput , childrenInput , infantsInput]

//agregamos una funcion en los inputs para que cada vez que se modifique, se deseleccionen los asientos
todosLosInputs.forEach((input)=>{
    input.addEventListener("input", ()=>{
        inputAsientos.value = ""
        asientosHTML.forEach((asiento) =>{
            asiento.classList.remove("seleccionado")
        })
    })
})

//Se le agrega las funcionalidades a cada asiento, para que se puedan elegir, deseleccionar y asi
asientosHTML.forEach(asiento => {
    asiento.addEventListener("click" , function(e) {
        if (inputTipoAsiento.value != "Economico normal" && inputTipoAsiento.value !="Economico bajo" && inputTipoAsiento.value !="Economico plus"){
            alert("Elige una clase para tus asientos")
            return null
        }
        if(sumarPasajeros() == 0){
            alert("Coloca la cantidad de asientos")
            return null
        }
        //Obtenemos el asiento que desencadeno el evento
        var asientoDelEvento = e.target
        //verificamos si el asiento ya esta seleccionado para deseleccionarlo
        if (asientoDelEvento.classList.contains("seleccionado") ) {
            asientoDelEvento.classList.remove("seleccionado");
            //Quitamos el asiento del input
            inputAsientos.value = inputAsientos.value.replace(" "+asientoDelEvento.getAttribute("data-value"), "")
            return null
        }

        //verifica si el asiento esta ocupado o deshabilitdao, para que no haga nada
        if (asientoDelEvento.classList.contains("ocupado") || asientoDelEvento.classList.contains("deshabilitado")) {
            return null
        }

        //si el asiento esta libre, procedemos a hacer validaciones
        let contAsientos= sumarPasajeros();
        let contAsientosSelect = 0;

        //contamos la cantidad de asientos seleccionados
        asientosHTML.forEach(asiento =>{
            if (asiento.classList.contains("seleccionado")) {
                contAsientosSelect += 1;
            }
        })
        //verificamos que la cantidad de los asientos seleccionados, no pase que la cantidad proporcionada por el usuario
        if (contAsientos > contAsientosSelect) {
            if(contAsientos == 0){
                inputAsientos.value += asientoDelEvento.getAttribute("data-value")
            }
            else{
                inputAsientos.value += " " + asientoDelEvento.getAttribute("data-value")
            }
            asientoDelEvento.classList.add("seleccionado")
        }
    })
})