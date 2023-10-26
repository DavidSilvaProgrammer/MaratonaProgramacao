import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite uma sequência de caracteres: ");
        String input = scanner.nextLine();

        int numero = converterDigitosParaInteiro(input);

        System.out.println("Números convertidos para inteiro: " + numero);

        scanner.close();
    }

    public static int converterDigitosParaInteiro(String input) {
        StringBuilder digitos = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char caracter = input.charAt(i);

            if (Character.isDigit(caracter)) {
                digitos.append(caracter);
            }
        }

        if (digitos.length() > 0) {
            return Integer.parseInt(digitos.toString());
        } else {
            System.out.println("Nenhum dígito foi encontrado.");
            return 0;
        }
    }
}
