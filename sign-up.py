from database import Database

class SignUP(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def submit(self):
        pass
        
one = SignUP('Amos', 'Mike', 'amos@gmail.com')

SignUP.submit(one)
