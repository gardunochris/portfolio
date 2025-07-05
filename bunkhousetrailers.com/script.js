function toggleMenu(){
    var nav=document.getElementById('mobile-nav');
    if(nav.classList.contains('show-nav')){
        nav.classList.remove('show-nav');
    } else {
        nav.classList.add('show-nav');
    }
}
