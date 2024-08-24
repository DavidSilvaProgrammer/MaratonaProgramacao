import java.util.Scanner;

public class CombinacoesDias {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        final int MODULO = 1713371337;

        while (true) {
            int D1 = scanner.nextInt();
            int D2 = scanner.nextInt();

            if (D1 == 0 && D2 == 0) {
                break;
            }

            long combinacoes = (long) D1 * D2; // Usamos long para evitar overflow
            combinacoes %= MODULO;

            System.out.println(combinacoes);
        }

        scanner.close();
    }
}
