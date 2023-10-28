import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe a quantidade de prédios: ");
        int n = scanner.nextInt();
        List<Integer>[] area = new List[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Informe o tamanho do prédio " + i + ": ");
            int c = scanner.nextInt();
            area[i] = new ArrayList<>(c);

            // Agora você pode adicionar elementos a cada lista individualmente
            for (int j = 0; j < c; j++) {
                area[i].add(scanner.nextInt());
            }
        }

        // Exemplo de como acessar elementos de cada lista
        for (int i = 0; i < n; i++) {
            System.out.println("Prédio " + i + ": " + area[i]);
        }

        scanner.close();
    }
}
