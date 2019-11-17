package codeanticode.eliza;
//import codeanticode.eliza.*;

public class Test
{
public static void main (String[] args)
{   
    Eliza eliza;
    eliza = new Eliza();

    String response = eliza.processInput("Hello");
    System.out.println(response);

}
}