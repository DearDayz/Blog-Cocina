//inputs del registro de reserva
console.log("Hola mundo")
var inputContacto = document.querySelector("#contact")
var inputPasaporte = document.querySelector("#passport");
var inputTelefono = document.querySelector("#phone")
var inputCorreo = document.querySelector("#email")
var inputBorrarReserva = document.querySelector("#botonBorrarReserva")
var inputTipoAsiento = document.querySelector("#tipoAsiento")

var inputEquipajeRegistrado = document.querySelector("#registered-luggage")
var inputEquipajeMano = document.querySelector("#hand-luggage")
var inputAdultos = document.querySelector("#adults")
var inputNiños = document.querySelector("#children")
var inputInfantes = document.querySelector("#infants")

// boton guardar panel de reserva
var inputGuardarReserva = document.querySelector("#botonGuardarReserva")

var pagoFinal = null

//funcion sumar cantidad de pasajeros
function sumarPasajeros() {
    const adultsInput = document.getElementById('adults');
    const childrenInput = document.getElementById('children');
    const infantsInput = document.getElementById('infants');
    const adultos = parseInt(adultsInput.value) || 0;
    const niños = parseInt(childrenInput.value) || 0;
    const infantes = parseInt(infantsInput.value) || 0;
    
    return adultos + niños + infantes;
}

var asientosHTML = document.querySelectorAll(".seat")
var inputAsientos = document.getElementById("seats")

var listaReservas = []
var contadorReservas = 1
class ReservaPersona{
    constructor(nombre,telefono,pasaporte,correo,tipoAsiento,equipajeRegistrado,equipajeMano,boletoAdulto,boletoNiño,boletoInfante,asiento ,cantidadAsientos ,pago){
        this.nombre = nombre;
        this.telefono = telefono;
        this.pasaporte = pasaporte;
        this.correo = correo;
        this.tipoAsiento = tipoAsiento;
        this.equipajeRegistrado = equipajeRegistrado;
        this.equipajeMano = equipajeMano;
        this.boletoAdulto = boletoAdulto;
        this.boletoNiño = boletoNiño;
        this.boletoInfante = boletoInfante;
        this.asiento = asiento;
        this.cantidadAsientos = cantidadAsientos;
        this.pago = pago;
        this.identificador = `ticket${contadorReservas}`
        contadorReservas += 1;
    }
}


function borrarFormularioReserva(){
    
    //procedemos a borrar cada valor de los inputs
    inputContacto.value = ""
    inputPasaporte.value = ""
    inputTelefono.value = ""
    inputCorreo.value = ""
    inputEquipajeRegistrado.value = "0"
    inputEquipajeMano.value = "0"
    inputAdultos.value = "0"
    inputNiños.value = "0"
    inputInfantes.value = "0"
    inputAsientos.value = ""
    asientosHTML.forEach((asiento) =>{
        asiento.classList.remove("seleccionado")
        asiento.classList.remove("deshabilitado")
    })
    inputTipoAsiento.selectedIndex = 0
}
