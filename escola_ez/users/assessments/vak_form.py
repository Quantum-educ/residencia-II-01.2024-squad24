from django import forms
from .vak_model import VAKAssessment


class VAKAssessmentForm(forms.ModelForm):
    class Meta:
        model = VAKAssessment
        fields = '__all__'
        widgets = {
            'question_01': forms.RadioSelect(choices=VAKAssessment.question_01.field.choices),
            'question_02': forms.RadioSelect(choices=VAKAssessment.question_02.field.choices),
            'question_03': forms.RadioSelect(choices=VAKAssessment.question_03.field.choices),
            'question_04': forms.RadioSelect(choices=VAKAssessment.question_04.field.choices),
            'question_05': forms.RadioSelect(choices=VAKAssessment.question_05.field.choices),
            'question_06': forms.RadioSelect(choices=VAKAssessment.question_06.field.choices),
            'question_07': forms.RadioSelect(choices=VAKAssessment.question_07.field.choices),
            'question_08': forms.RadioSelect(choices=VAKAssessment.question_08.field.choices),
            'question_09': forms.RadioSelect(choices=VAKAssessment.question_09.field.choices),
            'question_10': forms.RadioSelect(choices=VAKAssessment.question_10.field.choices),
            'question_11': forms.RadioSelect(choices=VAKAssessment.question_11.field.choices),
            'question_12': forms.RadioSelect(choices=VAKAssessment.question_12.field.choices),
            'question_13': forms.RadioSelect(choices=VAKAssessment.question_13.field.choices),
            'question_14': forms.RadioSelect(choices=VAKAssessment.question_14.field.choices),
            'question_15': forms.RadioSelect(choices=VAKAssessment.question_15.field.choices),
            'question_16': forms.RadioSelect(choices=VAKAssessment.question_16.field.choices),
            'question_17': forms.RadioSelect(choices=VAKAssessment.question_17.field.choices),
            'question_18': forms.RadioSelect(choices=VAKAssessment.question_18.field.choices),
            'question_19': forms.RadioSelect(choices=VAKAssessment.question_19.field.choices),
            'question_20': forms.RadioSelect(choices=VAKAssessment.question_20.field.choices),
            'question_21': forms.RadioSelect(choices=VAKAssessment.question_21.field.choices),
            'question_22': forms.RadioSelect(choices=VAKAssessment.question_22.field.choices),
            'question_23': forms.RadioSelect(choices=VAKAssessment.question_23.field.choices),
            'question_24': forms.RadioSelect(choices=VAKAssessment.question_24.field.choices),
            'question_25': forms.RadioSelect(choices=VAKAssessment.question_25.field.choices),
            'question_26': forms.RadioSelect(choices=VAKAssessment.question_26.field.choices),
            'question_27': forms.RadioSelect(choices=VAKAssessment.question_27.field.choices),
            'question_28': forms.RadioSelect(choices=VAKAssessment.question_28.field.choices),
            'question_29': forms.RadioSelect(choices=VAKAssessment.question_29.field.choices),
            'question_30': forms.RadioSelect(choices=VAKAssessment.question_30.field.choices),
        }
