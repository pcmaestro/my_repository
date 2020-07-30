<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>

 <script>
 
 
 $(document).ready(function(){	 
	 
	 $("#body").load(function cargando(){
	 	console.log("Carga el Jquery");
	 });
	 
	 $("#formularioRegistro").submit(function validar(e){
			console.log("carga el JQuery");
		 	e.preventDefault();
			var marca = $("#marca").val;
			var modelo = $("#modelo").val;
			var color = $("#color").val;
			var motor = $("#motor").val;fu	
			var cilindrada = $("#cilindrada").val;
			var precio = $("#precio").val;
			var telefono = $("#telefono").val;
			var email = $("#email").val;
			
			//Patrones Regexp para evitar campos vacios o con espacios
			var textPattern = new RegExp("^\w+$");
			var cilindradaPattern = new RegExp("^[0-9]{4}$");
			var precioPattern = new RegExp("^[0-9]$");
			var telefonoPattern = new RegExp("^[6-9]{1}[0-9]{8}$");
			var emailPattern = new RegExp("^\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b$");
			
			//booleanos para validar las Regexp
			var marcav = false;
			var modelov = false;
			var colorv = false;
			var motorv = false;
			var cilindradav = false;
			var preciov = false;
			var telefonov = false;
			var emailv = false;
			
			if(textPattern.test(marca)){
				marcav = true;
			}else{
				$("#marca").css({border-color:"red", background-color:"pink", border-width:"2px"});
				$("#error").css(display:"block");
			}
			
			if(textPattern.test(modelo)){
				modelov = true;
			}else{
				$("#modelo").css({border-color:"red", background-color:"pink", border-width:"2px"});
				$("#error").css(display:"block");
			
			if(textPattern.test(color)){
				colorv = true;
			}else{
				$("#color").css({border-color:"red", background-color:"pink", border-width:"2px"});
				$("#error").css(display:"block");
			
			if(textPattern.test(motor)){
				motorv = true;
			}else{
				$("#motor").css({border-color:"red", background-color:"pink", border-width:"2px"});
				$("#error").css(display:"block");
			
			if(cilindradaPattern.test(cilindrada)){
				cilindradav = true;
			}else{
				$("#cilindrada").css({border-color:"red", background-color:"pink", border-width:"2px"});
				$("#error").css(display:"block");
				
			
			if(telefonoPattern.test(telefono)){
				telefonov = true;
			}else{
				$("#telefono").css({border-color:"red", background-color:"pink", border-width:"2px"});
				$("#error").css(display:"block");
					
			
			if(emailPattern.test(email)){
				emailv = true;
			}else{
				$("#email").css({border-color:"red", background-color:"pink", border-width:"2px"});
				$("#error").css(display:"block");
			
				
			if(marcav && modelov && colorv && motorv && cilindradav && preciov && telefonov && emailv){
				validacion = true;
			}else{
				validacion = false;
			}
			
			return validacion;
			
		});// end submit function

	}); //end JQuery
 
 
 </script>