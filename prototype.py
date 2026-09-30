from abc import ABC, abstractmethod



#Prototype


class Notification(ABC):

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def send(self):
        pass


#EmailNotification


class EmailNotification(Notification):

    def __init__(self, message):
        self.message = message

    def clone(self):
        return EmailNotification(self.message)

    def send(self):
        print("Sending Email:", self.message)


#SMSNotification


class SMSNotification(Notification):

    def __init__(self, message):
        self.message = message

    def clone(self):
        return SMSNotification(self.message)

    def send(self):
        print("Sending SMS:", self.message)



#PushNotification


class PushNotification(Notification):

    def __init__(self, message):
        self.message = message

    def clone(self):
        return PushNotification(self.message)

    def send(self):
        print("Sending Push Notification:", self.message)


#WhatsAppNotification


class WhatsAppNotification(Notification):

    def __init__(self, message):
        self.message = message

    def clone(self):
        return WhatsAppNotification(self.message)

    def send(self):
        print("Sending WhatsApp:", self.message)



#Registry


class NotificationRegistry:

    def __init__(self):
        self.notifications = {}

    def add(self, name, notification):
        self.notifications[name] = notification

    def get(self, name):
        return self.notifications[name].clone()




registry = NotificationRegistry()


#Create templates
email = EmailNotification("Welcome to our application")
sms = SMSNotification("Your OTP is 123456")
push = PushNotification("You have a new message")
whatsapp = WhatsAppNotification("Hello! Welcome")


#Register templates
registry.add("welcome-email", email)
registry.add("otp-sms", sms)
registry.add("new-message-push", push)
registry.add("welcome-whatsapp", whatsapp)


#Get NEW objects by cloning templates
email1 = registry.get("welcome-email")
sms1 = registry.get("otp-sms")
push1 = registry.get("new-message-push")
whatsapp1 = registry.get("welcome-whatsapp")


#Send notifications
email1.send()
sms1.send()
push1.send()
whatsapp1.send()


#Check that they are different objects
print(email1 is email)      
print(sms1 is sms)          
print(push1 is push)        
print(whatsapp1 is whatsapp) 