from django.shortcuts import render

# View referente a página home
def index(request):
    return render('home/', 'sistema/templates/home.html')


# View referente a página cadastro
# View referente a página login
# View referente a página esqueci senha



