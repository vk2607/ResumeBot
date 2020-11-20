from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

education_response = "Vinod is a Final Year Computer Engineering Student, currently studying at "\
                    "Pune Vidyarthi Griha's College of Engineering and Technology. He has a CGPA "\
                        "of 8.51. \n. He completed his HSC (Science) in 2017 from Rajiv Gandhi "\
                            "College with 77.08%. \n He completed his SSC in 2015 from Modern "\
                                "Highschool in 2015 with 86.2%."

@csrf_exempt
def index(request):
    req_dict = request.body
    req_dict = req_dict.decode('utf-8')
    try:
	    request_json = json.loads(req_dict)
    except Exception as e:
	    print(e)
    message = request_json['payload']['payload']['text']
    message = message.lower()

    if (message == 'hi' or message == 'hello'):
        return HttpResponse("Hi, This is Vinod's ResumeBot!")
    
    elif 'education' in message:
        return HttpResponse(education_response)


    return HttpResponse("Sorry, I didn't understand. Can you please tell again?")
