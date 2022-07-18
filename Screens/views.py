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
    if request.method == 'POST':
        is1_1 = request.POST.get('is1_1')
        is1_2 = request.POST.get('is1_2')
        is1_3 = request.POST.get('is1_3')
        is1_4 = request.POST.get('is1_4')
        is1_5 = request.POST.get('is1_5')
        is1_6 = request.POST.get('is1_6')
        is1_7 = request.POST.get('is1_7')
        is1_8 = request.POST.get('is1_8')
        is1_9 = request.POST.get('is1_9')
        is1_10 = request.POST.get('is1_10')
        is1_11 = request.POST.get('is1_11')
        is1_12 = request.POST.get('is1_12')
        is1_13 = request.POST.get('is1_13')

        as1_1 = request.POST.get('as1_1')
        as1_2 = request.POST.get('as1_2')
        as1_3 = request.POST.get('as1_3')
        as1_4 = request.POST.get('as1_4')
        as1_5 = request.POST.get('as1_5')
        as1_6 = request.POST.get('as1_6')
        as1_7 = request.POST.get('as1_7')
        as1_8 = request.POST.get('as1_8')
        as1_9 = request.POST.get('as1_9')
        as1_10 = request.POST.get('as1_10')

        cs1_1 = request.POST.get('cs1_1')
        cs1_2 = request.POST.get('cs1_2')
        cs1_3 = request.POST.get('cs1_3')
        cs1_4 = request.POST.get('cs1_4')
        cs1_5 = request.POST.get('cs1_5')
        cs1_6 = request.POST.get('cs1_6')
        cs1_7 = request.POST.get('cs1_7')
        cs1_8 = request.POST.get('cs1_8')
        cs1_9 = request.POST.get('cs1_9')
        cs1_10 = request.POST.get('cs1_10')
        cs1_11 = request.POST.get('cs1_11')

        ks1_1 = request.POST.get('ks1_1')
        ks1_2 = request.POST.get('ks1_2')
        ks1_3 = request.POST.get('ks1_3')
        ks1_4 = request.POST.get('ks1_4')
        ks1_5 = request.POST.get('ks1_5')
        ks1_6 = request.POST.get('ks1_6')
        ks1_7 = request.POST.get('ks1_7')
        ks1_8 = request.POST.get('ks1_8')
        ks1_9 = request.POST.get('ks1_9')
        ks1_10 = request.POST.get('ks1_10')
        ks1_11 = request.POST.get('ks1_11')
        ks1_12 = request.POST.get('ks1_12')
        ks1_13 = request.POST.get('ks1_13')
        ks1_14 = request.POST.get('ks1_14')

        rs1_1 = request.POST.get('rs1_1')
        rs1_2 = request.POST.get('rs1_2')
        rs1_3 = request.POST.get('rs1_3')
        rs1_4 = request.POST.get('rs1_4')
        rs1_5 = request.POST.get('rs1_5')
        rs1_6 = request.POST.get('rs1_6')
        rs1_7 = request.POST.get('rs1_7')
        rs1_8 = request.POST.get('rs1_8')
        rs1_9 = request.POST.get('rs1_9')
        rs1_10 = request.POST.get('rs1_10')
        rs1_11 = request.POST.get('rs1_11')
        rs1_12 = request.POST.get('rs1_12')
        rs1_13 = request.POST.get('rs1_13')
        rs1_14 = request.POST.get('rs1_14')

        input = {
            'is1_1': is1_1,
            'is1_2': is1_2,
            'is1_3': is1_3,
            'is1_4': is1_4,
            'is1_5': is1_5,
            'is1_6': is1_6,
            'is1_7': is1_7,
            'is1_8': is1_8,
            'is1_9': is1_9,
            'is1_10': is1_10,
            'is1_11': is1_11,
            'is1_12': is1_12,
            'is1_13': is1_13,

            'as1_1': as1_1,
            'as1_2': as1_2,
            'as1_3': as1_3,
            'as1_4': as1_4,
            'as1_5': as1_5,
            'as1_6': as1_6,
            'as1_7': as1_7,
            'as1_8': as1_8,
            'as1_9': as1_9,
            'as1_10': as1_10,

            'cs1_1': cs1_1,
            'cs1_2': cs1_2,
            'cs1_3': cs1_3,
            'cs1_4': cs1_4,
            'cs1_5': cs1_5,
            'cs1_6': cs1_6,
            'cs1_7': cs1_7,
            'cs1_8': cs1_8,
            'cs1_9': cs1_9,
            'cs1_10': cs1_10,
            'cs1_11': cs1_11,

            'ks1_1': ks1_1,
            'ks1_2': ks1_2,
            'ks1_3': ks1_3,
            'ks1_4': ks1_4,
            'ks1_5': ks1_5,
            'ks1_6': ks1_6,
            'ks1_7': ks1_7,
            'ks1_8': ks1_8,
            'ks1_9': ks1_9,
            'ks1_10': ks1_10,
            'ks1_11': ks1_11,
            'ks1_12': ks1_12,
            'ks1_13': ks1_13,
            'ks1_14': ks1_14,

            'rs1_1': rs1_1,
            'rs1_2': rs1_2,
            'rs1_3': rs1_3,
            'rs1_4': rs1_4,
            'rs1_5': rs1_5,
            'rs1_6': rs1_6,
            'rs1_7': rs1_7,
            'rs1_8': rs1_8,
            'rs1_9': rs1_9,
            'rs1_10': rs1_10,
            'rs1_11': rs1_11,
            'rs1_12': rs1_12,
            'rs1_13': rs1_13,
            'rs1_14': rs1_14,
        }

        table = totalscoreinitial(input, request)
        is_avg_score = table.is_all_score()[1]

        table = AssessmentTotalscore(input, request)
        as_total_score = table.as_all_score()[0]
        as_avg_score = table.as_all_score()[1]

        table = Customertotalscore(input, request)
        cs_total_score = table.cs_all_score()[0]
        cs_avg_score = table.cs_all_score()[1]

        table = Kyctotalscore(input, request)
        ks_total_score = table.ks_all_score()[0]
        ks_avg_score = table.ks_all_score()[1]

        table = Regulatorytotalscore(input, request)
        rs_total_score = table.rs_all_score()[0]
        rs_avg_score = table.rs_all_score()[1]

        import ipdb
        ipdb.set_trace()
        total_avg = ((as_avg_score + cs_avg_score + ks_avg_score + rs_avg_score) / 4)
        total_avg = "{:.2f}".format(total_avg)

        context = {
            'input': input,
            'is_avg_score': is_avg_score,
            'as_total_score': as_total_score,
            'as_avg_score': as_avg_score,
            'cs_total_score': cs_total_score,
            'cs_avg_score': cs_avg_score,
            'ks_total_score': ks_total_score,
            'ks_avg_score': ks_avg_score,
            'rs_total_score': rs_total_score,
            'rs_avg_score': rs_avg_score,
            'total_avg': total_avg,
        }
        return render(request, 'final_score.html', context)
    else:
        return render(request, 'initial-screen.html')


