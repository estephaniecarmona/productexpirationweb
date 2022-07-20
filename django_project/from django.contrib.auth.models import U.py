from django.contrib.auth.models import User
from users.models import Profile
user = User.objects.get(username='estephanie')
profile = Profile(user=user)
profile.save()