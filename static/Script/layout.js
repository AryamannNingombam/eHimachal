var allNavs = document.getElementsByClassName('nav-link');

for (let nav of allNavs){
    if (nav.href === location.href){
        nav.classList.add('selectedNav');
       
    }

}





let goToTop  =  document.getElementById('topButton');
try{
    goToTop.addEventListener('click',()=>{
        window.scrollTo(0,0);
    });
}catch{}



