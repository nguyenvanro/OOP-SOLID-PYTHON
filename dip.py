"""
Dependency Inversion Principle
- Abstractions should not depend upon details. Details should depend upon abstractions
- High-level modules should not depend on low-level modules. 
    Both should depend on abstraction. 
    Furthermore, abstractions should not depend on details. 
    Details should depend on abstractions
"""

from abc import ABC, abstractmethod


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    

# abstraction
class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user):
        pass
    
    
# abstraction
class EmailService(ABC):
    @abstractmethod
    def send_mail(self, user, message):
        pass
    
    
# abstraction
class Logger(ABC):
    @abstractmethod
    def log_action(self, action):
        pass
    
    
class DatabaseUserRepositiry(UserRepository):
    def save_user(self, user):
        print(f"Saving user {user.username} to the database")
        
        
class SimpleEmailService(EmailService):
    def send_mail(self, user, message):
        print(f"Sending email to {user.email}: {message}")


class SimpleLogger(Logger):
    def log_action(self, action):
        print(f"Logging action:  {action}")


#  UserService depend on these abstractions
class UserService:
    def __init__(self, user_repo: UserRepository, email_serivice: EmailService, logger: Logger):
        self.user_repo = user_repo
        self.email_service = email_serivice
        self.logger = logger
        
        
    def register_user(self, user):
        self.user_repo.save_user(user)
        self.email_service.send_mail(user, "Welcome!")
        self.logger.log_action("User registered")
    
# Usage
user = User(username="nguyenvana", email="nguyenvana@gmail.com")
user_repo = DatabaseUserRepositiry()
email_service = SimpleEmailService()
logger = SimpleLogger()
user_service = UserService(user_repo, email_service, logger)
user_service.register_user(user)


