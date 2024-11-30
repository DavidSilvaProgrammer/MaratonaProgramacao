import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        int codPeça = scanner.nextInt();
        int nPeça = scanner.nextInt();
        float vPeça = scanner.nextFloat();

        float res = nPeça * vPeça;

        System.out.printf("VALOR A PAGAR: R$ %.2f%n", res);

        scanner.close();
    }
}
