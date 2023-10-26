String string1 = "Hello";
String string2 = "hello";

if (string1.equalsIgnoreCase(string2)) {
    System.out.println("As strings são iguais, ignorando diferenças de maiúsculas e minúsculas.");
} else {
    System.out.println("As strings não são iguais.");
}


************************

import java.util.Scanner;

public class CompararStrings {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a primeira string: ");
        String primeiraString = scanner.nextLine();

        System.out.print("Digite a segunda string: ");
        String segundaString = scanner.nextLine();

        if (primeiraString.equals(segundaString)) {
            System.out.println("As strings são iguais.");
        } else {
            System.out.println("As strings não são iguais.");
        }

        scanner.close();
    }
}
