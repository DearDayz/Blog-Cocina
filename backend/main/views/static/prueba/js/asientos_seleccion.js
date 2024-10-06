/* RECORDATORIOS
contains(class) --> verifica si el elemento tiene esa clase, si la tiene devuelv true sino false
e.target
*/

/*

    Input del pasaporte con solo numeros

 inputPasaporte.addEventListener('input', function() {
    let value = this.value.trim(); // Obtener el valor del input y eliminar espacios en blanco al principio y al final
    let formattedValue = '';

    // Agregar los caracteres numéricos restantes hasta un máximo de 9 caracteres en total
    for (let i = 0; i < Math.min(value.length, 9); i++) {
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

    Input del telefono en formato Internacional

    inputTelefono.addEventListener('input', function() {
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
	if (formattedValue.length > 1){
		this.value = "+"
	}

    // Actualizar el valor del input
    this.value = formattedValue.substring(0,15);
});

    Cambiar la validacion del boton guardar --> inputTelefono.value.length < 12

*/


//Funcion que suma la cantidad de pasajeros

/*Otra validacion del input formato local
//hacemos la validacion para el input del telefono
inputTelefono = document.querySelector("#phone")
inputTelefono.addEventListener('input', function() {
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

    // Aplicar el formato "0000-0000000"
    if (formattedValue.length > 4) {
        formattedValue = formattedValue.substring(0, 4) + '-' + formattedValue.substring(4, 11);
    }

    // Actualizar el valor del input
    this.value = formattedValue;
});
*/