from validate_email import validate_email

class SignUP(object):
    users = []
    def __init__(self, first_name, last_name, email):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.email = email

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def submit(self):
        
        SignUP.users.append([self.first_name, self.last_name, self.email])
        
        return "Successfully Registered"

    @staticmethod
    def validate_email(email):
        if null:
            return "Please enter email address"

        elif validate_email('email') ==True:
            return "Email is valid"
        
        else:
            return "Email is invalid"

print(SignUP.validate_email('hhhhhhhh'))