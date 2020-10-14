function soloLetras(e) {
  textoArea = document.getElementById("usuario").value;
  var total = textoArea.length;
  if (total == 0) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ"; //Se define todo el abecedario que se quiere que se muestre.
    especiales = [8, 9, 37, 39, 46, 6]; //Es la validación del KeyCodes, que teclas recibe el campo de texto.

    tecla_especial = false
    for (var i in especiales) {
      if (key == especiales[i]) {
        tecla_especial = true;
        break;
      }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
      return false;
    }

  } else if (total > 0) {
    if (window.event) { //asignamos el valor de la tecla a keynum
      keynum = e.keyCode; //IE
    } else {
      keynum = e.which; //FF
    }
    //comprobamos si se encuentra en el rango numérico y que teclas no recibirá.
    if ((keynum > 64 && keynum < 91) || (keynum > 47 && keynum < 58) || (keynum > 96 && keynum < 132) || keynum == 8 || keynum == 13 || keynum == 6) {
      return true;
    } else {
      return false;
    }

  }

}

function verificarPasswords() {
 
  // Ontenemos los valores de los campos de contraseñas 
  pass1 = document.getElementById('pass1');
  pass2 = document.getElementById('pass2');

  if (pass1.value != pass2.value) { 
    
        document.getElementById('msg').style.display = 'block';
  }
  else{
    document.getElementById('msg').style.display = 'none';
  }

}