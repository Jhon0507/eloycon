document.addEventListener("DOMContentLoaded", function () {
    const toggleButtons = document.querySelectorAll('.toggle-info');

    toggleButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Encuentra el contenedor del proyecto (padre)
            const projectContainer = this.closest('.project-container');

            // Encuentra el div con clase .info-project dentro de ese contenedor
            const infoSection = projectContainer.querySelector('.info-project');

            // Alterna el display
            if (infoSection.style.display === "block") {
                infoSection.style.display = "none";
                this.classList.remove('rotate');
            } else {
                infoSection.style.display = "block";
                this.classList.add('rotate');
            }
        });
    });
});
