const formInput = document.getElementById('form-add-project');
const nameInput = document.getElementById('name');
const provinceInput = document.getElementById('province');
const startDateInput = document.getElementById('start-date');
const budgetInput = document.getElementById('budget');
const error = document.getElementById('error');
const lang = document.documentElement.lang;

function verifyForm(event) {
    if (nameInput.value.trim() === '') {
        nameInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Completa el nombre' : 'Complete the name';
        return false;
    } else if (provinceInput.value.trim() === '' || /\d/.test(provinceInput.value)) {
        provinceInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Introduce la provincia' : 'Introduce province';
        return false;
    } else if (!startDateInput.value) {
        startDateInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Introduce una fecha' : 'Introduce date'
        return false;
    } else if (!budgetInput.value) {
        budgetInput.focus();
        event.preventDefault();
        error.innerText = lang === 'es' ? 'Rellena el presupuesto' : 'Fill in the budget';
        return false;
    }
    return true;
}

formInput.addEventListener('submit', verifyForm);