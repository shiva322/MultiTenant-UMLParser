from django import forms
from models import Scores,Tenant
from django.utils.translation import ugettext_lazy as _

class ScoresForm(forms.ModelForm):
    class Meta:
        model=Scores
        fields = ['score_attribute1','score_attribute2','score_attribute3','score_attribute4']
        labels = {
            'score_attribute1': _('Comments'),
            'score_attribute2':_('Complete'),
            'score_attribute3':_('Score'),
            'score_attribute4':_('Grade'),
        }

        widgets = {
            'score_attribute1': forms.Textarea(attrs={'cols': 30, 'rows': 8}),
            'score_attribute2': forms.CheckboxInput(attrs=None),
            'score_attribute3': forms.NumberInput(attrs={'min': '0', 'max': '10'}),
            'score_attribute4': forms.Select(choices=Scores.GRADE_OPTIONS)
        }



    