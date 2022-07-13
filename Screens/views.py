from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'POST':
        request.session['company_name'] = request.POST.get('company_name')
        request.session['industry'] = request.POST.get('industry')
        request.session['company_add'] = request.POST.get('company_add')
        request.session['proj_disc'] = request.POST.get('proj_disc')
        request.session['prepared_by'] = request.POST.get('prepared_by')
        request.session['p_date'] = request.POST.get('p_date')
        request.session['reviewed_by'] = request.POST.get('reviewed_by')
        request.session['r_date'] = request.POST.get('r_date')
        request.session['portfolio'] = request.POST.get('portfolio')
        company_name = request.session.get('company_name')
        industry = request.session.get('industry')
        company_add = request.session.get('company_add')
        proj_disc = request.session.get('proj_disc')
        prepared_by = request.session.get('prepared_by')
        p_date = request.session.get('p_date')
        reviewed_by  = request.session.get('reviewed_by')
        r_date = request.session.get('r_date')
        portfolio = request.session.get('portfolio')

        context = {
            'company_name': company_name,
            'industry': industry,
            'company_add': company_add,
            'proj_disc': proj_disc,
            'prepared_by': prepared_by,
            'p_date': p_date,
            'reviewed_by': reviewed_by,
            'r_date': r_date,
            'portfolio': portfolio,

        }
        return render(request, 'initial-screen.html', context)
    else:
        return render(request, 'index.html')


def introduction(request):
    return render(request, 'introduction.html')


def initial_screen(request):
    return render(request, 'initial-screen.html')