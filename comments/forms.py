from django import forms


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    content = forms.CharField(label='Comment', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 10,
        "resize": "None"
    }))
