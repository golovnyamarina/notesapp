from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/list.html', {'notes': notes})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/delete.html', {'note': note})
