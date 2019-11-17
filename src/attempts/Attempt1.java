package attempts;
import codeanticode.eliza.*;
import processing.core.*;

public class Attempt1 extends PApplet{
	
	public static void main() {

		PApplet app = new PApplet();
		Eliza eliza;
		eliza = new Eliza(app);

		String response = eliza.processInput("Hello");
		println(response);
	}

}
