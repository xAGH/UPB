
// Validación 1
function checkNombre(valor) {
    var numero = false;
    var largor = valor.length;

    for (i = 0; i < largor; i++) {
        try {
            if (Number.isInteger(parseInt(valor[i]))) {
                numero = true;
            }
        } catch (e) {}
    }
    if ((valor != null) && (largor > 3 && largor <= 30) && (numero == false)) {
        return true;
    }
    return false;
}

// Validación 2
function checkGenero(valor) {
    if (valor.type == 'checkbox') {
        if (valor.checked) {
            return true;
        }
        return false;
    }
    return false;
}

// Validación 3
function checkTelefono(valor) {
    const validacion = new RegExp(/^[0-9]+$/);
    const longitud = 7;

    if(valor.length === longitud && validacion.test(valor)) {
        return true;
    }

    return false;
}

// Validación 4
function checkDir(valor) {
    var largor = valor.length,
        especial_chars = false;
    var filtro = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890#- ";

    for (let i = 0; i < largor; i++) {
        if (filtro.indexOf(valor.charAt(i)) != -1) {} else {
            especial_chars = true;
        }
    }

    if (valor != null && (largor < 51 && largor > 0) && especial_chars == false) {
        return true;
    }
    return false;
}

// Validación 5
function checkCorreo(valor) {
    var validacion = (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/);
    var confirmacion = validacion.test(valor);
    if (confirmacion == true) {
        return true;
    }
    return false;
}

// Validación 6
function checkContrasena(valor) {
    var minusculas = "abcdefghijklmñopqrstuvwxyz";
    var minus = false;
    var mayusculas = "ABCDEFGHIJKLMÑOPQRSTUVWXYZ";
    var mayus = false;
    var numeros = "0123456789";
    var nums = false;
    var filtro = minusculas + mayusculas + numeros;
    var largor = valor.length;
    var permitidos = false;

    for (let i = 0; i < largor; i++) {
        if (filtro.indexOf(valor.charAt(i)) != -1) {}
        if (minusculas.indexOf(valor.charAt(i)) != -1) {
            minus = true;
        }
        if (mayusculas.indexOf(valor.charAt(i)) != -1) {
            mayus = true;
        }
        if (numeros.indexOf(valor.charAt(i)) != -1) {
            nums = true;
        }
    }
    if (nums === true && mayus === true && minus === true) {
        permitidos = true;
    }
    if (largor > 7 && permitidos === true) {
        return true;
    } else {
        return false;
    }
}
module.exports = {checkTelefono, checkNombre,checkGenero, checkDir,checkCorreo,checkContrasena};
