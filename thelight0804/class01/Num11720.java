import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        int sum = 0; //덧셈 결과

        //숫자의 개수 입력
        Scanner sc = new Scanner(System.in);
        String count = sc.nextLine();
        int countNum = Integer.parseInt(count);

        //합할 숫자 입력
        char[] numArr = sc.nextLine().toCharArray();

        //숫자 덧셈
        for(int i=0; i < countNum; i++)
            sum += Character.getNumericValue(numArr[i]);

        //결과 출력
        System.out.println(sum);
    }
}