function validar(){
    var marca = document.getElementById("marca").value;
    if( marca == null || marca.length == 0 || /^\s+$/.test(marca) ) {
        document.getElementById("marca").style.border = "3px #E12412";
        return false;}

    var modelo = document.getElementById("modelo").value;
    if( modelo == null || modelo.length == 0 || /^\s+$/.test(modelo) ) {
        return false;}

    var color = document.getElementById("color").value;
    if( color == null || color.length == 0 || /^\s+$/.test(color) ) {
        return false;}

    var pantalla = document.getElementById("pantalla").value;
    if( isNaN(pantalla) ) {
        return false;}

    var memoria = document.getElementById("memoria").value;
    if( isNaN(memoria) ) {
        return false;}    

    var anyo = document.getElementById("anyo").value;
    if( isNaN(anyo) ) {
        return false;}

    var precio = document.getElementById("precio").value;
    if( isNaN(precio) ) {
        return false;}

    var nombre = document.getElementById("nombre").value;
    if( nombre == null || nombre.length == 0 || /^\s+$/.test(nombre) ) {
        return false;}
    
    var telefono = document.getElementById("telefono").value;
    if( telefono == null || telefono.length == 0 || /^[6-9]{1}[0-9]{8}$/.test(telefono) ) {
        return false;}

    var email = document.getElementById("email").value;
    if( email == null || email.length == 0 || /^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/.test(email) ) {
        return false;}
    
}
 
if (validar() == false){
    alert("Todos los campos deben ser rellenados con valores válidos")
}