function hola(){
    console.log("llego a JS")
}

$(document).ready(function(){

    $('#id_form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");
        validacion = validar()
        if(validacion){
            create_post();
        }else{
            $("#resultado").html("Revise los campos marcados en rojo")
        }; //end event
    }); //end submit

    function validar(){
        console.log("validacion ejecutada")
        regexText = new RegExp("^[a-zñÑA-Z0-9]+\s?[a-zñÑA-Z0-9]*\s?[a-zñÑA-Z0-9]*\s?[a-zñÑA-Z0-9]*$");
        regexTf = new RegExp("^[6-9]{1}[0-9]{8}$");
        regexMail = new RegExp("^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$");

        var nombre = $("#id_nombre").val();
        var apellido_1 = $("#id_apellido_1").val();
        var apellido_2 = $("#id_apellido_2").val();
        var telefono = $("#telefono").val();
        var email = $("#email").val();

        validacion = false;

        if(regexText.test(nombre)){
            document.getElementById("id_nombre").style.border = "1px solid black";
            validacion = true;
            console.log("Nombre " + validacion)
            
        }else{
            document.getElementById("id_nombre").style.border = "2px solid red";
            validacion = false;   
            console.log("Nombre " + validacion)
        }
    
    
        if(regexText.test(apellido_1)){
            document.getElementById("id_apellido_1").style.border = "1px solid black";
            validacion = true;
            console.log("Apellido_1 " + validacion)
    
        }else{
            document.getElementById("id_apellido_1").style.border = "2px solid red";
            validacion = false;
            console.log("Apellido_1" + validacion)
        }
    
        if(regexText.test(apellido_2)){
            document.getElementById("id_apellido_2").style.border = "1px solid black";
            validacion = true;
            console.log("Apellido_2 " + validacion)
    
        }else{
            document.getElementById("id_apellido_2").style.border = "2px solid red";
            validacion = false;
            console.log("Apellido_2" + validacion)
        }


    
        /*if(regexTf.test(telefono) == true){
            document.getElementById("id_telefono").style.border = "1px solid black";        
            validacion = true;
            console.log("Telefono es " + validacion)
        }else{
            document.getElementById("id_telefono").style.border = "2px solid red";
            validacion = false;
            console.log("Telefono es " + validacion)
        }

    
        if(regexMail.test(email)){
            document.getElementById("id_email").style.border = "1px solid black";
            validacion = true;
            console.log("Email es " + validacion)
            
        }else{
            document.getElementById("id_email").style.border = "2px solid red";
            validacion = false;        
            console.log("Email es " + validacion)
        }
        */
        return validacion
    
    };// end validacion

    function create_post(){

        console.log("create post is working!")
        
        $.ajax({
            url: "guardar-formulario",
            type: "POST",
            data: $("#id_form").serialize(),
            success: function(json){
                                    $("#id_nombre").val("");
                                    $("#id_apellido_1").val("");
                                    $("#id_apellido_2").val("");
                                    $("#id_telefono").val("");
                                    $("#id_email").val("");
                                    $("#resultado").html("REGISTRO CORRECTO");
                                    console.log("ajax success OK")
                                    },

            error: function(xhr,errmsg,err){
                                    $("#resultado").html("REGISTRO INCORRECTO");
                                    console.log("ajax error")
                                    console.log(xhr)
                                    console.log(errmsg)
                                    console.log(err)
                                 }

        }); //end ajax


    }; //end create_post

}); //end jquery

$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

}); //end csrf
