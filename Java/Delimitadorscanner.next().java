import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        System.out.print("Digite uma palavra: ");
        String palavra = scanner.next();
        
        System.out.print("Digite um número: ");
        int numero = scanner.nextInt();

        System.out.println("Número: " + numero);
        System.out.println("Palavra: " + palavra);

        scanner.close();
    }
}
