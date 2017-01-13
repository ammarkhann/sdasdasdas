from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

from newsletter.forms import ContactForm, SignUpForm
from newsletter.models import SignUp
from django.shortcuts import render, get_object_or_404,redirect
from questions.models import Question,UserAnswer,UserTextAnswer
# Create your views here.
def home(request):
	
	if request.user.is_authenticated():

		new_user = False
	
		
		

		


		context = {
			"new_user": new_user,
		}
		
		return render(request, "dashboard/home.html", context)

	context = {
		
	}


	return render(request, "home.html", context)


def result(request):
	queryset = Question.objects.get_unanswered(request.user).order_by('-timestamp')	

	if queryset.count() == 0:
		multiple_choice_score = 0
		text_score = 0

		user_answer = UserAnswer.objects.filter(user=request.user)
		user_text_answer = UserTextAnswer.objects.filter(user=request.user)

		for obj in user_answer:
			multiple_choice_score += obj.my_points

		for obj in user_text_answer:
			text_score += obj.my_points

		temp_user_score = (multiple_choice_score + text_score)/ (user_answer.count() + user_text_answer.count())
		print temp_user_score

		
	else:
		print messages.error(request, 'Please answer all the questions first.')
		return redirect("home")

	context = {

	"temp_user_score": temp_user_score,
	}



	return render(request,"dashboard/result.html", context)


















