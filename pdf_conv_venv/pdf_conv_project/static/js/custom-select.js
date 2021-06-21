
function controlCustSelOptContainer(open = true) {
    // default open option container is true
    const custSelOptContainer = document.querySelector('.custom-select-opt-container');

    if(open) {
        // Set position coordinate for the option container to open
        const custSelBox = custSelOptContainer.previousElementSibling;
        const positionXOffset = custSelBox.offsetLeft;
        const positionYOffset = custSelBox.offsetTop + custSelBox.offsetHeight;
        custSelOptContainer.style.left = positionXOffset + 'px';
        custSelOptContainer.style.top = positionYOffset + 'px';

        // Display option container
        custSelOptContainer.classList.remove('custom-select-opt-container-hide');
        custSelOptContainer.classList.add('custom-select-opt-container-show');
    } else {
        // Hide option container
        custSelOptContainer.classList.remove('custom-select-opt-container-show');
        custSelOptContainer.classList.add('custom-select-opt-container-hide');
    }

}

function controlSelBox() {
    const caret = document.querySelector('.select-caret');

    if(caret.classList.contains('select-caret-up')) {
        // Options container is opened, going to close
        caret.classList.remove('select-caret-up');
        controlCustSelOptContainer(false);
    } else {
        // Options container is closed, going to open
        caret.classList.add('select-caret-up');
        controlCustSelOptContainer();
    }
}

function selectOption(event) {
    const originalSelect = document.getElementById('id_conversion_mode');
    if(event) {
        originalSelect.value = event.target.dataset.value;
    }
    const selectedOption = originalSelect.querySelector(`option[value='${originalSelect.value}']`);
    document.querySelector('.select-selected').textContent = selectedOption.textContent;
}

function initCustomSelect() {
    const custSelBox = document.querySelector('.custom-select-box');
    const custSelOptContainer = document.querySelector('.custom-select-opt-container');
    // Display current option value on custom select box
    selectOption();
    // Add click listener for custom select box
    custSelBox.addEventListener('click', controlSelBox);
    // Close the option container when clicked outside of the container
    document.addEventListener('click', event => {
        if(!custSelBox.contains(event.target) || custSelOptContainer.contains(event.target)) {
            if(custSelOptContainer.classList.contains('custom-select-opt-container-show')) {
                controlSelBox();
            }
        }
    });
    // Add click listener for each option
    const optionsCollection = custSelOptContainer.children;
    for(let i = 0; i < optionsCollection.length; i++) {
        optionsCollection[i].addEventListener('click', selectOption)
    }

}

// Initiate custom select when document is ready/loaded
const checkReadyStateInterval = setInterval(() => {
    if (document.readyState === "complete") {
        clearInterval(checkReadyStateInterval);
        initCustomSelect();
    }
}, 10);