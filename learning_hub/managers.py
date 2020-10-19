from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, password, role = 0):
        if not email or not username or not password:
            raise ValueError('One or more of required fields are missing')
        email = self.normalize_email(email)
        user = self.model(email = email,username = username, role = role)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, username, password):
        return self.create_user(email, username,  password, role = 1)


