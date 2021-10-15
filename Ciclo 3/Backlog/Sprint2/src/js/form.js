module.exports = checkNombre;
module.exports = checkGenero;
module.exports = checkTelefono;
module.exports = checkDir;
module.exports = checkCorreo;
module.exports = checkContrasena;

// Validación 1
function checkNombre(valor){
    var numero = false;
    var largor = valor.length;

    for(i = 0; i < largor;i++){
        try{
            if(Number.isInteger(parseInt(valor[i]))){
                numero = true; 
            }
        }
        catch(e){}
    }  
    if((valor != null) && (largor > 3  && largor <= 30) && (numero == false)){
        return true;
    }
    return false;
}

// Validación 2
function checkGenero(valor) {
    if (valor.type=='checkbox'){
        if (valor.checked){
            return true;
        }
        return false; 
    }
    return false; 
}

// Validación 3
function checkTelefono(valor) {
    var cadena = valor.toString();
    var largor = cadena.length;
    document.write(cadena)
    var filtro = "0123456789";

    for (let i = 0; i < largor; i++) {
        if (largor == 7){
            if(filtro.indexOf(cadena.charAt(i)) != -1){}

            else{
                return false;
            }
            return true;
        }
        return false;
    }
}

// Validación 4
function checkDir(valor){
    var largor = valor.length, especial_chars = false;
    var filtro = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890#- ";

    for (let i = 0; i < largor; i++) {
        if(filtro.indexOf(valor.charAt(i)) != -1){}
        else{
            especial_chars = true;
        }
    }

    if(valor != null && (largor < 51 && largor > 0) && especial_chars == false){
        return true;
    }
    return false;
}

// Validación 5
function checkCorreo(valor){
    var validacion=(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/);
    var confirmacion= validacion.test(valor);
    if (confirmacion ==true){
        return true;
    } 
    return false;
}

// Validación 6