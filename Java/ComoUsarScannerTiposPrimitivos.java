import java.util.Scanner;

public class TiposPrimitivos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar ao usuário que insira valores para diferentes tipos primitivos
        System.out.print("Digite um número inteiro (int): ");
        int numeroInt = scanner.nextInt();

        System.out.print("Digite um número em ponto flutuante (double): ");
        double numeroDouble = scanner.nextDouble();

        System.out.print("Digite um número em ponto flutuante (float): ");
        float numeroFloat = scanner.nextFloat();

        System.out.print("Digite um número longo (long): ");
        long numeroLong = scanner.nextLong();

        System.out.print("Digite um número de byte (byte): ");
        byte numeroByte = scanner.nextByte();

        System.out.print("Digite um número curto (short): ");
        short numeroShort = scanner.nextShort();

        System.out.print("Digite um caractere (char): ");
        char caractere = scanner.next().charAt(0);

        System.out.print("Digite um valor booleano (true ou false): ");
        boolean valorBooleano = scanner.nextBoolean();

        System.out.print("Digite uma String: ");
        String texto = scanner.next(); // Lê uma String

        // Imprimir os valores na tela
        System.out.println("Valores inseridos:");
        System.out.println("int: " + numeroInt);
        System.out.println("double: " + numeroDouble);
        System.out.println("float: " + numeroFloat);
        System.out.println("long: " + numeroLong);
        System.out.println("byte: " + numeroByte);
        System.out.println("short: " + numeroShort);
        System.out.println("char: " + caractere);
        System.out.println("boolean: " + valorBooleano);
        System.out.println("String: " + texto);

        scanner.close();
    }
}
