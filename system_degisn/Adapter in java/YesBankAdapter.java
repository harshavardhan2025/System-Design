public class YesBankAdapter implements BankApis{

    YesBankApi yesBankApi;
    public YesBankAdapter(){
        this.yesBankApi = new YesBankApi();
    }


    @Override
    public void makeTransaction(String accountNo, int amount) {
        yesBankApi.makeTranfer(accountNo,amount);
    }

    @Override
    public int checkBalance(String accountNo) {
        return yesBankApi.getBalance(accountNo);
    }
}
