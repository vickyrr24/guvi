import java.util.Scanner
public class test {

    public static void main(String[] args) {

        String input;
        Scanner obj = new Scanner(system.in)
        input = obj.nextLine();
        String output = new String();

        for (int i = 0; i < input.length(); i++) {
            for (int j = 0; j < output.length(); j++) {
                if (input.charAt(i) != output.charAt(j)) {
                    output = output + input.charAt(i);
                }
            }
        }

        System.out.println(output.length());

    }
