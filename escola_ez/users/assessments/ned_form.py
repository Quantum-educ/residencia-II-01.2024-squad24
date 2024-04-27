from django import forms
from .ned_model import NedAssessment


class NedAssessmentForm(forms.ModelForm):
    
    class Meta:
        model = NedAssessment
        fields = '__all__'
        widgets = {
            'question_01': forms.RadioSelect(choices=NedAssessment.question_01.field.choices),
            'question_02': forms.RadioSelect(choices=NedAssessment.question_02.field.choices),
            'question_03': forms.RadioSelect(choices=NedAssessment.question_03.field.choices),
            'question_04': forms.RadioSelect(choices=NedAssessment.question_04.field.choices),
            'question_05': forms.RadioSelect(choices=NedAssessment.question_05.field.choices),
            'question_06': forms.RadioSelect(choices=NedAssessment.question_06.field.choices),
            'question_07': forms.RadioSelect(choices=NedAssessment.question_07.field.choices),
            'question_08': forms.RadioSelect(choices=NedAssessment.question_08.field.choices),
            'question_09': forms.RadioSelect(choices=NedAssessment.question_09.field.choices),
            'question_10': forms.RadioSelect(choices=NedAssessment.question_10.field.choices),
            'question_11': forms.RadioSelect(choices=NedAssessment.question_11.field.choices),
            'question_12': forms.RadioSelect(choices=NedAssessment.question_12.field.choices),
            'question_13': forms.RadioSelect(choices=NedAssessment.question_13.field.choices),
            'question_14': forms.RadioSelect(choices=NedAssessment.question_14.field.choices),
            'question_15': forms.RadioSelect(choices=NedAssessment.question_15.field.choices),
            'question_16': forms.RadioSelect(choices=NedAssessment.question_16.field.choices),
            'question_17': forms.RadioSelect(choices=NedAssessment.question_17.field.choices),
            'question_18': forms.RadioSelect(choices=NedAssessment.question_18.field.choices),
            'question_19': forms.RadioSelect(choices=NedAssessment.question_19.field.choices),
            'question_20': forms.RadioSelect(choices=NedAssessment.question_20.field.choices),
            'question_21': forms.RadioSelect(choices=NedAssessment.question_21.field.choices),
            'question_22': forms.RadioSelect(choices=NedAssessment.question_22.field.choices),
            'question_23': forms.RadioSelect(choices=NedAssessment.question_23.field.choices),
            'question_24': forms.RadioSelect(choices=NedAssessment.question_24.field.choices),
            'question_25': forms.RadioSelect(choices=NedAssessment.question_25.field.choices),
        }
