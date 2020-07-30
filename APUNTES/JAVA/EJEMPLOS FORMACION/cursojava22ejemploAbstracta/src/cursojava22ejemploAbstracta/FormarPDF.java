package cursojava22ejemploAbstracta;

public class FormarPDF extends FormarDocumento{

	@Override
	public void formarCabecera() {
		System.out.println("formar cabecera pdf");
	}

	@Override
	public void formarCuerpo() {
		System.out.println("formar cuerpo pdf");		
	}

	@Override
	public void formarFirma() {
		System.out.println("formar firma pdf");
	}

	@Override
	public void formarPieDePagina() {
		System.out.println("formar pie de pagina pdf");
	}

}
