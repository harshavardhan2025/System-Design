public class Client {
    public static void main(String[] args) {
        PhonePe phonePe = new PhonePe();

        phonePe.makeTransaction("1234",600);
        System.out.println(phonePe.checkBalance("1234"));
    }
}
