import java.util.Scanner;
import java.util.ArrayList;

public class TowerOfHanoi {
  String name;
  ArrayList[] peg;
  int numDiscs;

  public TowerOfHanoi(String name, int n) {
    this.name = name;
    this.numDiscs = n;
    this.peg = new ArrayList[3];
    // Write your code here
    for (int i = 0; i < 3; i++) {

      peg[i] = new ArrayList<Integer>();
      if (i == 0) {
        for (int j = 0; j < numDiscs; j++) {
          peg[i].add(j);
        }
      }
    }

  }

  private void moveDisc(int src, int des) {
    // Write your code here
    int discToMove;
    ArrayList<Integer> source = peg[src];
    ArrayList<Integer> desti = peg[des];
    discToMove = source.get(source.size() - 1);
    desti.add(discToMove);
    source.remove(source.size() - 1);
    printTower();
    return;
  }

  public void printTower() {
    // Write your code here
    for (int i = 0; i < 3; i++) {
      System.out.print("[ ");
      for (int j = 0; j < peg[i].size(); j++) {
        System.out.print(peg[i].get(j) + " ");
      }
      if (i == 2) {
        System.out.print("]");
      } else {
        System.out.print("], ");
      }

    }
    System.out.println();
    return;

  }

  public void makeMoves(int n, int src, int des, int aux) {
    if (n <= 0)
      return;
    makeMoves(n - 1, src, aux, des);
    moveDisc(src, des);
    makeMoves(n - 1, aux, des, src);
    return;
  }

  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter number of disks: ");
    int n = input.nextInt();
    TowerOfHanoi t = new TowerOfHanoi("Hanoi", n);
    t.printTower();
    t.makeMoves(n, 0, 2, 1);
  }

}
