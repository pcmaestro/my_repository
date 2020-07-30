package servletsAdmin;

import java.io.IOException; 

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.CochesDAO;
import daosimpl.CochesDAOimpl;
import model.Coche;
import validadores.Validador;

@WebServlet("/admin/ServletGuardarCambiosCoche")
public class ServletGuardarCambiosCoche extends HttpServlet {
	private static final long serialVersionUID = 1L;	
	
	private boolean valorValidacion;

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		//leemos los formularios y validamos que no estén vacios y que los
		//números no tengan puntos ni comas al viajar a la BBDD
		String marca = request.getParameter("marca").trim();
		String modelo = request.getParameter("modelo").trim();
		String color = request.getParameter("color").trim();
		String motor = request.getParameter("motor").trim();
		String cilindrada = request.getParameter("cilindrada").replace(".","").replace(",","").trim();
		String precio = request.getParameter("precio").replace(".","").replace(",","").trim();
		String telefono = request.getParameter("telefono").replace(".","").replace(",","").trim();
		String email = request.getParameter("email").trim();
		String id_categoria = request.getParameter("id_categoria");
		String id = request.getParameter("id");

		Coche coche = new Coche();
		coche.setMarca(marca);
		coche.setModelo(modelo);
		coche.setColor(color);
		coche.setMotor(motor);
		coche.setCilindrada(Integer.parseInt(cilindrada));
		coche.setPrecio(Integer.parseInt(precio));
		coche.setTelefono(Integer.parseInt(telefono));
		coche.setEmail(email);
		coche.setId_categoria(Integer.parseInt(id_categoria));
		
		coche.setId(Integer.parseInt(id));
		
		CochesDAO cochesDAO = new CochesDAOimpl();
		cochesDAO.guardarCambiosCoche(coche);
		response.sendRedirect("ServletListarAnuncios");		
	
	}//end doPost

}//end class
