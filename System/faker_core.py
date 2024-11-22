from faker import Faker

class SXSCLI_Faker:
    def __init__(self):
        self.fake = Faker()

    def sxscli_version(self):
        return "1.0.0"

    def generate_fake_person(self):
        return {
            "full_name": self.fake.name(),
            "address": self.fake.address(),
            "phone_number": self.fake.phone_number(),
            "email": self.fake.email(),
            "job": self.fake.job(),
            "company": self.fake.company(),
            "birthdate": self.fake.date_of_birth(minimum_age=18, maximum_age=90),
            "ssn": self.fake.ssn(),
            "username": self.fake.user_name(),
            "password": self.fake.password(),
            "credit_card": {
                "number": self.fake.credit_card_number(),
                "provider": self.fake.credit_card_provider(),
                "expiry_date": self.fake.credit_card_expire(),
                "security_code": self.fake.credit_card_security_code()
            },
            "profile": self.fake.profile(),
            "simple_profile": self.fake.simple_profile()
        }
    
    def generate_fake_card(self):
        return {
            "credit_card": {
                "number": self.fake.credit_card_number(),
                "provider": self.fake.credit_card_provider(),
                "expiry_date": self.fake.credit_card_expire(),
                "security_code": self.fake.credit_card_security_code()
            }
        }
    
    def generate_fake_phone_number(self):
        return {
            "phone_number": self.fake.phone_number()
        }
        
    def generate_fake_email(self):
        return {
            "email": self.fake.email()
        }
    
    def generate_fake_address(self):
        return {
            "country": self.fake.country(),
            "city": self.fake.city(),
            "street": self.fake.street_address(),
            "zipcode": self.fake.zipcode(),
            "state": self.fake.state()
        }
