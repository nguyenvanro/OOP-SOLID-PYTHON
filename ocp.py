"""
Open-Close Principle
- Software entities (classes, modules, function, etc.) should be open for extension, but closed for modification.

"""
from abc import ABC, abstractmethod


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    
class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user):
        pass
    
    
class DatabaseUserRepository(UserRepository):
    def save_user(self, user):
        print(f"Saving user {user.username} to the database")
    
    
class EmailService(ABC):
    @abstractmethod
    def send_mail(self, user, message):
        pass
    
    
class SimpleEmailService(EmailService):
    def send_mail(self, user, message):
        print(f"Sending email to {user.email}: {message}")
    

class AdvancedEmailService(EmailService):
    def send_mail(self, user, message):
        print(f"Sending email to {user.email}: {message}")
        # Additional functionality here
    
class Logger(ABC):
    @abstractmethod
    def log_action(self, action):
        pass


class SimpleLogger(Logger):
    def log_action(self, action):
        print(f"Logging action: {action}")
    
    
class AdvancedLogger(Logger):
    def log_action(self, action):
        print(f"Logging action: {action}")
        
        
# Usage
user = User(username="nguyenvana", email="nguyenvana@gmail.com")
user_repo = DatabaseUserRepository()
user_repo.save_user(user)

advanced_email_service = AdvancedEmailService()
advanced_email_service.send_mail(user, "Welcome!")

advanced_logger = AdvancedLogger()
advanced_logger.log_action("User created")
