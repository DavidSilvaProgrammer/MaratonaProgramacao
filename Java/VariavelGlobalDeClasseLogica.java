public class Main {
    static int banana; // Tornar a variável banana estática

    public static void main(String[] args) {
        int valorBanana1 = metodoQueRetornaBanana1();

        System.out.println("Banana 1: " + valorBanana1);
        System.out.println("Atual valor global Banana: " + banana);
        //int valorBanana2 = metodoQueRetornaBanana2(); Se colocar aqui, valor global banana passa logo 5
        
        int valorBanana2 = metodoQueRetornaBanana2();
        
        System.out.println("Banana 2: " + valorBanana2);
        System.out.println("Atual valor global Banana: " + banana);
    }
    
    static int metodoQueRetornaBanana1() {
        banana = 3;
        return banana;
    }
    static int metodoQueRetornaBanana2() {
        banana = 5;
        return banana;
    }
    
    
}
