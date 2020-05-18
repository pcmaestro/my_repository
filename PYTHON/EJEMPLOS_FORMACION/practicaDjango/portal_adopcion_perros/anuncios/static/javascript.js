
function hola(){
    console.log("llego al javascript")
}

function validar_usuario(event){
    console.log("iniciada validacion")

    var regexText = new RegExp("^[a-zA-Z0-9]+\s?[a-zA-Z0-9]*\s?[a-zA-Z0-9]*\s?[a-zA-Z0-9]*$");
    var regexTf = new RegExp("^[6-9]{1}[0-9]{8}$");
    var regexMail = new RegExp("^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$");
    var regexPass = new RegExp("[a-z0-9_-]{4,8}$");

    var nombre = document.getElementById("nombre").value;
    var apellido_1 = document.getElementById("apellido_1").value;
    var apellido_2 = document.getElementById("apellido_2").value;
    var telefono = document.getElementById("telefono").value;
    var email = document.getElementById("email").value;
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;

    var validacion = true;

    console.log("Al empezar validacion tiene el valor " + validacion)

    if(regexText.test(nombre)){
        document.getElementById("nombre").style.border = "1px solid black";
        validacion = true;
        console.log("Nombre " + validacion)
        
    }else{
        document.getElementById("nombre").style.border = "2px solid red";
        validacion = false;   
        console.log("Nombre " + validacion)
    }


    if(regexText.test(apellido_1)){
        document.getElementById("apellido_1").style.border = "1px solid black";
        validacion = true;
        console.log("Apellido_1 " + validacion)

    }else{
        document.getElementById("apellido_1").style.border = "2px solid red";
        validacion = false;
        console.log("Apellido_1" + validacion)
    }

    if(regexText.test(apellido_2)){
        document.getElementById("apellido_2").style.border = "1px solid black";
        validacion = true;
        console.log("Apellido_2 " + validacion)

    }else{
        document.getElementById("apellido_2").style.border = "2px solid red";
        validacion = false;
        console.log("Apellido_2" + validacion)
    }


    if(regexTf.test(telefono)){
        document.getElementById("telefono").style.border = "1px solid black";        
        validacion = true;
        console.log("Telefono es " + validacion)
    }else{
        document.getElementById("telefono").style.border = "2px solid red";
        validacion = false;
        console.log("Telefono es " + validacion)
    }  

    if(regexMail.test(email)){
        document.getElementById("email").style.border = "1px solid black";
        validacion = true;
        console.log("Email es " + validacion)
        
    }else{
        document.getElementById("email").style.border = "2px solid red";
        validacion = false;        
        console.log("Email es " + validacion)
    }

    if(regexPass.test(password1)){
        document.getElementById("password1").style.border = "1px solid black";
        validacion = true;      
        console.log("Password1 es " + validacion)
        
    }else{
        document.getElementById("password1").style.border = "2px solid red";
        validacion = false;
        console.log("Password1 es " + validacion)
    }

        if(regexPass.test(password2)){
        document.getElementById("password2").style.border = "1px solid black";
        validacion = true;
        console.log("Password2 es " + validacion)

    }else{
        document.getElementById("password2").style.border = "2px solid red";
        validacion = false;
        console.log("Password2 es " + validacion)
    }

    if(password1 == password2){
        document.getElementById("password1").style.border = "1px solid black";
        document.getElementById("password2").style.border = "1px solid black";
        validacion = true;
    }else{
        document.getElementById("password1").style.border = "2px solid red";
        document.getElementById("password2").style.border = "2px solid red";
        validacion = false;
        console.log("La verificación de password no coincide")

    }

    if(validacion == false){
        event.preventDefault()
        alert("Los campos en rojo no son correctos");
    }

    return validacion;
}