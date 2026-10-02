public class PhonePe {
    
    BankApis bankApis;
    public PhonePe(){
        this.bankApis = new YesBankAdapter();
    }
    public void makeTransaction(String accountNo, int amount){
        bankApis.makeTransaction(accountNo,amount);
    }

    public int checkBalance(String accountNO){
        return bankApis.checkBalance(accountNO);
    }
}
