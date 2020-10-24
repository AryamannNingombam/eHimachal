

let mainDiv = document.getElementById('demographics');

if (mainDiv !== null){
    let stats= {
        //Not Optimized Yet
        malePopulation :  parseInt(document.getElementById('malePopulation').innerText.split('').splice(0,2).join('')),
        femalePopulation :  parseInt(document.getElementById('femalePopulation').innerText.split('').splice(0,2).join('')),
        maleLiteracy : parseInt(document.getElementById('maleEducated').innerText.split('').splice(0,2).join('')),
        femaleLiteracy : parseInt(document.getElementById('femaleEducated').innerText.split('').splice(0,2).join('')),
        totalLiteracy : parseInt(document.getElementById('totalEducated').innerText.split('').splice(0,2).join('')),
        
    }

    

let populationChart = document.getElementById('populationChart');
let litChartMale = document.getElementById('literacyChartMale');
let litChartTotal = document.getElementById('literacyChartAll');
let litChartFemale = document.getElementById('literacyChartFemale');

var myChart = new Chart(populationChart, {
    type: 'doughnut',
    data: {
        labels: [ 'Population Men %', 'Population Women %'],
        datasets: [{
            label: '# of Votes',
            data: [stats.malePopulation,stats.femalePopulation],
            backgroundColor: [
                '#FF0000',
                '#FF00E3',
               //Test
              
            ],
            borderColor: [
                '#FF0000',
                '#FF00E3',
                
                
            ],
            hoverBackgroundColor : [
                '#FF6A6A',
                '#C054DC'
            ],
            hoverBackgroundColor : [
                'rgba(229,39,39,0.4)',
                'rgba(232,33,202,0.4)'
            ],
            borderWidth: 1,
           
        }],
        
        
      
    },
    options : [
        {  cutoutPercentage : 50}
    ]
    
});

var myChartLiteracyMale = new Chart(litChartMale, {
    type: 'doughnut',
    data: {
        labels: [ 'Educated M%', 'Uneducated M%'],
        datasets: [{
            label: '# of Votes',
            data: [stats.maleLiteracy,(100 - stats.maleLiteracy)],
            backgroundColor: [
                '#484AD7',
                '#00E2D7',
               //Test
              
            ],
            borderColor: [
                '#050885',
                '#00E2D7',
                
                
            ],
            hoverBackgroundColor : [
                '#6266DC',
                '#95FFF5'
            ],
            
            borderWidth: 1,
           
        }],
        
        
      
    }
    });

var myChartLiteracyAll = new Chart(litChartTotal, {
        type: 'doughnut',
        data: {
            labels: [ 'Educated T%', 'Uneducated T%'],
            datasets: [{
                label: '# of Votes',
                data: [stats.totalLiteracy,(100 - stats.totalLiteracy)],
                backgroundColor: [
                    '#E2590C',
                    '#FCB711',
                   //Test
                  
                ],
                borderColor: [
                    '#FF0000',
                    '#FF00E3',
                    
                    
                ],
                hoverBackgroundColor : [
                    '#FFB38B',
                    '#FCD689'
                ],
               
                borderWidth: 1,
               
            }],
            
            
          
        }
        
    });


var myChartLiteracyFemale = new Chart(litChartFemale, {
        type: 'doughnut',
        data: {
            labels: [ 'Educated F%', 'Uneducated F%'],
            datasets: [{
                label: '# of Votes',
                data: [stats.femaleLiteracy,(100 - stats.femaleLiteracy)],
                backgroundColor: [
                    'rgba(234,247,0,0.6)',
                    'rgba(247,214,1,0.6)',
                   //Test
                  
                ],
                borderColor: [
                    'rgba(234,247,0,0.6)',
                    'rgba(247,214,1,0.6)',
                    
                    
                ],
                hoverBackgroundColor : [
                    'rgba(244,252,151,0.6)',
                    'rgba(249,235,149,0.6)'
                ],
               
                borderWidth: 1,
               
            }],
            
            
          
        },
       
        
    });
    
    
    
    
    }


    


    
