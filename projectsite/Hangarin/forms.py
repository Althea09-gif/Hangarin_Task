from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-input"})
    )

    class Meta:
        model = Task
        fields = ["title", "description", "deadline", "status", "category", "priority"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Enter task title"
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-input form-textarea",
            "placeholder": "Enter task description"
        })
        self.fields["status"].widget.attrs.update({
            "class": "form-input"
        })
        self.fields["category"].widget.attrs.update({
            "class": "form-input"
        })
        self.fields["priority"].widget.attrs.update({
            "class": "form-input"
        })