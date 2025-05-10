const formInput = document.getElementById('form-register');
const nameInput = document.getElementById('name');
const surnamesInput = document.getElementById('surnames');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const directionInput = document.getElementById('direction');
const provinceInput = document.getElementById('province');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const repeatPasswordInput = document.getElementById('repeat-password');
const error = document.getElementById('error');
const lang = document.documentElement.lang;

function verifyFormRegister (event) {
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
    } else if (passwordInput.value.trim() === '') {
        passwordInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'La contraseña no puede estar vacía' : "The password cannot be empty";
        return false;
    } else if (repeatPasswordInput.value.trim() === '') {
        repeatPasswordInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Debes introducir dos veces la contraseña' : 'You must enter the password twice';
        return false;
    } else if (passwordInput.value.trim() !== repeatPasswordInput.value.trim()) {
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Las contraseñas no coinciden' : 'Passwords are not the same';
        return false;
    }
    return true;
}

formInput.addEventListener('submit', verifyFormRegister);