import java.util.Scanner;

public class EntradaFloatDouble {
    public static void main(String[] args) {
        // Criando um scanner para ler a entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicitando ao usuário que insira um valor float
        System.out.print("Digite um número com ponto flutuante (float): ");
        float numeroFloat = scanner.nextFloat();  // Lê um valor float

        // Solicitando ao usuário que insira um valor double
        System.out.print("Digite um número com ponto flutuante (double): ");
        double numeroDouble = scanner.nextDouble();  // Lê um valor double

        // Imprimindo os valores armazenados
        System.out.println("\nO valor digitado para float é: " + numeroFloat);
        System.out.println("O valor digitado para double é: " + numeroDouble);

        // Fechando o scanner
        scanner.close();
    }
}
