from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from App.models import UserInfo

REQUIER_LOGIN_JSON=[
    'app/index',
]

REQUIER_LOGIN=[
    'app/Shopping_Cart',
]



class loginMiddleware(MiddlewareMixin):
    def process_request(self,request):

        if request.path in REQUIER_LOGIN_JSON:
            user_id = request.session.get('user_id')

            if user_id:
                try:
                    user=UserInfo.objects.get(pk=user_id)
                    request.user = user
                except:
                    data={
                        'status':301,
                    'msg':'user not vavliable',
                    }
                    # return  redirect(reverse('app:login'))
                    return JsonResponse(data=data)
            else:
                # return redirect(reverse('app:login'))
                data = {
                    'status': 301,
                    'msg': 'user not login',
                }
                return JsonResponse(data=data)
            if request.path in REQUIER_LOGIN:
                user_id = request.session.get('user_id')

                if user_id:
                    try:
                        user = UserInfo.objects.get(pk=user_id)
                        request.user = user
                    except:

                        return  redirect(reverse('app:login'))

                else:
                    return redirect(reverse('app:login'))

