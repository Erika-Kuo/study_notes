from notes.models import Subject

def subjects_processor(request):
    # Only include main subjects (no parent)
    return {
        'subjects': Subject.objects.filter(parent__isnull=True).prefetch_related('subsubjects')
    }
