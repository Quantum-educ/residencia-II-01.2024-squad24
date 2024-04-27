function addSubmitEvents() {
    const form = document.getElementById('form');
    const assessments = document.getElementsByClassName('assessment');
    for (let assessment of assessments) {
        assessment.addEventListener('click', event => {
            cleanForm(assessment)
            form.submit()
        });
    }
}


function cleanForm(assessment) {
    const inputs = Array.from(document.getElementsByTagName('input'));
    const assessmentChildren = Array.from(assessment.children);
    const assessmentInputs = assessmentChildren.filter(element => element.tagName == 'INPUT');
    const inputsToRemove = inputs.filter(input => !assessmentInputs.includes(input)).slice(1);
    inputsToRemove.forEach(input => {
        input.remove()
    });
}


addSubmitEvents();
