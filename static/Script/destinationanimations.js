const demographics = document.getElementById('demographics');





function animatePercentage(percentage,element){
    percentage = percentage.split('').splice(0,2).join('');
let pop = 0;
let animationFunction = setInterval(()=>{

    if (pop > percentage){
        clearInterval(animationFunction);
        element.innerHTML = pop + '%';
    } else{
        pop ++;
        element.innerHTML = pop;
    }
},20)

};


if (!!demographics){


const totalPopulation  = document.getElementById('totalPopulation');
const total = +totalPopulation.innerHTML;

document.getElementById('totalPopulation').innerHTML = '0';

let totalNumber = 0;



    let animation = setInterval(function(){

        if (totalNumber > total){
            clearInterval(animation);
            totalPopulation.innerHTML = total;
        } else{
            totalNumber += 200;
            totalPopulation.innerHTML = totalNumber;
        }
    },1);
    
    totalPopulation.addEventListener('click',()=>{
        let totalNumber = 0;
    
    let animation = setInterval(function(){
    
        if (totalNumber > total){
            clearInterval(animation);
            totalPopulation.innerHTML = total;
        } else{
            totalNumber += 200;
            totalPopulation.innerHTML = totalNumber;
        }
    },1);
    
    
    });
    
    
    
    //Male Population Function;
    const malePop = document.getElementById('malePopulation');
    const malePopTotal = malePop.innerHTML;
    
    
    
    animatePercentage(malePopTotal,malePop);
    
    
    malePop.addEventListener('click',()=>{
    
        animatePercentage(malePopTotal,malePop);
    
    
    
    });
    
    
    
    //Female Population Function;
    const femalePop = document.getElementById('femalePopulation');
    const femalePopTotal = femalePop.innerHTML;
    animatePercentage(femalePopTotal,femalePop);
    
    
    femalePop.addEventListener('click',()=>{
        animatePercentage(femalePopTotal,femalePop);
    });
    
    //Total Educated;
    const totalEducated = document.getElementById('totalEducated');
    const totalEducatedPC = totalEducated.innerHTML;
    animatePercentage(totalEducatedPC,totalEducated);
    
    totalEducated.addEventListener('click',()=>{
        animatePercentage(totalEducatedPC,totalEducated);
    });
    
    
    //Male Educated;
    const maleEducated = document.getElementById('maleEducated');
    const maleEducatedPC = maleEducated.innerHTML;
    animatePercentage(maleEducatedPC,maleEducated);
    
    maleEducated.addEventListener('click',()=>{
        animatePercentage(maleEducatedPC,maleEducated);  
    })
    
    
    //Female Educated;
    const femaleEducated = document.getElementById('femaleEducated');
    const femaleEducatedPC = femaleEducated.innerHTML;
    animatePercentage(femaleEducatedPC,femaleEducated);
    
    femaleEducated.addEventListener('click',()=>{
        animatePercentage(femaleEducatedPC,femaleEducated); 
    })
    
    
    
    
    
    
    
    
    
    







}










