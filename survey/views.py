import json

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from survey.models import ResponsesBeta

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

def save_survey():
    import json
    import pprint
    import openpyxl

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

    wb = openpyxl.Workbook()
    ws = wb.active

    #json_data = """{"priorities":["Regulatory Compliance","Strategy","Cost Management and Efficiency"],"question2":{"Adopting regulation in business processes ":"3 - A challenge","Adopting regulation in systems & technology ":"2 - A minor challenge","Adopting regulation in the organisation":"1 - Not a challenge","Turning regulation into an advantage":"4 - A considerable challenge","Turning regulation into innovation":"5 - A major challenge"},"Technology - opportunity and maturity":{"Cybersecurity":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"Robotics":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"Data & Analytics":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"Cloud Computing":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"AI & Machine Learning":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"Blockchain":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"Digital Assistants (chat/voice)":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"Internet of Things (sensor/devices)":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"},"Augmented & Virtual Reality":{"Degree of Maturity. 1 = Not mature for implementation, 5 = mature for implementation.":"1","Degree of Opportunity. 1 = Not considered an opportunity, 5 = major opportunity.":"1"}},"To what degree do you see the following factors as opportunities within digitalisation for you as a CFO? (Rate 1 - 5) ":{"Administration processes":"1 - Not an opportunity","Shorter lead time":"1 - Not an opportunity","Improved quality and consistency":"1 - Not an opportunity","Higher regulative agility":"1 - Not an opportunity","Effective customer interface":"1 - Not an opportunity","Procurement to pay":"1 - Not an opportunity","Order to cash":"1 - Not an opportunity","Record to report":"1 - Not an opportunity"},"question5":{"New offerings":"1 - Not an opportunity","Stronger customer interaction":"1 - Not an opportunity","Data Driven decision making":"1 - Not an opportunity","Disrupt competition":"1 - Not an opportunity","Improved brand image":"1 - Not an opportunity"},"question7":{"Maturity of new technology":"1 - Not a challenge","Analog/manual processes":"1 - Not a challenge","Implementation costs":"1 - Not a challenge","Digital debt & IT legacy ":"1 - Not a challenge"},"question6":{"CXO level of digital capabilities":"1 - Not a challenge","Fear of redundancy ":"1 - Not a challenge","Employee digital skills":"1 - Not a challenge","Adaptability to change":"1 - Not a challenge","Organisation and governance":"1 - Not a challenge"}}"""

    #json_data = json.loads(json_data)
    count = 1
    with open("survey_answers", 'w') as survey_answers:
        for respondee in ResponsesBeta.objects.all():
            json_data = json.loads(respondee.data.get('survey_response'))
            survey_answers.write("START RESPONSE {}: \n".format(count))

            for question in json_data:
                responses = json_data.get(question)
                question = questions_to_text.get(question) if questions_to_text.get(question) is not None else question

                output = pprint.pformat(responses)
                survey_answers.write('\n' + question.upper() + '\n')
                survey_answers.write(output.replace('{', '').replace('}', '') + '\n')
            survey_answers.write('\nEND RESPONSE {count} \n\n\n\n'.format(count=count))
            count += 1


