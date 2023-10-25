public class Main {
    public static void main(String[] args) {
        System.out.println("O método main foi chamado.");

       meuMetodoLocal(); // Chame o método diretamente
    }

    static void meuMetodoLocal() {
        System.out.println("Este é um método local dentro da classe Main.");
    }
}