class totalscoreinitial:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def is1_1(self):
        self.score = 0
        if self.input.get('is1_1') == '1':
            self.score = 1
        elif self.input.get('is1_1') == '2':
            self.score = 2
        elif self.input.get('is1_1') == '3':
            self.score = 3
        elif self.input.get('is1_1') == '4':
            self.score = 4
        return self.score

    def is1_2(self):
        self.score = 0
        if self.input.get('is1_2') == '1':
            self.score = 1
        elif self.input.get('is1_2') == '2':
            self.score = 2
        elif self.input.get('is1_2') == '3':
            self.score = 3
        elif self.input.get('is1_2') == '4':
            self.score = 4
        return self.score

    def is1_3(self):
        self.score = 0
        if self.input.get('is1_3') == '1':
            self.score = 1
        elif self.input.get('is1_3') == '2':
            self.score = 2
        elif self.input.get('is1_3') == '3':
            self.score = 3
        elif self.input.get('is1_3') == '4':
            self.score = 4
        return self.score

    def is1_4(self):
        self.score = 0
        if self.input.get('is1_4') == '1':
            self.score = 1
        elif self.input.get('is1_4') == '2':
            self.score = 2
        elif self.input.get('is1_4') == '3':
            self.score = 3
        elif self.input.get('is1_4') == '4':
            self.score = 4
        return self.score

    def is1_5(self):
        self.score = 0
        if self.input.get('is1_5') == '1':
            self.score = 1
        elif self.input.get('is1_5') == '2':
            self.score = 2
        elif self.input.get('is1_5') == '3':
            self.score = 3
        elif self.input.get('is1_5') == '4':
            self.score = 4
        return self.score

    def is1_6(self):
        self.score = 0
        if self.input.get('is1_6') == '1':
            self.score = 1
        elif self.input.get('is1_6') == '2':
            self.score = 2
        elif self.input.get('is1_6') == '3':
            self.score = 3
        elif self.input.get('is1_6') == '4':
            self.score = 4
        return self.score

    def is1_7(self):
        self.score = 0
        if self.input.get('is1_7') == '1':
            self.score = 1
        elif self.input.get('is1_7') == '2':
            self.score = 2
        elif self.input.get('is1_7') == '3':
            self.score = 3
        elif self.input.get('is1_7') == '4':
            self.score = 4
        return self.score

    def is1_8(self):
        self.score = 0
        if self.input.get('is1_8') == '1':
            self.score = 1
        elif self.input.get('is1_8') == '2':
            self.score = 2
        elif self.input.get('is1_8') == '3':
            self.score = 3
        elif self.input.get('is1_8') == '4':
            self.score = 4
        return self.score

    def is1_9(self):
        self.score = 0
        if self.input.get('is1_9') == '1':
            self.score = 1
        elif self.input.get('is1_9') == '2':
            self.score = 2
        elif self.input.get('is1_9') == '3':
            self.score = 3
        elif self.input.get('is1_9') == '4':
            self.score = 4
        return self.score

    def is1_10(self):
        self.score = 0
        if self.input.get('is1_10') == '1':
            self.score = 1
        elif self.input.get('is1_10') == '2':
            self.score = 2
        elif self.input.get('is1_10') == '3':
            self.score = 3
        elif self.input.get('is1_10') == '4':
            self.score = 4
        return self.score

    def is1_11(self):
        self.score = 0
        if self.input.get('is1_11') == '1':
            self.score = 1
        elif self.input.get('is1_11') == '2':
            self.score = 2
        elif self.input.get('is1_11') == '3':
            self.score = 3
        elif self.input.get('is1_11') == '4':
            self.score = 4
        return self.score

    def is1_12(self):
        self.score = 0
        if self.input.get('is1_12') == '1':
            self.score = 1
        elif self.input.get('is1_12') == '2':
            self.score = 2
        elif self.input.get('is1_12') == '3':
            self.score = 3
        elif self.input.get('is1_12') == '4':
            self.score = 4
        return self.score

    def is1_13(self):
        self.score = 0
        if self.input.get('is1_13') == '1':
            self.score = 1
        elif self.input.get('is1_13') == '2':
            self.score = 2
        elif self.input.get('is1_13') == '3':
            self.score = 3
        elif self.input.get('is1_13') == '4':
            self.score = 4
        return self.score

    def is_all_score(self):
        is1_1_score = self.is1_1()
        is1_2_score = self.is1_2()
        is1_3_score = self.is1_3()
        is1_4_score = self.is1_4()
        is1_5_score = self.is1_5()
        is1_6_score = self.is1_6()
        is1_7_score = self.is1_7()
        is1_8_score = self.is1_8()
        is1_9_score = self.is1_9()
        is1_10_score = self.is1_10()
        is1_11_score = self.is1_11()
        is1_12_score = self.is1_12()
        is1_13_score = self.is1_13()

        is_total_score = is1_1_score + is1_2_score + is1_3_score + is1_4_score + is1_5_score + is1_6_score + is1_7_score\
                         + is1_8_score + is1_9_score + is1_10_score + is1_11_score + is1_12_score + is1_13_score

        avg_score_ini = round((is_total_score/13), 2)
        return [is_total_score, avg_score_ini]


