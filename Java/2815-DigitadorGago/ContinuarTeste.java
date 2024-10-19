import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        
        // Lê a string do usuário
        System.out.print("Digite uma frase: ");
        String input = scanner.nextLine();
        
        // Divide a string em palavras
        String[] palavras = input.split(" ");
    
        StringBuilder resultado = new StringBuilder();
        
        // Remove a primeira e a segunda letra de cada palavra que satisfaz a condição
        for (String palavra : palavras) {
            if (palavra.length() > 3 && palavra.charAt(0) == palavra.charAt(2) && palavra.charAt(1) == palavra.charAt(3)) {
                resultado.append(palavra.substring(2)).append(" "); // Remove as duas primeiras letras
            } else {
                resultado.append(palavra).append(" "); // Mantém a palavra original
            }
        }
        
        // Exibe o resultado
        System.out.println("Resultado: " + resultado.toString().trim());
        
        scanner.close();
    }
}
