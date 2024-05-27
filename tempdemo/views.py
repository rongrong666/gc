from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginView(View):


    def get(self, request):
        '''返回模板界面给前端'''

        # return HttpResponse()


        context = {
            'city':'beijing',
            'age':2134
        }


        return render(request, 'index.html', context)


