from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

education_list = ['education','study','studied','qualification','qualifications']
education_response = "Vinod is a Final Year Computer Engineering Student, currently studying at "\
                    "Pune Vidyarthi Griha's College of Engineering and Technology. He has a CGPA "\
                        "of 8.51. \n\nHe completed his HSC (Science) in 2017 from Rajiv Gandhi "\
                            "College with 77.08%. \n\nHe completed his SSC from Modern "\
                                "Highschool in 2015 with 86.2%."

experience_list = ['experience','internship','internships','work', 'intern']
experience_response = "Vinod has done 2 major internships throughout his engineering.\n\n"\
                        "The first one was as Android Development Intern at The Sparks Foundation."\
                            " The duration of internship was from April 2019 till June 2019."\
                                " Vinod devised more than 5 android application using XML, Java and Django"\
                                    " as a part of the internship.\n\n"\
                                "The second internship was as Data Science intern at Sapio Analytics."\
                                    " Vinod worked on Projects for State Govevernments as a part of this"\
                                        " internship. He also learnt about NLP, Data Visualization during"\
                                            " this internship. The duration of the internship was from"\
                                                " May 2020 - August 2020"
                                    

achievements_list = ['achievement','achievements', 'awards','honours','honors','award','honor']
achievements_repsonse = "Achievements -\n\n1.Winner of Smart India Hackathon 2020\n"\
                        "2. Winner of Principal Global Hackathon\n"\
                            "3. Winner of Alacrity Hackathon\n"\
                                "4. First Position at ​ Collegiate Coding Competition\n"\
                                    "5. Led team to the Finals of Walchand Hackathonn\n"\
                                        "6. Finalist at IBM Hackathon - Cummins College"

projects_list = ['projects', 'project']
projects_response = "Vinod is currently working on his BE Project which is Sensor Fusion for"\
                        " autonomous vehicle. The project is sponsored by ARAI. Apart from that"\
                            " he has developed several other projects such as - \n\n"\
                                "1. Portfolio Rebalancing of Mutual Funds ​ (Sponsored and Awarded by Principal Global Services)\n"\
                                    "2. Calculating safe speed limit for driver ​ (Awarded first prize by ​ Automotive Research Association of India ​ )​\n"\
                                        "3. Township Management Android Application ​ (Winning Project at Alacrity Hackathon 2020)\n"\
                                            "You can view all his projects at - https://github.com/vk2607 "

skills_list = ['skill', 'skills']
skills_response = 'Vinod has technical skills such as - \n\n'\
                    "Programming Languages: ​ Python, Java, C++, C\n"\
                        "Databases: ​ MYSQL, NoSQL\n"\
                            "Domains: ​ Machine Learning, Data Science, Android\n"\
                                "Tools: ​ Git, AWS, MS Excel, Tableau, Google Colab\n"\
                                    "Libraries: ​ matplotlib, seaborn, beautiful soup, Tensorflow\n"\
                                        "Web Developmen​t: HTML, CSS, JavaScript, Django.\n\n"\
                                            "Apart from these, he has also been a part of clubs and committees in his colleges"\
                                                " which have helped him to develop soft skills such as teamwork, leadership,"\
                                                    " public speaking, management, etc."

cocurricular_list = ['co-curriculars','curricular', 'curriculars','co-curriculars']
cocurricular_response = 'Vinod believes that all-round development is extremely important to'\
                        " be successfull in life. He has managed to learn things whenever an opportunity was presented.\n\n"\
                            "He is the General Secretary of Association of Computer Engineering Students (ACES). He was previously"\
                                " in Web Development and Sponsorship Team in ACES.\n\n"\
                                    "He is also a Project Management Head and a Podcaster at Developer Students Club PVGCOET.\n"\
                                        "He was the team member of Robocon PVGCOET 2020.\n\n"\
                                            "Vinod has a working proficency in English, Japanese, Marathi, Hindi.\n"\
                                                "He loves to cycle, go on a trek, read some poetry, and occassionally tries his hand at flute too."

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
        return HttpResponse("Hi, This is Vinod's ResumeBot!.\nI can tell you about Vinod's education, experience, achievement's, projects, skills and co-curriculars.\nYou can know more about Vinod by visiting - https://www.linkedin.com/in/vinodkamat2607/ ")
    
    elif search(education_list,message):
        return HttpResponse(education_response)

    elif search(experience_list,message):
        return HttpResponse(experience_response)

    elif search(achievements_list,message):
        return HttpResponse(achievements_repsonse)
    
    elif search(projects_list, message):
        return HttpResponse(projects_response)

    elif search(skills_list,message):
        return HttpResponse(skills_response)

    elif search(cocurricular_list, message):
        return HttpResponse(cocurricular_response)

    return HttpResponse("Sorry, I didn't understand. Can you please ask again? I can tell you about Vinod's education, experience, achievement's, projects, skills and co-curriculars")

def search(search_list, message):
    for word in search_list:
        if word in message:
            return True
    return False