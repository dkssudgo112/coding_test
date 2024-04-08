import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();

    int[] P = new int[N];
    ArrayList<Integer> list = new ArrayList<Integer>();
    for (int i = 0; i < N; i++) {
        P[i] = scanner.nextInt();
        list.add(P[i]);
    }

    scanner.close();
    int[] P2 = Arrays.copyOf(P, P.length);

    Arrays.sort(P2);

    int result_time = 0;
    for (int i=0; i<N; i++){
        //System.out.print(P[i]);
        for(int j =0;j<=i;j++){
            result_time +=  P2[j];
        }

    }
    System.out.print(result_time);
    
    // Now you can use the variables N and P as needed
    }
}