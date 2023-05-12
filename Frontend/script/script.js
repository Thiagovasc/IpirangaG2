const form = document.querySelector('#pesquisa-form');
const fieldsets = form.querySelectorAll('fieldset');
const fieldsetFront = document.querySelector(".fieldsetAtualFront")
const fielsetLength = document.querySelector(".fiedsetLenFront")
const nextBtn = form.querySelectorAll(".next-btn")
let fieldsetAtual = 0;



function exibirFieldset(index){
    for(let i = 0; i < fieldsets.length; i++){
        if(i === index){
            fieldsets[i].style.display = "block"
            fieldsetFront.innerHTML = `${i + 1} /`
            fielsetLength.innerHTML = parseInt(fieldsets.length)
        }
        else {
            fieldsets[i].style.display = "none"
        }
        //i === index ? fieldsets[i].style.display = "block" : fieldsets[i].style.display = "none"
    }
}


function proximoField(){
    if(fieldsetAtual < fieldsets.length - 1){
        fieldsetAtual++
        exibirFieldset(fieldsetAtual)
    }
}

nextBtn.forEach((button) => {
    button.addEventListener('click', proximoField)
})

exibirFieldset(fieldsetAtual)