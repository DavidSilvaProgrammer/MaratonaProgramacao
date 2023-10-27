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


************************


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner("Este é um exemplo de entrada.");

        String palavra1 = scanner.next(); // Lê "Este"
        String palavra2 = scanner.next(); // Lê "é"
        String palavra3 = scanner.next(); // Lê "um"
        String palavra4 = scanner.next(); // Lê "exemplo"
        String palavra5 = scanner.next(); // Lê "de"

        System.out.println("Palavra 1: " + palavra1);
        System.out.println("Palavra 2: " + palavra2);
        System.out.println("Palavra 3: " + palavra3);
        System.out.println("Palavra 4: " + palavra4);
        System.out.println("Palavra 5: " + palavra5);
    }
}
