from django.shortcuts import render , get_object_or_404
from .models import Choice

from django.http import HttpResponse , HttpResponseRedirect

from django.urls import reverse

#vamos a importar el modelo
from .models import Question

#vistas basadas en clases
from django.views import generic 





# Create your views here.

""" 


def index(request):
    latest_question_list= Question.objects.all()
    #Con el render yo le estoy pasando al template el el diccionarioo con los datos 
    #que hay en la variable latest_question_list
    return render(
        request,
        "polls/index.html",
        {"latest_question_list":latest_question_list}
        )
"""

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]#- pues ordena desde las mas nuevas hasta las mas viejas





def detail(request,question_id):
    #si encuenrta la question_id lo almacena en pk en caso contrario lanza el error 404
    question=get_object_or_404(Question,pk=question_id)
    return render(
        request,
        "polls/detail.html",
        {"question":question} 
        )



""" 
class DetailView(generic.DetailView):
   model=Question
   template_name="polls/detail.html"

class ResultsView(generic.DetailView):
   model=Question
   template_name="polls/results.html"

"""


def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "polls/results.html",
        {"question":question}
    )
    #return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")



def vote(request,question_id):
    #nos va llegar el name y id de la respuesta elegida


    question = get_object_or_404(Question , pk=question_id) 
    #pues vamos a intentar obtener la respuesta del usuario
    try : 
        #vamos a usar el request pues eso es lo ques estamos recibiendo del post
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError ,  Choice.DoesNotExist):
       return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"No elegiste una respuesta"
            }
        )
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #con el HttpResponseRedirect me aseguro que el usuario no envie dos veces el formulario 
        #                                    "app_name:name"  args son los argumentos de la url que esta en url en este caso la question.id 

        return HttpResponseRedirect(reverse("polls:results" , args=[(question.id)]))



    #question = Question.objects.get(pk=question_id) 

   

  








