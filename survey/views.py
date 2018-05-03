import json
import pprint

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from survey.models import ResponsesBeta


def save_survey():
    import json
    import pprint
    import openpyxl
    from openpyxl import Workbook

    renaming = {
        'To what degree do you see the following factors as opportunities within digitalisation for you as a CFO? (Rate 1 - 5)': 'CFO digitalisation opportunities',
    }

    questions_to_text = {
        'question5': 'To what degree do you see digitalisation as an opportunity to increase value creation on the following areas?',
        'question2': "To what degree are the following factors challenging for you in terms of regulatory compliance? (Rate 1 - 5) ",
        "question1": "To what degree are the following factors challenging for you in terms of governance & stakeholder management? (Rate 1 - 5) ",
        'strategy': "To what degree are the following factors challenging for you in terms of strategy? (Rate 1 - 5) ",
        "question3": "To what degree are the following factors challenging for you in terms of value creation? (Rate 1 - 5) ",
        "Risk management": "To what degree are the following factors challenging for you in terms of risk management? (Rate 1 - 5) ",
        "question5": "To what degree do you see digitalisation as an opportunity to increase value creation on the following areas? (Rate 1 - 5)",
        "question6": "To what degree do you believe the following cultural factors are challenges to effective digitalisation?",
        "question7": "To what degree do you believe the following aspects are challenges to effective digitalisation?",
    }

    wb = Workbook()
    ws = wb.active

    count = 1
    with open("survey_answers", 'w') as survey_answers:
        for respondee in ResponsesBeta.objects.all():
            json_data = json.loads(respondee.data.get('survey_response'))
            survey_answers.write("START RESPONSE {}: \n".format(count))

            for question in json_data:
                if question == 'priorities':
                    response = json_data.get(question)
                    ws.append(['Priorities'])
                    ws.append(response)
                    ws.append([])
                    continue
                responses = json_data.get(question)
                question = questions_to_text.get(question) if questions_to_text.get(question) is not None else question
                ws.append([question])
                if type(responses) == dict:
                    responses = list(responses.items())
                    if question == 'Technology - opportunity and maturity':
                        ws.append(['','Degree of Maturity', 'Degree of Opportunity'])
                        for response in responses:
                            topic = response[0]
                            maturity = response[1].get('Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.')
                            if not maturity:
                                maturity = 0
                            if not maturity == 'N/A':
                                maturity = int(maturity)

                            opportunity = response[1].get('Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.')
                            if not opportunity:
                                opportunity = 0

                            if not opportunity == 'N/A':
                                opportunity = int(opportunity)
                            ws.append([topic, maturity, opportunity])
                    else:
                        pprint.pprint(responses)
                        for response in responses:
                            topic = response[0]
                            rating = int(response[1][0]) if response[1][0].isdigit() else 'N/A'
                            ws.append([topic, rating])

                else:
                    ws.append([responses])
                ws.append([])
            ws.append([])
            ws.append([])
    wb.save("sample.xlsx")


# Create your views here.
class SurveyTemplateView(TemplateView):
    template_name = "survey/survey_landing.html"

class SurveyAboutView(TemplateView):
    template_name = "survey/survey_about.html"

class SurveyQuestionsView(TemplateView):
    template_name = "survey/survey_questions.html"

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        return super(SurveyQuestionsView, self).get(request, *args, **kwargs)

def survey_ajax_submit(request):
    if request.is_ajax():
        json_data = json.dumps(request.POST)
        json_loaded = json.loads(json_data)
        ResponsesBeta.objects.create(data=json_loaded)
        return JsonResponse(request.POST)
