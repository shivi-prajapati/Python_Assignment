'''Assignment 5: Multi-Channel Notification System (Multiple Inheritance & MRO)'''

class Notifier:
    def __init__(self,sender_id:str):
        self.sender_id=sender_id

    def send(self,message):
        a=[f"[Notifier {self.sender_id}] general broadcast: {message}"]
        return a

class EmailNotifier(Notifier):
    def __init__(self,email_server:str,sender_id):
        self.email_server=email_server
        Notifier.__init__(self,sender_id)

    def send(self,message):
        l=[f"[Email via {self.email_server}] sending: {message}"]
        return l

class SMSNotifier(Notifier):
    def __init__(self,sms_gateway:str,sender_id):
        self.sms_gateway=sms_gateway
        Notifier.__init__(self,sender_id)

    def send(self,message):
        l=[f"[SMS via {self.sms_gateway}] sending: {message}"]
        l.extend(super().send(message))
        return l

class HybridAlertChannel(EmailNotifier, SMSNotifier):
    def __init__(self,sender_id:str,email_server:str,sms_gateway:str):
        EmailNotifier.__init__(self,email_server,sender_id)
        SMSNotifier.__init__(self,sms_gateway,sender_id)

    def send(self,message):
        log=["[HYBRID ALERT] Initiating dual channels..."]
        log.extend(super().send(message))
        log.extend(SMSNotifier.send(self,message))
        return log

def main():
    alert = HybridAlertChannel(sender_id="SYS-ADMIN", email_server="smtp.cdac.in", sms_gateway="gw.acts.com")
    logs = alert.send("Disk space 95%")

    for log in logs:
        print(log)

    print(HybridAlertChannel.mro())

if __name__=="__main__": main()












    


