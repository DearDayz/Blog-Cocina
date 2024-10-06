// cremaos el objeto ReservaPersona


function despuesDePagar(){
    //guardamos la informacion de la reserva en el array

    let nuevaReserva = new ReservaPersona(new String(inputContacto.value) , new String(inputTelefono.value) , new String(inputPasaporte.value) , new String(inputCorreo.value) , new String(inputTipoAsiento.value) , new String(inputEquipajeRegistrado.value) , new String(inputEquipajeMano.value ), new String(inputAdultos.value ), new String(inputNiños.value ), new String(inputInfantes.value) , new String(inputAsientos.value ), new Number(sumarPasajeros()) ,new String(pagoFinal))
    listaReservas.push(nuevaReserva)
    console.log(listaReservas)
    //Pasamos los asientos seleccionados a ocupados
    asientosHTML.forEach(asiento => {
        if (asiento.classList.contains("seleccionado")){
            asiento.classList.add("ocupado")
            asiento.classList.remove("seleccionado")
        }
        
    })

    borrarFormularioReserva()
}

/*Panel pago*/
let inputNumeroTarjeta = document.querySelector("#cardNumber")

inputNumeroTarjeta.addEventListener('input', function() {

    let valor = inputNumeroTarjeta.value;
    let nuevoValor = '';

    // Iterar sobre cada carácter del valor actual del input
    for (let i = 0; i < valor.length; i++) {
        // Verificar si el carácter actual es un dígito
        if (!isNaN(valor[i]) && valor[i] !== ' ') {
            // Si es un dígito, añadirlo al nuevo valor
            nuevoValor += valor[i];
        }
    }

    // Limitar la longitud a 16 caracteres
    if (nuevoValor.length > 19) {
        nuevoValor = nuevoValor.slice(0, 19); // Cortar el valor a los primeros 16 caracteres
    }

    // Actualizar el valor del input con el nuevo valor limpio y limitado
    inputNumeroTarjeta.value = nuevoValor;
});

let inputFechaVencimientoTarjeta = document.querySelector("#expiryDate")
let inputCodigoSeguridadTarjeta = document.querySelector("#securityCode")
inputCodigoSeguridadTarjeta.addEventListener('input', function() {
    let valor = inputCodigoSeguridadTarjeta.value;
    let nuevoValor = '';

    // Iterar sobre cada carácter del valor actual del input
    for (let i = 0; i < valor.length; i++) {
        // Verificar si el carácter actual es un dígito
        if (!isNaN(valor[i]) && valor[i] !== ' ' && nuevoValor.length < 4) {
            // Si es un dígito, añadirlo al nuevo valor
            nuevoValor += valor[i];
        }
    }

    // Actualizar el valor del input con el nuevo valor limpio y permitido
    inputCodigoSeguridadTarjeta.value = nuevoValor;
});

let inputCardHolder = document.querySelector("#cardHolder");
inputCardHolder.addEventListener('input', function() {
    let valor = inputCardHolder.value;
    let nuevoValor = '';

    // Iterar sobre cada carácter del valor actual del input
    for (let i = 0; i < valor.length; i++) {
        let char = valor.charAt(i);
        // Verificar si el carácter actual es una letra (mayúscula o minúscula) o un espacio
        if ((char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z') || char === ' ') {
            // Si es una letra o espacio, añadirlo al nuevo valor
            nuevoValor += char;
        }
        inputCardHolder.value = nuevoValor;
    }});


//boton pagar
let botonPagar = document.querySelector(".boton-pagar")
botonPagar.addEventListener("click" , ()=>{
    if( inputFechaVencimientoTarjeta.value == "" || inputCodigoSeguridadTarjeta.value == "" || inputCardHolder.value == ""){
        alert("Complete todos los datos")
        return null
    }
    if(inputNumeroTarjeta.value.length== 0){
        alert("Coloque los Digitos de la tarjeta")
        return null
    }
    alert("Compra Exitosa")
    //rederigir a la pagina principal
    let panelPrincipal = document.querySelector(".section_img")
    panelPrincipal.style.display = "flex"
    let panelPago = document.querySelector(".payment-method")
    panelPago.style.display = "none"
    inputNumeroTarjeta.value = ""
    inputFechaVencimientoTarjeta.value = ""
    inputCodigoSeguridadTarjeta.value = ""
    inputCardHolder.value = ""
    let todasLasTarjetas3 = document.querySelectorAll('.card-logo');
        todasLasTarjetas3.forEach(function(tarjeta) {
            tarjeta.style.border = 'none';
        });
    despuesDePagar()
})

// Funcionalidad a las imagenes
let todasLasTarjetas = document.querySelectorAll('.card-logo');
todasLasTarjetas.forEach(tarjetaImagen =>{
    tarjetaImagen.addEventListener("click" , ()=>{
        let todasLasTarjetas2 = document.querySelectorAll('.card-logo');
        todasLasTarjetas2.forEach(function(tarjeta) {
            tarjeta.style.border = 'none';
        });

        // Añade un borde resaltado a la tarjeta seleccionada
        
        tarjetaImagen.style.border = '2px solid blue'; // Cambia el estilo del borde según tus necesidades
    })
})

// boton volver costos
let botonVolverCostos = document.querySelector(".boton-volver-costos")
botonVolverCostos.addEventListener("click" , ()=>{
    let panelCostos = document.querySelector(".costos-panel")
    panelCostos.style.display = "block"
    let panelPago = document.querySelector(".payment-method")
    panelPago.style.display = "none"
    inputNumeroTarjeta.value = ""
    inputFechaVencimientoTarjeta.value = ""
    inputCodigoSeguridadTarjeta.value = ""
    inputCardHolder.value = ""
    let todasLasTarjetas3 = document.querySelectorAll('.card-logo');
        todasLasTarjetas3.forEach(function(tarjeta) {
            tarjeta.style.border = 'none';
        });

})