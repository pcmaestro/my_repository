
package com.mycompany.mavenproject1;
 
import java.util.regex.Matcher;
import java.util.regex.Pattern;





public class NewClass {
  public static void main(String[] args) {
      
      boolean validacion;
      
      String text = "1234";
      
      Pattern patronEmail = Pattern.compile("^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,6}$", Pattern.CASE_INSENSITIVE);
		
      Matcher matcher = patronEmail.matcher(text);
		
      boolean matchfound = matcher.find();
		
    if(matchfound) {
            validacion = true;
    }else {
            validacion = false;
    }

    System.out.println("validacion = "+ validacion)
      
  }
}
