const imgContainer = document.querySelector('.imgs-project');
const imgs = document.querySelectorAll('.imgs-project img');
const numImgsLastProjects = imgs.length;
let cont = 0;

const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

function updateCarousel() {
    const width = imgs[0].clientWidth;
    imgContainer.style.transform = `translateX(-${cont * width}px)`;

    // enable or disable button
    prevBtn.disabled = cont === 0;
    nextBtn.disabled = cont === numImgsLastProjects - 3;
}

prevBtn.addEventListener('click', () => {
    if (cont > 0) {
        cont --;
        updateCarousel();
    }
});

nextBtn.addEventListener('click', () => {
    if (cont < numImgsLastProjects - 3) {
        cont++;
        updateCarousel();
    }
});

window.addEventListener('resize', updateCarousel);
updateCarousel();