class AssessmentTotalscore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def as1_1(self):
        self.score = 0
        if self.input.get('as1_1') == '1':
            self.score = 1
        elif self.input.get('as1_1') == '2':
            self.score = 2
        elif self.input.get('as1_1') == '3':
            self.score = 3
        elif self.input.get('as1_1') == '4':
            self.score = 4
        return self.score

    def as1_2(self):
        self.score = 0
        if self.input.get('as1_2') == '1':
            self.score = 1
        elif self.input.get('as1_2') == '2':
            self.score = 2
        elif self.input.get('as1_2') == '3':
            self.score = 3
        elif self.input.get('as1_2') == '4':
            self.score = 4
        return self.score

    def as1_3(self):
        self.score = 0
        if self.input.get('as1_3') == '1':
            self.score = 1
        elif self.input.get('as1_3') == '2':
            self.score = 2
        elif self.input.get('as1_3') == '3':
            self.score = 3
        elif self.input.get('as1_3') == '4':
            self.score = 4
        return self.score

    def as1_4(self):
        self.score = 0
        if self.input.get('as1_4') == '1':
            self.score = 1
        elif self.input.get('as1_4') == '2':
            self.score = 2
        elif self.input.get('as1_4') == '3':
            self.score = 3
        elif self.input.get('as1_4') == '4':
            self.score = 4
        return self.score

    def as1_5(self):
        self.score = 0
        if self.input.get('as1_5') == '1':
            self.score = 1
        elif self.input.get('as1_5') == '2':
            self.score = 2
        elif self.input.get('as1_5') == '3':
            self.score = 3
        elif self.input.get('as1_5') == '4':
            self.score = 4
        return self.score

    def as1_6(self):
        self.score = 0
        if self.input.get('as1_6') == '1':
            self.score = 1
        elif self.input.get('as1_6') == '2':
            self.score = 2
        elif self.input.get('as1_6') == '3':
            self.score = 3
        elif self.input.get('as1_6') == '4':
            self.score = 4
        return self.score

    def as1_7(self):
        self.score = 0
        if self.input.get('as1_7') == '1':
            self.score = 1
        elif self.input.get('as1_7') == '2':
            self.score = 2
        elif self.input.get('as1_7') == '3':
            self.score = 3
        elif self.input.get('as1_7') == '4':
            self.score = 4
        return self.score

    def as1_8(self):
        self.score = 0
        if self.input.get('as1_8') == '1':
            self.score = 1
        elif self.input.get('as1_8') == '2':
            self.score = 2
        elif self.input.get('as1_8') == '3':
            self.score = 3
        elif self.input.get('as1_8') == '4':
            self.score = 4
        return self.score

    def as1_9(self):
        self.score = 0
        if self.input.get('as1_9') == '1':
            self.score = 1
        elif self.input.get('as1_9') == '2':
            self.score = 2
        elif self.input.get('as1_9') == '3':
            self.score = 3
        elif self.input.get('as1_9') == '4':
            self.score = 4
        return self.score

    def as1_10(self):
        self.score = 0
        if self.input.get('as1_10') == '1':
            self.score = 1
        elif self.input.get('as1_10') == '2':
            self.score = 2
        elif self.input.get('as1_10') == '3':
            self.score = 3
        elif self.input.get('as1_10') == '4':
            self.score = 4
        return self.score

    def as_all_score(self):
        as1_1_score = self.as1_1()
        as1_2_score = self.as1_2()
        as1_3_score = self.as1_3()
        as1_4_score = self.as1_4()
        as1_5_score = self.as1_5()
        as1_6_score = self.as1_6()
        as1_7_score = self.as1_7()
        as1_8_score = self.as1_8()
        as1_9_score = self.as1_9()
        as1_10_score = self.as1_10()

        as_total_score = as1_1_score + as1_2_score + as1_3_score + as1_4_score + as1_5_score + as1_6_score \
                         + as1_7_score + as1_8_score + as1_9_score + as1_10_score

        as_avg_score = round((as_total_score / 10), 2)
        return [as_total_score, as_avg_score]


