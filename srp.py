"""
Single Responsibility Principle
- A class should have only one reason to change
This means that a class should have only one responsibility.
If a class takes care of more than one task, then should separate those task into separate classes.
"""

class User:
  def __init__(self, username, email):
    self.username = username
    self.email = email
    
    
class UserRepository:
  def save_user(self, user):
    # Code to save user to a database
    print(f"Saving user {user.username} to the database")
    
    
class EmailService:
  def send_mail(self, user, message):
    # Code to send an email
    print(f"Sending email to {user.email}: {message}")
    
    
class Logger:
  def log_action(self, action):
    # Code to log an action
    print(f"Logging action: {action}")
    
    
# Usage
user = User(username="nguyenvana", email="nguyenvana@gmail.com")
user_repo = UserRepository()
user_repo.save_user(user)

email_service = EmailService()
email_service.send_mail(user, "Welcome!")

logger = Logger()
logger.log_action("User created")