function addClickSelect(choices) {
    for (let choice of choices) {
        choice.addEventListener('click', event => {
            target = event.target;
            if (target.tagName == 'DIV') {
                label = target.getElementsByTagName('label')[0];
                input = label.getElementsByTagName('input')[0];
                input.checked = true;
            }
        });
    }
}


function addStyle(choices) {
    for (let choice of choices) {
        label = choice.getElementsByTagName('label')[0];
        if (label !== undefined) {
            input = label.getElementsByTagName('input')[0];
            label.classList.add('cursor-pointer', 'flex', 'items-center', 'gap-4');
            input.classList.add('cursor-pointer', 'w-4', 'h-4', 'mb-1');
        }
    }
}


function removeBlankFields(choices) {
    for (let choice of choices) {
        label = choice.getElementsByTagName('label')[0];
        input = choice.getElementsByTagName('input')[0];
        if (label !== undefined) {
            if (label.htmlFor[15] == 0) {
                choice.remove();
            }
        }
    };
}


let choices = document.getElementsByClassName('choice');
removeBlankFields(choices);
addClickSelect(choices);
addStyle(choices);
