from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, Note
from django.urls import reverse
from django.views.decorators.http import require_http_methods

def home(request):
    subjects = Subject.objects.filter(parent__isnull=True).prefetch_related('subsubjects', 'notes')
    return render(request, 'notes/home.html', {'subjects': subjects})

@require_http_methods(["GET", "POST"])
def create_note(request, subject_id=None):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        subject = get_object_or_404(Subject, id=subject_id) if subject_id else None
        if title and content and subject:
            Note.objects.create(title=title, content=content, subject=subject)
            return redirect(reverse('notes:home'))
        else:
            error = "All fields are required."
            return render(request, 'notes/note_form.html', {'error': error, 'subject_id': subject_id})
    else:
        return render(request, 'notes/note_form.html', {'subject_id': subject_id})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject.objects.prefetch_related('subsubjects', 'notes'), id=subject_id)
    return render(request, 'notes/subject_detail.html', {'subject': subject})
