// Prepare form data
function prepFormdata(uploadFile) {
    const targetFile = uploadFile.files;

    // If there is items in the file input, prepare formdata to submit
    if(targetFile.length) {
        const formdata = new FormData();
        const csrf = document.querySelector("input[name='csrfmiddlewaretoken']").value;
        formdata.append('csrfmiddlewaretoken', csrf);
        const filelistName = uploadFile.getAttribute('name');
        for(let i=0; i < targetFile.length; i++) {
            formdata.append(filelistName, targetFile[i]);
        }
        return formdata;
    }
    return null;
}

// Send form data through fetch API
function sendFormdata(uploadForm, formdata) {
    dispLoading(uploadForm);
    fetch(
        uploadForm.getAttribute('action'), 
        {
            method:'POST',
            mode:'cors',
            cache:'default',
            credentials:'include',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest', 
                // 'X-CSRFToken': csrf,
            },
            body: formdata 
        }
    ).then(
        res => res.json()
    ).then(result =>{
        if(result?.redirectUrl) {
            window.location.replace(result.redirectUrl);
        } else {
            if(result?.error) {
                const convError = document.getElementById('convert-error');
                convError.textContent = result.error;
                dispLoading(uploadForm, false);
            }

        }
    }).catch(err => {
        console.log(err);
    });
}

// Funtion to handle submit button and display selected file info text
function dispSubmitBtn(uploadFile, show = true) {
    // uploadFile is selector for form input type=file. show is true to display submit btn, 
    // false is to hide. Info text also change based on is there file selected
    const uploadBtn = document.querySelector("input[type='submit']");
    const infoText = document.querySelector(".convert-file-info");
    if(show) {
        uploadBtn.classList.add('show-btn');
        uploadBtn.disabled = false;
        // limit file name length to 18 char max, 
        // else its truncated to length of 18 excluding '...'
        const filename = uploadFile.files[0].name.length <= 18 
            ? uploadFile.files[0].name 
            : uploadFile.files[0].name.slice(0, 15) + '...';

        infoText.textContent = uploadFile.files.length > 1
            ? `${uploadFile.files.length} files selected` 
            : `${filename} is selected`;
    } else {
        uploadBtn.classList.remove('show-btn');
        uploadBtn.disabled = true;
        infoText.textContent = 'No file selected';
    }
}

// Function to show or hide loading, also reset form when hiding loading
function dispLoading(uploadForm, show = true) {
    const loadingComp = document.querySelector(".loading-container");
    const formContainer = uploadForm.parentElement
    if(show) {
        // display loading component
        formContainer.classList.add('hidden');
        loadingComp.classList.remove('hidden');
    } else {
        // hide loading component
        uploadForm.reset();
        dispSubmitBtn(uploadForm[0], false);
        loadingComp.classList.add('hidden');
        formContainer.classList.remove('hidden');
    }
}

// Function handling form submission
function onFileUpload() {
    const uploadForm = document.querySelector(".convert-form");
    const uploadFile = uploadForm[0];
    uploadForm.addEventListener('submit', event => {
        event.preventDefault();
        const formdata = prepFormdata(uploadFile);
        if(formdata instanceof FormData) sendFormdata(uploadForm, formdata);
        
        // prevent form from submitting after sending request
        return false;
    }, false);
}

// Function handling when user selected what file/files to upload
function onFileSelected(event) {
    if(event.target.files.length) {
        dispSubmitBtn(event.target);
    } else {
        dispSubmitBtn(event.target, false);
    }
}

// Funcion to run when document is ready
function main() {
    const uploadFile = document.querySelector("input[type='file']");
    dispSubmitBtn(uploadFile, false);
    onFileUpload();
    uploadFile.addEventListener('change', onFileSelected);
}

// Initiate script for convert page when document is ready/loaded
const checkReadyStateInterval = setInterval(() => {
    if (document.readyState === "complete") {
        clearInterval(checkReadyStateInterval);
        main();
    }
}, 10);