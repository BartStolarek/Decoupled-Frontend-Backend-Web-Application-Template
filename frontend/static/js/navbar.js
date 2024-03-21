document.querySelector('.menu-icon').addEventListener('click', function() {
    this.classList.toggle('active');
    document.querySelector('#menuOverlay').classList.toggle('hidden');
});