class Customertotalscore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def cs1_1(self):
        self.score = 0
        if self.input.get('cs1_1') == '1':
            self.score = 1
        elif self.input.get('cs1_1') == '2':
            self.score = 2
        elif self.input.get('cs1_1') == '3':
            self.score = 3
        elif self.input.get('cs1_1') == '4':
            self.score = 4
        return self.score

    def cs1_2(self):
        self.score = 0
        if self.input.get('cs1_2') == '1':
            self.score = 1
        elif self.input.get('cs1_2') == '2':
            self.score = 2
        elif self.input.get('cs1_2') == '3':
            self.score = 3
        elif self.input.get('cs1_2') == '4':
            self.score = 4
        return self.score

    def cs1_3(self):
        self.score = 0
        if self.input.get('cs1_3') == '1':
            self.score = 1
        elif self.input.get('cs1_3') == '2':
            self.score = 2
        elif self.input.get('cs1_3') == '3':
            self.score = 3
        elif self.input.get('cs1_3') == '4':
            self.score = 4
        return self.score

    def cs1_4(self):
        self.score = 0
        if self.input.get('cs1_4') == '1':
            self.score = 1
        elif self.input.get('cs1_4') == '2':
            self.score = 2
        elif self.input.get('cs1_4') == '3':
            self.score = 3
        elif self.input.get('cs1_4') == '4':
            self.score = 4
        return self.score

    def cs1_5(self):
        self.score = 0
        if self.input.get('cs1_5') == '1':
            self.score = 1
        elif self.input.get('cs1_5') == '2':
            self.score = 2
        elif self.input.get('cs1_5') == '3':
            self.score = 3
        elif self.input.get('cs1_5') == '4':
            self.score = 4
        return self.score

    def cs1_6(self):
        self.score = 0
        if self.input.get('cs1_6') == '1':
            self.score = 1
        elif self.input.get('cs1_6') == '2':
            self.score = 2
        elif self.input.get('cs1_6') == '3':
            self.score = 3
        elif self.input.get('cs1_6') == '4':
            self.score = 4
        return self.score

    def cs1_7(self):
        self.score = 0
        if self.input.get('cs1_7') == '1':
            self.score = 1
        elif self.input.get('cs1_7') == '2':
            self.score = 2
        elif self.input.get('cs1_7') == '3':
            self.score = 3
        elif self.input.get('cs1_7') == '4':
            self.score = 4
        return self.score

    def cs1_8(self):
        self.score = 0
        if self.input.get('cs1_8') == '1':
            self.score = 1
        elif self.input.get('cs1_8') == '2':
            self.score = 2
        elif self.input.get('cs1_8') == '3':
            self.score = 3
        elif self.input.get('cs1_8') == '4':
            self.score = 4
        return self.score

    def cs1_9(self):
        self.score = 0
        if self.input.get('cs1_9') == '1':
            self.score = 1
        elif self.input.get('cs1_9') == '2':
            self.score = 2
        elif self.input.get('cs1_9') == '3':
            self.score = 3
        elif self.input.get('cs1_9') == '4':
            self.score = 4
        return self.score

    def cs1_10(self):
        self.score = 0
        if self.input.get('cs1_10') == '1':
            self.score = 1
        elif self.input.get('cs1_10') == '2':
            self.score = 2
        elif self.input.get('cs1_10') == '3':
            self.score = 3
        elif self.input.get('cs1_10') == '4':
            self.score = 4
        return self.score

    def cs1_11(self):
        self.score = 0
        if self.input.get('cs1_11') == '1':
            self.score = 1
        elif self.input.get('cs1_11') == '2':
            self.score = 2
        elif self.input.get('cs1_11') == '3':
            self.score = 3
        elif self.input.get('cs1_11') == '4':
            self.score = 4
        return self.score

    def cs_all_score(self):
        cs1_1_score = self.cs1_1()
        cs1_2_score = self.cs1_2()
        cs1_3_score = self.cs1_3()
        cs1_4_score = self.cs1_4()
        cs1_5_score = self.cs1_5()
        cs1_6_score = self.cs1_6()
        cs1_7_score = self.cs1_7()
        cs1_8_score = self.cs1_8()
        cs1_9_score = self.cs1_9()
        cs1_10_score = self.cs1_10()
        cs1_11_score = self.cs1_11()

        cs_total_score = cs1_1_score + cs1_2_score + cs1_3_score + cs1_4_score + cs1_5_score + cs1_6_score \
                         + cs1_7_score + cs1_8_score + cs1_9_score + cs1_10_score + cs1_11_score

        cs_avg_score = round((cs_total_score / 11), 2)
        return [cs_total_score, cs_avg_score]


