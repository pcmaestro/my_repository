package servlets;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ServletInicio
 */
@WebServlet("/inicio")
public class ServletInicio extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ServletInicio() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		//la idea es que esto seria informaciones de bd
		List<Anuncio> anuncios = new ArrayList<Anuncio>();
		anuncios.add(new Anuncio("raton optico", "por 3,99 euros "
				+ "llamar a 123456"));
		anuncios.add(new Anuncio("portatil ", "por 499 euros "
				+ "llamar a 6789012"));
		anuncios.add(new Anuncio("raton optico", "por 4,99 euros "
				+ "llamar a 8976543"));
		request.setAttribute("anuncios", anuncios);
		
		
		//los servlets hacen una labor de control, 
		//lo mas normal es que el servlet tras realizar la operacion que 
		//se quiera hacer, redirija al usuario a una vista
		RequestDispatcher dispatcher = 
				getServletContext().getRequestDispatcher("/bienvenido.jsp");
		dispatcher.forward(request, response);
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
