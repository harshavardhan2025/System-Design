public class IciciBankApi {
    public void sendMoney(String accountNo, int amount){
        System.out.println("Sending money from Icici bank " + "accountNo = " + accountNo + " amount = " + amount);
    }

    public int fetchBalance(String accountNo){
        return 5000;
    }


}
