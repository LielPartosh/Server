var i = 0;
var text= "Most dogs need daily attention in order to be happy";
var speed = 50;

function TypingText(){
    if(i<text.length){
        document.getElementById("pText").innerHTML+= text.charAt(i);
        i++;
        setTimeout(TypingText,speed)
    }
}

function clearF() {
    var DogsNameInput = document.getElementById("DogsName");
    var DogsColorInput = document.getElementById("DogsColor");
    var DogsTypeInput = document.getElementById("DogsType");
    var DogsGenderInput = document.getElementById("DogsGender");
    var DogsAgeInput = document.getElementById("DogsAge");
    var ownersPhoneNumberInput = document.getElementById("ownersPhoneNumber");
    var EmailInput = document.getElementById("Email");

      if (DogsNameInput.value !="" || DogsColorInput.value !="" || DogsTypeInput.value !="" || DogsGenderInput.value !="" || DogsAgeInput.value !="" || ownersPhoneNumberInput.value !="" || EmailInput.value !="") {
        DogsNameInput.value = "";
        DogsColorInput.value = "";
        DogsTypeInput.value = "";
        DogsGenderInput.value = "";
        DogsAgeInput.value = "";
        ownersPhoneNumberInput.value = "";
        EmailInput.value = "";
      }
  }

function sendMassageAfterSumbit(e){
  
    alert("Your doggy details have been saved!");
    e.preventDefault();

}


//pull the pathname from window location
const activePage = window.location.pathname;

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});

function get_user_json(user_id){
    fetch('https://reqres.in/api/users/'+user_id).then(
        response => response.json()
    ).then(
        responseOBJECT => create_user(responseOBJECT.data)
    ).catch(
        err => console.log(err)
    );
}

function create_user(response){
    let user = response;
    const currMain = document.querySelector("main")

    const section = document.createElement('section')
    section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
         <span>${user.first_name} ${user.last_name}</span>
         <br>
         <a href="mailto:${user.email}">Send Email</a>
        </div> 
        `
    currMain.appendChild(section)
}


