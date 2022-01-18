var slides = document.querySelectorAll('#slides > img');
var current = 0;

showSlides(current);

function showSlides(n) { 
    for(var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[current].style.display = "block";
    current++;

    if(current > slides.length - 1) {
        current = 0;
    }

    setTimeout(showSlides, 2000);
}