from django.shortcuts import render, get_object_or_404 , redirect
from django.utils import timezone

from .models import Consulta
from .forms import ConsultaForm


# Create your views here.

def consulta_list (request):
	# colocar os filtros para mostrar da maneira que queremos
	consultas = Consulta.objects.filter(published_date__lte=timezone.now()).order_by('name')
	return render (request, 'desafio/consulta_list.html' , {})

def more_details(request,pk):
	consulta = get_objects_or_404(Consulta, pk = pk)
	return render (request, 'desafio/more_details.html', {'consulta' : consulta})


def consulta_new(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ConsultaForm()
    return render(request, 'desafio/consulta_edit.html', {'form': form})