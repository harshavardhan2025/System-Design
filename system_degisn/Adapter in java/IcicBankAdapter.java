public class IcicBankAdapter implements BankApis {

    IciciBankApi icicBankapi;

    public IcicBankAdapter() {
        this.icicBankapi = new IciciBankApi();
    }

    @Override
    public void makeTransaction(String accountNo, int amount) {
        icicBankapi.sendMoney(accountNo, amount);
    }

    @Override
    public int checkBalance(String accountNo) {
        return icicBankapi.fetchBalance(accountNo);
    }

}
