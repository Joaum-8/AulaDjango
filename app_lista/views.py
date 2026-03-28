from django.shortcuts import render, redirect, get_object_or_404
from .models import lista

def lista_listas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')

        if titulo:
            lista.objects.create(titulo=titulo)

        return redirect('home')

    minhas_listas = lista.objects.filter(deletada=False)

    return render(request, 'app_lista/app_lista.html', {'listas': minhas_listas})


def concluir_tarefa(request, id):
    tarefa = get_object_or_404(lista, id=id)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('home')


def deletar_tarefa(request, id):
    tarefa = get_object_or_404(lista, id=id)
    tarefa.deletada = True
    tarefa.save()
    return redirect('home')


def lixeira(request):
    tarefas = lista.objects.filter(deletada=True)
    return render(request, 'app_lista/lixeira.html', {'listas': tarefas})


def editar_tarefa(request, id):
    tarefa = get_object_or_404(lista, id=id)

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.save()
        return redirect('home')

    return render(request, 'app_lista/editar.html', {'tarefa': tarefa})