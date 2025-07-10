import hashlib
from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import User


## default automatically decide the db using shardrouter
# def register_user(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')

#         # Check if user exists in any shard
#         for shard in ['shard_1', 'shard_2', 'shard_3']:
#             if User.objects.using(shard).filter(email=email).exists():
#                 return render(request, 'users/register.html', {
#                     'error': 'User with this email already exists.'
#                 })

#         # Create user object
#         user = User(name=name, email=email)

#         # Get correct DB using Django's router
#         db = router.db_for_write(User, hints={'email': email})

#         # Save user (now routed automatically!)
#         user.save(using=db)

#         return HttpResponseRedirect('/thanks/')

#     return render(request, 'users/register.html')

## manual db selection explicitly using logic
# def register_user(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')

#         shard = get_shard_for_email(email)

#         # Check if user already exists in the correct shard
#         if User.objects.using(shard).filter(email=email).exists():
#             return render(request, 'users/register.html', {
#                 'error': 'User with this email already exists.'
#             })

#         user = User(name=name, email=email)
#         user.save(using=shard)
#         return HttpResponseRedirect('/thanks/')

#     return render(request, 'users/register.html')


# def get_shard_for_email(email):
#     """
#     Hashes the email and returns the shard name: shard_1 / shard_2 / shard_3
#     """
#     hash_val = int(hashlib.md5(email.encode()).hexdigest(), 16)
#     shard_num = (hash_val % 3) + 1
#     return f'shard_{shard_num}'


def thanks(request):
    return render(request, 'users/thanks.html')
