public class Main {
    public static void main(String[] args) {
        System.out.println("O método main foi chamado.");

        Main objeto = new Main(); // Crie uma instância da classe Main
        objeto.meuMetodoLocal(); // Chame o método a partir do objeto
    }

    static void meuMetodoLocal() {
        System.out.println("Este é um método local dentro da classe Main.");
    }
}
