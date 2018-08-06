import re

class SignUP(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = SignUP.validate_email(email)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def submit(self):
        pass

    @staticmethod
    def validate_email(email):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if match == None:
            return "invalid email address"
        
        else:
            print("email is valid")
            return email
            