class Kyctotalscore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def ks1_1(self):
        self.score = 0
        if self.input.get('ks1_1') == '1':
            self.score = 1
        elif self.input.get('ks1_1') == '2':
            self.score = 2
        elif self.input.get('ks1_1') == '3':
            self.score = 3
        elif self.input.get('ks1_1') == '4':
            self.score = 4
        return self.score

    def ks1_2(self):
        self.score = 0
        if self.input.get('ks1_2') == '1':
            self.score = 1
        elif self.input.get('ks1_2') == '2':
            self.score = 2
        elif self.input.get('ks1_2') == '3':
            self.score = 3
        elif self.input.get('ks1_2') == '4':
            self.score = 4
        return self.score

    def ks1_3(self):
        self.score = 0
        if self.input.get('ks1_3') == '1':
            self.score = 1
        elif self.input.get('ks1_3') == '2':
            self.score = 2
        elif self.input.get('ks1_3') == '3':
            self.score = 3
        elif self.input.get('ks1_3') == '4':
            self.score = 4
        return self.score

    def ks1_4(self):
        self.score = 0
        if self.input.get('ks1_4') == '1':
            self.score = 1
        elif self.input.get('ks1_4') == '2':
            self.score = 2
        elif self.input.get('ks1_4') == '3':
            self.score = 3
        elif self.input.get('ks1_4') == '4':
            self.score = 4
        return self.score

    def ks1_5(self):
        self.score = 0
        if self.input.get('ks1_5') == '1':
            self.score = 1
        elif self.input.get('ks1_5') == '2':
            self.score = 2
        elif self.input.get('ks1_5') == '3':
            self.score = 3
        elif self.input.get('ks1_5') == '4':
            self.score = 4
        return self.score

    def ks1_6(self):
        self.score = 0
        if self.input.get('ks1_6') == '1':
            self.score = 1
        elif self.input.get('ks1_6') == '2':
            self.score = 2
        elif self.input.get('ks1_6') == '3':
            self.score = 3
        elif self.input.get('ks1_6') == '4':
            self.score = 4
        return self.score

    def ks1_7(self):
        self.score = 0
        if self.input.get('ks1_7') == '1':
            self.score = 1
        elif self.input.get('ks1_7') == '2':
            self.score = 2
        elif self.input.get('ks1_7') == '3':
            self.score = 3
        elif self.input.get('ks1_7') == '4':
            self.score = 4
        return self.score

    def ks1_8(self):
        self.score = 0
        if self.input.get('ks1_8') == '1':
            self.score = 1
        elif self.input.get('ks1_8') == '2':
            self.score = 2
        elif self.input.get('ks1_8') == '3':
            self.score = 3
        elif self.input.get('ks1_8') == '4':
            self.score = 4
        return self.score

    def ks1_9(self):
        self.score = 0
        if self.input.get('ks1_9') == '1':
            self.score = 1
        elif self.input.get('ks1_9') == '2':
            self.score = 2
        elif self.input.get('ks1_9') == '3':
            self.score = 3
        elif self.input.get('ks1_9') == '4':
            self.score = 4
        return self.score

    def ks1_10(self):
        self.score = 0
        if self.input.get('ks1_10') == '1':
            self.score = 1
        elif self.input.get('ks1_10') == '2':
            self.score = 2
        elif self.input.get('ks1_10') == '3':
            self.score = 3
        elif self.input.get('ks1_10') == '4':
            self.score = 4
        return self.score

    def ks1_11(self):
        self.score = 0
        if self.input.get('ks1_11') == '1':
            self.score = 1
        elif self.input.get('ks1_11') == '2':
            self.score = 2
        elif self.input.get('ks1_11') == '3':
            self.score = 3
        elif self.input.get('ks1_11') == '4':
            self.score = 4
        return self.score

    def ks1_12(self):
        self.score = 0
        if self.input.get('ks1_12') == '1':
            self.score = 1
        elif self.input.get('ks1_12') == '2':
            self.score = 2
        elif self.input.get('ks1_12') == '3':
            self.score = 3
        elif self.input.get('ks1_12') == '4':
            self.score = 4
        return self.score

    def ks1_13(self):
        self.score = 0
        if self.input.get('ks1_13') == '1':
            self.score = 1
        elif self.input.get('ks1_13') == '2':
            self.score = 2
        elif self.input.get('ks1_13') == '3':
            self.score = 3
        elif self.input.get('ks1_13') == '4':
            self.score = 4
        return self.score

    def ks1_14(self):
        self.score = 0
        if self.input.get('ks1_14') == '1':
            self.score = 1
        elif self.input.get('ks1_14') == '2':
            self.score = 2
        elif self.input.get('ks1_14') == '3':
            self.score = 3
        elif self.input.get('ks1_14') == '4':
            self.score = 4
        return self.score

    def ks_all_score(self):
        ks1_1_score = self.ks1_1()
        ks1_2_score = self.ks1_2()
        ks1_3_score = self.ks1_3()
        ks1_4_score = self.ks1_4()
        ks1_5_score = self.ks1_5()
        ks1_6_score = self.ks1_6()
        ks1_7_score = self.ks1_7()
        ks1_8_score = self.ks1_8()
        ks1_9_score = self.ks1_9()
        ks1_10_score = self.ks1_10()
        ks1_11_score = self.ks1_11()
        ks1_12_score = self.ks1_12()
        ks1_13_score = self.ks1_13()
        ks1_14_score = self.ks1_14()

        ks_total_score = ks1_1_score + ks1_2_score + ks1_3_score + ks1_4_score + ks1_5_score + ks1_6_score \
                         + ks1_7_score + ks1_8_score + ks1_9_score + ks1_10_score + ks1_11_score \
                         + ks1_12_score + ks1_13_score + ks1_14_score

        ks_avg_score = round((ks_total_score / 14), 2)
        return [ks_total_score, ks_avg_score]


