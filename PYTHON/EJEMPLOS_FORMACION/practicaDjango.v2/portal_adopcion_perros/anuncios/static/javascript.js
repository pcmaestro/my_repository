
function hola(){
    console.log("llego al javascript")
}

function validar_usuario(){
    console.log("iniciada validacion")

    var regexText = new RegExp("^[a-zA-Z0-9]+\s?[a-zA-Z0-9]*\s?[a-zA-Z0-9]*\s?[a-zA-Z0-9]*$");
    var regexTf = new RegExp("^[6-9]{1}[0-9]{8}$");
    var regexMail = new RegExp("^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$");
    var regexPass = new RegExp("[a-z0-9_-]{4,8}$");

    var texto = document.getElementsByClassName("text").value;
    var telefono = document.getElementById("telefono").value;
    var email = document.getElementById("email").value;
    var password = document.getElementsByClassName("password").value;

    var validacion = true;
    console.log("Al empezar validacion tiene el valor " + validacion)
    if(regexText.test(texto)){              
        document.getElementsByClassName("text").style.border = "1px solid black";
        validacion = true;
        console.log("regexText es " + validacion)
        
    }else{
        document.getElementsByClassName("text").style.border = "2px solid red";
        validacion = false;   
        console.log("regexText es " + validacion)     
    }

    if(regexTf.test(telefono)){
        document.getElementById("telefono").style.border = "1px solid black";        
        validacion = true;
        console.log("regexTf es " + validacion)
    }else{
        document.getElementById("telefono").style.border = "2px solid red";
        validacion = false;
        console.log("regexTf es " + validacion)
        
    }  

    if(regexMail.test(email)){
        document.getElementById("email").style.border = "1px solid black";
        validacion = true;
        console.log("regexMail es " + validacion)
        
    }else{
        document.getElementById("email").style.border = "2px solid red";
        validacion = false;        
        console.log("regexMail es " + validacion)
    }

    if(regexPass.test(password)){
        document.getElementsByClassName("password").style.border = "1px solid black";
        validacion = true;      
        console.log("regexPass es " + validacion)
        
    }else{
        document.getElementsByClassName("password").style.border = "2px solid red";
        validacion = false;
        console.log("regexPass es " + validacion)
        
    }

    if(validacion == false){
        preventDefault()
        alert("Los campos en rojo no son correctos");
        
    }

    return validacion;
}