from faker import Faker
import random
import string
import json

class TestDataGenerator:
    """Generate test data for automated tests"""

    def __init__(self):
        self.fake = Faker()

    def generate_user_data(self):
        """Generate user data"""
        return {
            'username': self.fake.user_name(),
            'email': self.fake.email(),
            'password': self.generate_password(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'phone': self.fake.phone_number(),
            'address': self.fake.address(),
            'company': self.fake.company(),
            'job_title': self.fake.job(),
        }

    def generate_password(self, length=12):
        """Generate secure password"""
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_credit_card(self):
        """Generate credit card data"""
        return {
            'number': self.fake.credit_card_number(),
            'expiry': self.fake.credit_card_expire(),
            'cvv': self.fake.credit_card_security_code(),
            'provider': self.fake.credit_card_provider(),
        }

    def generate_test_file(self, filename, count=10):
        """Generate test data file"""
        data = []
        for _ in range(count):
            data.append(self.generate_user_data())

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        return filename
