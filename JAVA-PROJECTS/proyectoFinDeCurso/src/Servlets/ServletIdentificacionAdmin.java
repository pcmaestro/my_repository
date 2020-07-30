package Servlets;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ServletIdentificacionAdmin
 */
@WebServlet("/ServletIdentificacionAdmin")
public class ServletIdentificacionAdmin extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	private static final String USER_ADMIN = "admin";
	private static final String PASS_ADMIN = "1234";

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String usuario = request.getParameter("usuario");
		String password = request.getParameter("password");		
		
		if(usuario.equals(USER_ADMIN) && password.equals(PASS_ADMIN)) {
			//Asigno la sesion y refresco el navegador de usuario con la siguiente ruta:
			request.getSession().setAttribute("adminOK", "ok");
			response.sendRedirect("loginAdminOK.jsp");
		}else {
			response.sendRedirect("loginAdmin.jsp");		
		}//end if
	}//end doPost
}//end class
