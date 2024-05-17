from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .assessments.ned_form import NedAssessmentForm
from .assessments.vak_form import VAKAssessmentForm
from .assessments.ned_model import NedAssessment
from .assessments.vak_model import VAKAssessment
from .decorators import redirect_authenticate
from .forms import StudentSignUpForm, StudentSignInForm


@redirect_authenticate
def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, 'users.backends.EmailBackend')
            return redirect('userpage')
        return render(request, 'signup.html', {'form': form})
    else:
        form = StudentSignUpForm()

    return render(request, 'signup.html', {'form': form})


@redirect_authenticate
def signin(request):
    if request.method == 'POST':
        form = StudentSignInForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user, 'users.backends.EmailBackend')
            return redirect('userpage')
        return render(request, 'signin.html', {'form': form})
    else:
        form = StudentSignInForm()

    return render(request, 'signin.html', {'form': form})


@login_required
def userpage(request):
    return render(request, 'userpage.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def ned_assessment(request):
    if request.method == 'POST':
        profile = request.user.student_profile
        form = NedAssessmentForm(request.POST, profile=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Avaliação Ned realizada com sucesso!')
            return redirect('userpage')
        return render(request, 'assessment.html', {'form': form})
    else:
        form = NedAssessmentForm()
    
    return render(request, 'assessment.html', {'form': form, 'post_url': 'ned_assessment'})


@login_required
def vak_assessment(request):
    if request.method == 'POST':
        profile = request.user.student_profile
        form = VAKAssessmentForm(request.POST, profile=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Avaliação ACV realizada com sucesso!')
            return redirect('userpage')
        return render(request, 'assessment.html', {'form': form})
    else:
        form = VAKAssessmentForm()
    
    return render(request, 'assessment.html', {'form': form, 'post_url': 'vak_assessment'})


@login_required
def assessments_history(request):
    profile = request.user.student_profile
    ned_assessments = list(NedAssessment.objects.filter(ned_profile=profile))
    vak_assessments = list(VAKAssessment.objects.filter(vak_profile=profile))
    ned_assessments.reverse()
    vak_assessments.reverse()
    context = {'ned_assessments': ned_assessments, 'vak_assessments': vak_assessments}
    return render(request, 'assessments_history.html', context)


@login_required
def assessment_result(request):
    if request.method == 'POST':
        form = request.POST
        assessment_type = form.get('assessmentType')

        if assessment_type == 'ned':
            assessment_id = form.get('assessmentId')
            assessment = NedAssessment.objects.get(id=assessment_id)
            context = {
                'assessment_type': assessment_type,
                'result': {
                    'eagle': assessment.resultado_aguia(),
                    'cat': assessment.resultado_gato(),
                    'wolf': assessment.resultado_lobo(),
                    'shark': assessment.resultado_tubarao(),
                }
            }
        
        elif assessment_type == 'vak':
            assessment_id = form.get('assessmentId')
            assessment = VAKAssessment.objects.get(id=assessment_id)
            totalScore = assessment.pontos_auditivo() + assessment.pontos_visual() + assessment.pontos_cinestesico()
            context = {
                'assessment_type': assessment_type,
                'result': {
                    'auditory': assessment.pontos_auditivo(),
                    'visual': assessment.pontos_visual(),
                    'kinesthetic': assessment.pontos_cinestesico(),
                    'totalScore': totalScore,
                }
            }
    
    return render(request, 'assessment_result.html', context)
