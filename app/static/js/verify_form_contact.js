const formInput = document.getElementById('form-contact');
const nameInput = document.getElementById('name');
const surnamesInput = document.getElementById('surnames');
const emailInput = document.getElementById('email');
const locationInput = document.getElementById('location')
const serviceInput = document.getElementById('service');
const ideaInput = document.getElementById('idea');
const error = document.getElementById('error');
const lang = document.documentElement.lang;

function verifyForm(event) {
    if (nameInput.value.trim() === '' || /\d/.test(nameInput.value)) {
        nameInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Completa tu nombre' : 'Complete your name';
        return false;
    } else if (surnamesInput.value.trim() === '' || /\d/.test(surnamesInput.value)) {
        surnamesInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Completa tus apellidos' : 'Complete your surnames';
        return false;
    } else if (emailInput.value.trim() === '' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
        emailInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Revisa tu correo' : 'Review your email';
        return false;
    } else if (locationInput.value.trim() === '' || /\d/.test(locationInput.value)) {
        locationInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Introduce tu localidad' : 'Introduce your location';
        return false;
    } else if (serviceInput.value === '0') {
        serviceInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Selecciona un tipo de servicio' : 'Select your type service';
        return false;
    } else if (ideaInput.value.trim() === '') {
        ideaInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Explicanos tus ideas' : 'Explain your ideas';
        return false;
    }
    return true;
}

formInput.addEventListener('submit', verifyForm);
