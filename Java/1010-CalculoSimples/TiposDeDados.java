import java.util.Scanner;

public class TiposDeDados {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // String
        System.out.print("Digite uma String: ");
        String texto = scanner.nextLine();

        // Inteiro
        System.out.print("Digite um número inteiro (int): ");
        int inteiro = scanner.nextInt();

        // Decimal de ponto flutuante (float)
        System.out.print("Digite um número decimal (float): ");
        float flutuante = scanner.nextFloat();

        // Decimal de dupla precisão (double)
        System.out.print("Digite um número decimal maior (double): ");
        double duplo = scanner.nextDouble();

        // Caractere (char)
        System.out.print("Digite um caractere (char): ");
        char caractere = scanner.next().charAt(0);

        // Booleano
        System.out.print("Digite um valor booleano (true/false): ");
        boolean booleano = scanner.nextBoolean();

        // Byte
        System.out.print("Digite um número pequeno (byte): ");
        byte pequeno = scanner.nextByte();

        // Curto (short)
        System.out.print("Digite um número curto (short): ");
        short curto = scanner.nextShort();

        // Longo (long)
        System.out.print("Digite um número longo (long): ");
        long longo = scanner.nextLong();

        // Exibindo os valores
        System.out.println("\nVocê digitou os seguintes valores:");
        System.out.println("String: " + texto);
        System.out.println("Int: " + inteiro);
        System.out.println("Float: " + flutuante);
        System.out.println("Double: " + duplo);
        System.out.println("Char: " + caractere);
        System.out.println("Boolean: " + booleano);
        System.out.println("Byte: " + pequeno);
        System.out.println("Short: " + curto);
        System.out.println("Long: " + longo);

        scanner.close();
    }
}
