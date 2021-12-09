const darkBtn = document.querySelector('.fass');
const icon = document.getElementById('icon')
setIcon = localStorage.getItem('sun');

const darkMode = () => {
    document.body.classList.toggle('dark')
}

darkBtn.addEventListener('click', () => {
    // Get the value of the "dark" item from the local storage on every click
    setDarkMode = localStorage.getItem('dark');

    if(setDarkMode !== "on") {
        darkMode();
        icon.classList.remove('bi-moon');
        icon.classList.add('bi-brightness-low-fill');
        // Set the value of the itwm to "on" when dark mode is on
        setDarkMode = localStorage.setItem('dark', 'on');
        setIcon = localStorage.setItem('sun', 'on');
    } else {
        darkMode();
        // Set the value of the item to  "null" when dark mode if off
        icon.classList.remove('bi-brightness-low-fill');
        icon.classList.add('bi-moon');
        setDarkMode = localStorage.setItem('dark', null);
        setIcon = localStorage.setItem('sun', null);
    }
});

// Get the value of the "dark" item from the local storage
let setDarkMode = localStorage.getItem('dark');

// Check dark mode is on or off on page reload
if(setDarkMode === 'on') {
    darkMode();
    icon.classList.remove('bi-moon');
    icon.classList.add('bi-brightness-low-fill');
}

if (setIcon === 'on') {
    icon.classList.remove('bi-moon');
    icon.classList.add('bi-brightness-low-fill');  
}
else{
    icon.classList.remove('bi-brightness-low-fill');
    icon.classList.add('bi-moon');
}