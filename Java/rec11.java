import java.util.*;

class Solver {
    public int old_fib(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return old_fib(n - 1) + old_fib(n - 2);
        }
    }

    public long fib(long n) {
        if (n <= 2)
            return 1;
        long a = 1, b = 1, c;
        for (int i = 3; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;// the value must be initialised in order for it to be compiled,
        // i.e c cannot be returned as there is no initial value for c
    }

    private int[] denomination = { 1, 5, 10, 20, 50 };

    public int cc(int amount, int d) {
        if (amount == 1) {
            return 1;
        } else if (d == 0 || amount < 0) {

            return 0;
        } else {
            return cc(amount - denomination[d - 1], d) + cc(amount, d - 1);

        }
    }

    private int[][] dp = new int[105][6];

    public int dp_cc(int amount) {
        // dp [i][j] = dp[i-denomination[j-1]][j] + dp[i][j-1];
        for (int j = 1; j <= 5; ++j) {
            dp[0][j] = 1;
        }
        for (int j = 1; j <= 5; ++j) {
            for (int i = 1; i <= amount; ++i) {
                if (i >= denomination[j - 1]) {
                    dp[i][j] = dp[i - denomination[j - 1]][j] + dp[i][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1];
                }
            }

        }
        for (int i = 0; i <= 5; ++i) {
            System.out.print(i + ": ");
            for (int j = 0; j <= 5; ++j) {
                System.out.print(dp[i][j] + " ");
            }
            System.out.print("\n");

        }
        return dp[amount][5];
    }

    private int[] dp2 = new int[105];

    public int dp_cc2(int amount) {
        // dp2[i] = dp2[i - denomination[j-1]] + dp2[i];
        // dp2[i] += dp2[i - denomination[j-1]]
        for (int i = 0; i <= amount; ++i) {
            dp2[i] = 0;
        }
        dp2[0] = 1;
        for (int j = 1; j <= 5; ++j) {
            System.out.print(j + ": ");
            for (int i = 1; i <= amount; ++i) {
                if (i >= denomination[j - 1]) {
                    dp2[i] += dp2[i - denomination[j - 1]];
                }
                System.out.print(dp2[i] + " ");
            }
            System.out.print("\n");
        }
        return dp2[amount];
    }

    public List<List<Integer>> split(List<Integer> arr, int n) {
        List<Integer> le = new ArrayList<>();
        List<Integer> gt = new ArrayList<>();

        for (int i = 0; i < arr.size(); ++i) {
            if (arr.get(i) <= n) {
                le.add(arr.get(i));
            } else {
                gt.add(arr.get(i));
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        result.add(le);
        result.add(gt);

        return result;
    }

    private Random rn = new Random();

    public List<Integer> quick_sort(List<Integer> arr) {
        if (arr.size() <= 1) {
            return arr;
        }

        int idx = rn.nextInt(arr.size());
        int n = arr.get(idx);

        List<List<Integer>> spl = split(arr, n);

        List<Integer> sorted_le = quick_sort(spl.get(0));
        List<Integer> sorted_gt = quick_sort(spl.get(1));

        List<Integer> result = new ArrayList<>();

        result.addAll(sorted_le);
        result.addAll(sorted_gt);
        // for (int x : sorted_le) {
        // result.add(x);
        // }
        // for (int x : sorted_gt) {
        // result.add(x);
        // }

        return result;
    }
}

public class rec11 {
    public static void main(String[] args) {
        // System.out.println(old_fib(46));
        // System.out.println(old_fib(47));
        Solver solver = new Solver();
        // for (int i = 1; i <= 47; i++) {
        // System.out.println(i + ": " + solver.fib(i));
        // }
        // System.out.println(solver.cc(6, 5));
        // System.out.println(solver.dp_cc2(20));
        List<Integer> arr = new ArrayList<>();
        for (int i = 10; i >= 0; --i) {
            arr.add(i);
        }
        // System.out.println(solver.split(arr, 5));
        System.out.println(solver.quick_sort(arr));
    }
}