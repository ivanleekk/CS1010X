class BankAcct {
  protected int _acctNum;
  protected double _balance;

  // Constructors
  public BankAcct() {
    // initialize all attributes to 0
  }

  public BankAcct(int aNum, double bal) {
    // initialize attributes with user provided values
    _acctNum = aNum;
    _balance = bal;
  }

  // Methods
  public boolean withdraw(double amount) {
    if (_balance < amount)
      return false;
    _balance -= amount;
    return true;
  }

  public void deposit(double amount) {
    if (amount <= 0)
      return;
    _balance += amount;
  }

  public void print() {
    System.out.println("Account Number: " + _acctNum);
    System.out.printf("Balance: $%.2f\n", _balance);
  }
}

// Subclass
class LoanAcct extends BankAcct {
  protected double _rate;
  protected double _limit;

  public LoanAcct(int aNum, double bal, double rate, double limit) {
    _acctNum = aNum;
    _balance = bal;
    _rate = rate;
    _limit = limit;
  }

  // New method in subclass
  public void payInterest() {
    double interest = _balance * _rate;
    _balance += interest;
  }

  // Method Overriding
  public boolean withdraw(double amount) {
    if (_balance - amount < -_limit)
      return false;
    _balance -= amount;
    return true;
  }

  public void deposit(double amount) {
    if (amount <= 0)
      return;
    _balance += amount;
  }

  public boolean transfer(BankAcct fromAcct, BankAcct toAcct, double amount) {
    if (fromAcct.withdraw(amount)) {
      toAcct.deposit(amount);
      return true;
    }
    return false;
  }
}
