import java.util.*;

public class VehiclePlate {

   public static void main(String[] args) {
      System.out.println(generateCheckSum("SS", 11));
      System.out.println(generateCheckSum("ABC", 123));
      System.out.println(generateCheckSum("YZ", 9872));
      System.out.println(generateCheckSum("SGZ", 7758));
      Scanner stdIn = new Scanner(System.in);

      System.out.print("Vehicle Plate (excluding the checksum alphabet at the end): ");
      String plate = stdIn.nextLine();
      plate = plate.toUpperCase();
      String prefix = plate.replaceAll("[0123456789]", "");
      int suffix = Integer.parseInt(plate.replaceAll("[a-zA-Z]", ""));
      char checkSum = generateCheckSum(prefix, suffix);

      System.out.println("Vehicle Plate is: " + prefix + " " + suffix + " " + checkSum);

   } // end main

   /*********************************************************
      
   **********************************************************/
   public static char generateCheckSum(String prefix, int suffix) {
      // to convert char to int
      char FirstChar;
      char SecondChar;
      int FirstCharInt;
      int SecondCharInt;
      int[] store = new int[6];
      int[] mul = { 9, 4, 5, 4, 3, 2 };
      Character[] resultChar = { 'A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D',
            'C', 'B' };
      int tempSum = 0;
      int finalSum;

      if (prefix.length() == 1) {
         SecondChar = prefix.charAt(prefix.length() - 1);
         SecondCharInt = SecondChar - 'A' + 1;
         FirstCharInt = 0;
      } else {
         FirstChar = prefix.charAt(prefix.length() - 2);
         FirstCharInt = FirstChar - 'A' + 1;
         SecondChar = prefix.charAt(prefix.length() - 1);
         SecondCharInt = SecondChar - 'A' + 1;
         System.out.println("FirstChar: " + FirstChar);
         System.out.println("FirstCharInt: " + FirstCharInt);
         System.out.println("SecondChar: " + SecondChar);
         System.out.println("SecondCharInt: " + SecondCharInt);
      }
      store[0] = FirstCharInt;
      store[1] = SecondCharInt;
      // to get value of each digit
      for (int i = 4; i > 0; --i) {
         int divisor = 1;
         for (int j = 1; j < i; j++) {
            divisor = divisor * 10;
         }
         store[6 - i] = Math.floorDiv(suffix, divisor);
         suffix = suffix % divisor;
      }
      // do multiplication for each number
      for (int i = 0; i < store.length; i++) {
         store[i] = store[i] * mul[i];
      }
      System.out.println(Arrays.toString(store));
      for (int i = 0; i < store.length; i++) {
         tempSum = tempSum + store[i];
      }
      finalSum = tempSum % 19;
      System.out.println("finalSum: " + finalSum);
      return resultChar[finalSum];
   }// end generateCheckSum

}// end class