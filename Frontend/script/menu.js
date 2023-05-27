const formBtn = document.querySelector(".open-form")
const cadastrosBtn = document.querySelector(".cadastros-btn")
const menuInicial = document.querySelector(".container-menu")
const containerCadastros = document.querySelector(".container-cadastros")
const retornarCadastros = document.querySelector(".retornar-menu")
const footer = document.querySelector("footer")


formBtn.addEventListener("click", exibirForm)
cadastrosBtn.addEventListener("click", exibirContainerCadastros)
retornarCadastros.addEventListener("click", retornarMenu)


function exibirForm(){
    menuInicial.style.display = "none";
    form.setAttribute("class", "pesquisa-form")
}

function exibirContainerCadastros(){
    menuInicial.style.display = "none"
    containerCadastros.style.display = "flex"
    containerCadastros.setAttribute("id", "cadastros")
}

function retornarMenu() {
    containerCadastros.style.display = "none";
    menuInicial.style.display = "block";
  }