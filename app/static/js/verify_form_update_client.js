const formUpdateClient = document.getElementById('form-update-client');
const nameInput = document.getElementById('name');
const surnamesInput = document.getElementById('surnames');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const directionInput = document.getElementById('direction');
const phoneInput = document.getElementById('phone');
const provinceInput = document.getElementById('province');
const error = document.getElementById('error')
const lang = document.documentElement.lang;

function verifyFormUpdate (event) {
    if (nameInput.value.trim() === '' || /\d/.test(nameInput.value)) {
        nameInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Tu nombre no puede estar vacío ni tener números' : "Your name can't be empty or have numbers";
        return false;
    } else if (surnamesInput.value.trim() === '' || /\d/.test(surnamesInput.value)) {
        surnamesInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Tus apellidos no pueden estar vacíos o tener números' : "Your surnames can't be empty or have numbers";
        return false;
    } else if (usernameInput.value.trim() === '') {
        usernameInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Tu nombre de usuario no puede estar vacío' : "Your username can't be empty";
        return false;
    } else if (emailInput.value.trim() === '' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
        emailInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Tu email esta vacío o tiene un mal formato' : "Your email is empty or poorly formatted";
        return false;
    } else if (directionInput.value.trim() === '') {
        directionInput.focus();
        event.preventDefault();
        error.innerText = 'lang' === 'es' ? 'Tu direccion no puede estar vacío' : "Your address can't be empty";
        return false;
    } else if (phoneInput.value.trim() === '' || !/^\+\d{1,3}\s\d{3}\s\d{3}\s\d{3}$/.test(phoneInput.value)) {
        phoneInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'El numero debe tener este format: +34 123 456 789' : "The number must have this format: +34 123 456 789";
        return false;
    } else if (provinceInput.value.trim() === '') {
        provinceInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'La provincia no puede estar vacío' : "Province can't be empty";
        return false;
    }
    return true;
} 

formUpdateClient.addEventListener('submit', verifyFormUpdate);

const formUpdateClientPassword = document.getElementById('form-update-client-password');
const actualPassword = document.getElementById('actual');
const newPassword = document.getElementById('new');
const repeatPassword = document.getElementById('repeat');
const errorPassword = document.getElementById('error_password_1')

function verifyFormUpdatePassword (event) {
    if (actualPassword.value.trim() === '' || newPassword.value.trim() === '' || repeatPassword.value.trim() === '') {
        newPassword.focus();
        event.preventDefault();
        errorPassword.innerText = lang === 'es' ? 'Completa todos los campos para cambiar de contraseña' : "Complete all the files to change password";
        return false;
    } else if (newPassword.value.trim() !== repeatPassword.value.trim()) {
        event.preventDefault();
        errorPassword.innerText = lang === 'es' ? 'La nueva contraseña no coincide con la repetida' : "The new password is not same as repeat password"
        return false;
    }
    
    return true;
}

formUpdateClientPassword.addEventListener('submit', verifyFormUpdatePassword)