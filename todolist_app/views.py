# todolist_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    """
    Vue pour afficher la liste de toutes les tâches.
    """
    tasks = Task.objects.all().order_by('-created_at')
    
    # ---- Ligne de débogage pour vérifier si la vue est appelée et si les tâches sont trouvées ----
    print("--- Vue 'task_list' exécutée ---")
    print("Nombre de tâches trouvées en base :", tasks.count()) 
    print("Tâches:", tasks)
    # ------------------------------------------------------------------------------------

    return render(request, 'todolist_app/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    """
    Vue pour afficher les détails d'une seule tâche.
    Le 'pk' est la clé primaire (ID) de la tâche.
    """
    task = get_object_or_404(Task, pk=pk)
    
    # ---- Ligne de débogage ----
    print(f"--- Vue 'task_detail' exécutée pour la tâche ID {pk} : {task.title} ---")
    # --------------------------

    return render(request, 'todolist_app/task_detail.html', {'task': task})

def task_create(request):
    """
    Vue pour créer une nouvelle tâche.
    Gère à la fois l'affichage du formulaire (GET) et sa soumission (POST).
    """
    if request.method == 'POST':
        print("--- Vue 'task_create' : Méthode POST détectée ---")
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title: # S'assurer qu'au moins un titre est fourni
            Task.objects.create(title=title, description=description)
            print(f"Tâche '{title}' créée avec succès.")
        else:
            print("Tentative de création de tâche sans titre.")

        return redirect('task_list') # Redirige vers la liste des tâches après création
    
    # Si la méthode n'est pas POST, on affiche juste la page
    print("--- Vue 'task_create' : Méthode GET, affichage du formulaire ---")
    return render(request, 'todolist_app/task_create.html')
