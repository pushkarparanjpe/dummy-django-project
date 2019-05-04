from django.shortcuts import render
import helloapp.models


# Create your views here.
def hello_view(request):
    messages = helloapp.models.Message.objects.all()
    return render(request, template_name='helloapp/index.html', context={'messages': messages})
