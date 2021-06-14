from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
# Create your views here.

class HelloView(TemplateView):
    #初期化処理
    def __init__(self):
        self.params = {
            'title'     :'Hello',
            #'message'   :'your data',
            'form'      :HelloForm(),
            'result'   : None
            }
        
    #GETときの処理
    def get(self,request):
        return render(request, 'hello/index.html',self.params)
    
    #POST時の処理
    def post(self,request):
        if('check' in request.POST):
            self.params['result'] = 'Checked'
        else:
            self.params['result'] = 'Not Checked'
            
        self.params['form']= HelloForm(request.POST)
        
        return render(request, 'hello/index.html',self.params)
        
