class WseiEmails:
    def __init__(self, email):
        self.email = email
        
    def validate(self):
        return "@wsei.edu.pl" in self.email
            
    
    