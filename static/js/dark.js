
let darkMode = localStorage.getItem('darkMode');
let darkModeButton = localStorage.getItem('darkModeButton');
const darkModeToggle = document.querySelector('#dark-mode-toggle');

darkModeToggle.addEventListener('click', () => {
    darkMode = localStorage.getItem('darkMode');
    if (darkMode !== 'enabled') {   
        enableDarkMode();
    }
    else {       
        disableDarkMode();
    }
});


const enableDarkMode = () => {
    document.body.classList.add('darkmode');
    darkModeToggle.classList.add('dark-mode-toggle');
    localStorage.setItem('darkMode', 'enabled');
    localStorage.setItem('darkModeButton', 'disabled');
}

const disableDarkMode = () => {
    document.body.classList.remove('darkmode');
    darkModeToggle.classList.remove('dark-mode-toggle');
    localStorage.setItem('darkMode', null);
    localStorage.setItem('darkModeButton', 'enabled');
}

if (darkModeButton === 'enabled') {
    darkModeToggle.classList.remove('dark-mode-toggle');   
}
else{
    darkModeToggle.classList.add('dark-mode-toggle');
}

if (darkMode === 'enabled') {
    document.body.classList.add('darkmode');
    enableDarkMode();
}

