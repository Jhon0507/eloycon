function openModal() {
    document.getElementById('modal').classList.add('show')
}

function closeModal(event) {
    if (event.target === event.currentTarget) {
        document.getElementById('modal').classList.remove('show');
    }
}