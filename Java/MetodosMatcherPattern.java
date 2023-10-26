import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class NumericalCharsExample {
    public static void main(String[] args) {
        String texto = "A string 1234 contém alguns números 5678.";

        // Defina a expressão regular para encontrar caracteres numéricos
        Pattern padrao = Pattern.compile("\\d");

        // Crie um objeto Matcher para encontrar as correspondências
        Matcher matcher = padrao.matcher(texto);

        // Use o Matcher para encontrar e imprimir os caracteres numéricos
        while (matcher.find()) {
            String caracterNumerico = matcher.group();
            System.out.println("Caracter numérico encontrado: " + caracterNumerico);
        }
    }
}
