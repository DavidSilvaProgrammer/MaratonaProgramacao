import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Cria um objeto Scanner para ler dados da entrada padrão
        Scanner scanner = new Scanner(System.in);

        // Solicita ao usuário que digite dois números separados por espaço
        System.out.print("Digite dois números separados por espaço: ");
        
        // Lê dois números inteiros
        int numero1 = scanner.nextInt();
        int numero2 = scanner.nextInt();

        // Exibe os números lidos
        System.out.println("Número 1: " + numero1);
        System.out.println("Número 2: " + numero2);

        // Fecha o scanner para liberar os recursos
        scanner.close();
    }
}

