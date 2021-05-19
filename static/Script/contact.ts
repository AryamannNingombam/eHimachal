
interface requestBody{
    email_address : string,
    message : string
};
interface response { 
    successful  : boolean
};

function getMessage(alert :{message:string,type : string}){

    return `
    <div class="alert alert-${alert.type} alert-dismissible fade show" role="alert">
  ${alert.message}
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>`;
};

class SendingContactRequest{
    constructor(private url : string){}
   async sendRequest(body : requestBody){

       const cookie = this.getCookie('csrftoken')
    let request = await fetch(this.url,{
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken': cookie
        },
        body : JSON.stringify(body)
    });
    const response : response = await request.json();

    return response.successful;
    }
   private getCookie(name : string) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                };
            };
        };

        return cookieValue;
    }
};

//MAIN LOGIC

const successMessage = {message : '<strong>Hello!</strong> We have successfully <strong>got your message</strong> and would try to contact you as soon as possible.<strong>Thanks!</strong>',type : 'success'};
const warningMessage = {message :"<strong>Hello!</strong>  We <strong> coudn't send your request </strong> as you might have entered some invalid credentials. Please enter correct credentials to send the request. <strong>Thanks!</strong>" ,type :'warning'};
const errorMessage = {message : '<strong>Error!</strong> We <strong>could not send your request </strong> due to an internal server error. We apologize for the inconvenience caused. <strong>Sorry!</strong>',type : 'danger'};

const request = new SendingContactRequest('http://127.0.0.1:8000/contact-request/');
let alertSpan = document.getElementById('alertSpan') as HTMLSpanElement;
let submitButton = document.getElementById('submitButton') as HTMLButtonElement;

submitButton.addEventListener('click',(e)=>{
    const emailInput = document.getElementById('email') as HTMLInputElement;
    const messageInput = document.getElementById('content') as HTMLInputElement;
    const email = emailInput.value;
    const message = messageInput.value;

    e.preventDefault();
    const body : requestBody = {email_address: email ,message :message };

    request.sendRequest(body).then(successful=>{
            if (successful){
                let responseAlert =  getMessage(successMessage);
                alertSpan.innerHTML = responseAlert;
                
                
            } else{
               let responseAlert =    getMessage(warningMessage);
               alertSpan.innerHTML = responseAlert;

                
            };
    }
        
    ).catch(error=>{
        let responseAlert =    getMessage(errorMessage);
        alertSpan.innerHTML = responseAlert;

    })
    emailInput.value= '';
    messageInput.value= '';
    
   
    
    
    window.scroll(0,0);
});



