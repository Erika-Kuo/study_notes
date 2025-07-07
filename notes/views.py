from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, Note
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import NoteForm

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

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {
    'note': note,
    'subject': note.subject 
})

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:home')
