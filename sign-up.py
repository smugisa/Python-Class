import re

class SignUP(object):
    users = []
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def submit(self):
        
        SignUP.users.append([self.first_name, self.last_name, self.email])
        
        return "Successfully Registered"

    @staticmethod
    def validate_email(email):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if match == None:
            return "invalid email address"
        
        else:           
           return "email is valid" +email