class Regulatorytotalscore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def rs1_1(self):
        self.score = 0
        if self.input.get('rs1_1') == '1':
            self.score = 1
        elif self.input.get('rs1_1') == '2':
            self.score = 2
        elif self.input.get('rs1_1') == '3':
            self.score = 3
        elif self.input.get('rs1_1') == '4':
            self.score = 4
        return self.score

    def rs1_2(self):
        self.score = 0
        if self.input.get('rs1_2') == '1':
            self.score = 1
        elif self.input.get('rs1_2') == '2':
            self.score = 2
        elif self.input.get('rs1_2') == '3':
            self.score = 3
        elif self.input.get('rs1_2') == '4':
            self.score = 4
        return self.score

    def rs1_3(self):
        self.score = 0
        if self.input.get('rs1_3') == '1':
            self.score = 1
        elif self.input.get('rs1_3') == '2':
            self.score = 2
        elif self.input.get('rs1_3') == '3':
            self.score = 3
        elif self.input.get('rs1_3') == '4':
            self.score = 4
        return self.score

    def rs1_4(self):
        self.score = 0
        if self.input.get('rs1_4') == '1':
            self.score = 1
        elif self.input.get('rs1_4') == '2':
            self.score = 2
        elif self.input.get('rs1_4') == '3':
            self.score = 3
        elif self.input.get('rs1_4') == '4':
            self.score = 4
        return self.score

    def rs1_5(self):
        self.score = 0
        if self.input.get('rs1_5') == '1':
            self.score = 1
        elif self.input.get('rs1_5') == '2':
            self.score = 2
        elif self.input.get('rs1_5') == '3':
            self.score = 3
        elif self.input.get('rs1_5') == '4':
            self.score = 4
        return self.score

    def rs1_6(self):
        self.score = 0
        if self.input.get('rs1_6') == '1':
            self.score = 1
        elif self.input.get('rs1_6') == '2':
            self.score = 2
        elif self.input.get('rs1_6') == '3':
            self.score = 3
        elif self.input.get('rs1_6') == '4':
            self.score = 4
        return self.score

    def rs1_7(self):
        self.score = 0
        if self.input.get('rs1_7') == '1':
            self.score = 1
        elif self.input.get('rs1_7') == '2':
            self.score = 2
        elif self.input.get('rs1_7') == '3':
            self.score = 3
        elif self.input.get('rs1_7') == '4':
            self.score = 4
        return self.score

    def rs1_8(self):
        self.score = 0
        if self.input.get('rs1_8') == '1':
            self.score = 1
        elif self.input.get('rs1_8') == '2':
            self.score = 2
        elif self.input.get('rs1_8') == '3':
            self.score = 3
        elif self.input.get('rs1_8') == '4':
            self.score = 4
        return self.score

    def rs1_9(self):
        self.score = 0
        if self.input.get('rs1_9') == '1':
            self.score = 1
        elif self.input.get('rs1_9') == '2':
            self.score = 2
        elif self.input.get('rs1_9') == '3':
            self.score = 3
        elif self.input.get('rs1_9') == '4':
            self.score = 4
        return self.score

    def rs1_10(self):
        self.score = 0
        if self.input.get('rs1_10') == '1':
            self.score = 1
        elif self.input.get('rs1_10') == '2':
            self.score = 2
        elif self.input.get('rs1_10') == '3':
            self.score = 3
        elif self.input.get('rs1_10') == '4':
            self.score = 4
        return self.score

    def rs1_11(self):
        self.score = 0
        if self.input.get('rs1_11') == '1':
            self.score = 1
        elif self.input.get('rs1_11') == '2':
            self.score = 2
        elif self.input.get('rs1_11') == '3':
            self.score = 3
        elif self.input.get('rs1_11') == '4':
            self.score = 4
        return self.score

    def rs1_12(self):
        self.score = 0
        if self.input.get('rs1_12') == '1':
            self.score = 1
        elif self.input.get('rs1_12') == '2':
            self.score = 2
        elif self.input.get('rs1_12') == '3':
            self.score = 3
        elif self.input.get('rs1_12') == '4':
            self.score = 4
        return self.score

    def rs1_13(self):
        self.score = 0
        if self.input.get('rs1_13') == '1':
            self.score = 1
        elif self.input.get('rs1_13') == '2':
            self.score = 2
        elif self.input.get('rs1_13') == '3':
            self.score = 3
        elif self.input.get('rs1_13') == '4':
            self.score = 4
        return self.score

    def rs1_14(self):
        self.score = 0
        if self.input.get('rs1_14') == '1':
            self.score = 1
        elif self.input.get('rs1_14') == '2':
            self.score = 2
        elif self.input.get('rs1_14') == '3':
            self.score = 3
        elif self.input.get('rs1_14') == '4':
            self.score = 4
        return self.score

    def rs_all_score(self):
        rs1_1_score = self.rs1_1()
        rs1_2_score = self.rs1_2()
        rs1_3_score = self.rs1_3()
        rs1_4_score = self.rs1_4()
        rs1_5_score = self.rs1_5()
        rs1_6_score = self.rs1_5()
        rs1_7_score = self.rs1_6()
        rs1_8_score = self.rs1_7()
        rs1_9_score = self.rs1_8()
        rs1_10_score = self.rs1_9()
        rs1_11_score = self.rs1_10()
        rs1_12_score = self.rs1_11()
        rs1_13_score = self.rs1_11()
        rs1_14_score = self.rs1_11()

        rs_total_score = rs1_1_score + rs1_2_score + rs1_3_score + rs1_4_score + rs1_5_score \
                         + rs1_6_score + rs1_7_score + rs1_8_score + rs1_9_score + rs1_10_score \
                         + rs1_11_score + rs1_12_score + rs1_13_score + rs1_14_score

        rs_avg_score = round((rs_total_score/14), 2)
        return [rs_total_score, rs_avg_score]


def final_score(request):
    return render(request, 'final_score.html')


def temp(request):
    return render(request, 'temp.html')
