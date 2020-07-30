package servlets;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.LibrosDAO;
import daos.LibrosDAOImpl;
import modelo.Libro;

@WebServlet("/guardarNuevoLibro")
public class ServletGuardarLibro extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// en getParameter indico el name del input cuya informacion
		// quiera obtener
		String titulo = request.getParameter("titulo");
		String autor = request.getParameter("autor");
		String paginas = request.getParameter("paginas");
		String precio = request.getParameter("precio");

		// validacion, queda mejor si se pone en otro sitio y se usa aquí
		//para no sobrecargar este servlet con validaciones
		String errorTitulo = "";
		String errorPaginas = "";
		String errorPrecio = "";
		if (titulo.trim().equals("")) {
			errorTitulo = "titulo vacio";
		} else if (titulo.length() < 3) {
			errorTitulo = "titulo menor de 3 caracteres";
		}
		int intPaginas = -1;
		try {
			intPaginas = Integer.parseInt(paginas);
		} catch (NumberFormatException e) {
			errorPaginas = "introduce un numero";
		}
		double doublePrecio = -1;
		try {
			doublePrecio = Double.parseDouble(precio.replace(",", "."));
		} catch (Exception e) {
			errorPrecio = "precio no valido";
		}
		//fin validacion
		
		
		if( !errorPaginas.equals("") || !errorTitulo.equals("") || 
				!errorPrecio.equals("")) {
			//no registro el libro y redirijo al formulario indicando error
			request.setAttribute("errorTitulo", errorTitulo);
			request.setAttribute("errorPaginas", errorPaginas);
			request.setAttribute("errorPrecio", errorPrecio);
			RequestDispatcher dispatcher = 
					getServletContext().getRequestDispatcher("/registrarLibro.jsp");
			dispatcher.forward(request, response);
			
		}else {
			LibrosDAO librosDAO = new LibrosDAOImpl();
			Libro l = new Libro(titulo, autor, intPaginas, doublePrecio);
			librosDAO.registrarLibro(l);
			RequestDispatcher dispatcher = 
					getServletContext().getRequestDispatcher("/registroLibroOK.jsp");
			dispatcher.forward(request, response);			
		}//end else
		
	}//end doPost

}//end class
