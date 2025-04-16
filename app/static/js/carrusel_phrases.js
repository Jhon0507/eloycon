const phrasesCarrusel = document.getElementById('phrases-carrusel');
const phrases = phrasesCarrusel.querySelectorAll('div');
let currentIndex = 0;

// clone first phrase and add at the final to get a slow transition
const firstPhrase = phrases[0].cloneNode(true);
phrasesCarrusel.appendChild(firstPhrase);

// function that will be move phrases
function movePhrases() {
    currentIndex++;
    phrasesCarrusel.style.transform = `translateX(-${currentIndex * 100}%)`
    // at the last phrase restart carrusel phrases without animation
    if (currentIndex === phrases.length) {
        setTimeout(() => {
            phrasesCarrusel.style.transition = 'none';
            currentIndex = 0;
            phrasesCarrusel.style.transform = 'translateX(0)';
            void phrasesCarrusel.offsetWidth;
            phrasesCarrusel.style.transition = 'transform 1s ease-in-out';
        }, 1000);
    }
}

// start carrusel of phrases
setInterval(movePhrases, 5000);

// adjust the window when we change size
window.addEventListener('resize', () => {
    phrasesCarrusel.style.transition = 'none';
    phrasesCarrusel.style.transform = `translateX(-${currentIndex * 100}%)`;
    void phrasesCarrusel.offsetWidth;
    phrasesCarrusel.style.transition = 'transform 1s ease-in-out';
});