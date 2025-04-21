const imgContainer = document.querySelector('.last-projects');
const imgs = document.querySelectorAll('.last-projects a img');
const numImgs = imgs.length;
let index = 0;

const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

function updateCarousel() {
    const width = imgs[0].clientWidth;
    imgContainer.style.transform = `translateX(-${index * width}px)`;

    // enable or disable button
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === numImgs - 4;
}

prevBtn.addEventListener('click', () => {
    if (index > 0) {
        index --;
        updateCarousel();
    }
});

nextBtn.addEventListener('click', () => {
    if (index < numImgs - 4) {
        index++;
        updateCarousel();
    }
});

window.addEventListener('resize', updateCarousel);
updateCarousel();