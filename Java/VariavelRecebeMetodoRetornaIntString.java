public class Main {
    public static void main(String[] args) {
        int valorInteiro = metodoQueRetornaInt();
        String valorString = metodoQueRetornaString();

        System.out.println("Valor Inteiro: " + valorInteiro);
        System.out.println("Valor String: " + valorString);
    }

    static int metodoQueRetornaInt() {
        // Este método retorna um valor int
        return 42;
    }

    static String metodoQueRetornaString() {
        // Este método retorna uma String
        return "Isso é uma String.";
    }
}
