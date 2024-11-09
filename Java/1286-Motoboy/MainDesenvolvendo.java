import java.util.Scanner;
import java.util.ArrayList;

public class HelloWorld {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  
        
        int n = -1, p = -1;
        ArrayList<Integer> listaTempo = new ArrayList<>();
        ArrayList<Integer> listaPizza = new ArrayList<>();
        int pizza=0;
        int tempo=0;
        contaPizza=0;

        while (n != 0) {
            
            n = scanner.nextInt();
            if(n==0){
                break;
            }
            p = scanner.nextInt();
            for(int i = 1; i<= n; i++){
                tempo = scanner.nextInt();
                pizza = scanner.nextInt();
                listaTempo.add(tempo);
                listaPizza.add(pizza);
                while (p <= contaPizza){

                }
            }

        }

        
        
        scanner.close();  
    }
}
