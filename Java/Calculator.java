import java.util.Scanner;

public class Calculator{
    public static String action;
    public static Scanner myObj = new Scanner(System.in);
    public static void main(String[] args) {
        
        System.out.println("hello world this is a calclulator");
        boolean loop = true;

            System.out.println("what do you want to do");
            System.out.println("please use coresponding input below");
            System.out.println("mul");
            System.out.println("div");
            System.out.println("sub");
            System.out.println("add");
            int c;
            if(myObj.hasNextLine()){
                action = myObj.nextLine();
              }
            System.out.println("what is number 1 ");
            int a = myObj.nextInt();
            System.out.println("what is number 2 ");
            int b = myObj.nextInt();
            myObj.close();
            if (action == "mul"){
                c = a*b;
                System.out.println(c);
            }
            else if (action == "div"){
                c = a/b;
                System.out.println(c);
            }
            else if (action == "sub"){
                c = a - b;
                System.out.println(c);
            }
            else if (action == "add"){
                c = a + b;
                System.out.println(c);
            }
            
    }
    
}