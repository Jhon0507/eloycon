const carrusel = document.getElementById('carrusel');
const numImgs = carrusel.children.length;
let index = 0;

function moveCarrusel() {
    const imgWidth = carrusel.querySelector('img').clientWidth;  // get img width
    index++;

    carrusel.style.transition = 'transform 1s ease-in-out';
    carrusel.style.transform = `translateX(-${index * imgWidth}px)`;

    // restart at the end to image 1
    if (index === numImgs - 1) {
        setTimeout(() => {
            carrusel.style.transition = 'none';
            carrusel.style.transform = 'translateX(0px)'
            index = 0;
        }, 1000);
    }
}
let interval = setInterval(moveCarrusel, 7000); // add interval time to change image

// reload img size to responsive
const resizeObservation = new ResizeObserver(() => {
    clearInterval(interval);
    carrusel.style.transition = 'none';
    carrusel.style.transform = 'translate(0px)';
    index = 0;
    interval = setInterval(moveCarrusel, 7000);
});

resizeObservation.observe(document.querySelector('.carrusel-container'));