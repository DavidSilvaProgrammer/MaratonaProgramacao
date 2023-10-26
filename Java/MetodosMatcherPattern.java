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

/*

    Você começa definindo uma string texto que contém a frase na qual você deseja encontrar caracteres numéricos.

    Em seguida, você define uma expressão regular \\d usando a classe Pattern. Essa expressão regular significa encontrar qualquer caractere que seja um dígito numérico.

    Um objeto Matcher é criado com a expressão regular e a string texto para encontrar correspondências.

    Em seguida, você usa um loop while com matcher.find() para encontrar todas as correspondências na string. O método find() encontra a próxima correspondência na string.

    Para cada correspondência encontrada, você usa matcher.group() para obter o caractere numérico encontrado e, em seguida, o imprime na tela.

Esse método é eficaz para encontrar caracteres numéricos em uma string usando expressões regulares, e é especialmente útil quando você precisa de flexibilidade na definição de padrões de busca.

*/

