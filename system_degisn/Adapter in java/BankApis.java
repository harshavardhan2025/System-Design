public interface BankApis {
    public void makeTransaction(String accountNo, int amount);

    public int checkBalance(String accountNo);

}
