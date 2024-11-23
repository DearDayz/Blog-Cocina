let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

function showSlide(index) {
    slides[currentIndex].classList.remove('active');
    currentIndex = (index + slides.length) % slides.length;
    slides[currentIndex].classList.add('active');
}

function showNextSlide() {
    showSlide(currentIndex + 1);
}

function showPreviousSlide() {
    showSlide(currentIndex - 1);
}

let intervalId = setInterval(showNextSlide, 3000);

prevBtn.addEventListener('click', () => {
    clearInterval(intervalId);
    showPreviousSlide();
    intervalId = setInterval(showNextSlide, 3000);
});

nextBtn.addEventListener('click', () => {
    clearInterval(intervalId);
    showNextSlide();
    intervalId = setInterval(showNextSlide, 3000);
});