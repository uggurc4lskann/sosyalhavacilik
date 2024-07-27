const mobileBtn = document.querySelector('.mobile-btn');
const menu = document.querySelector('.sidebar-section');


mobileBtn.addEventListener('click', e => {

    menu.classList.toggle('openSidebar')
})
