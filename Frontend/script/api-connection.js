const submitBtn = document.querySelector(".submit-btn");
const reqBtn = document.querySelector(".requisicao-cadastros")
const numeroDeRequisicoes = document.querySelector(".numero-cadastros")
const modal = document.querySelector(".modal")
const modalTitulo = document.querySelector("#modal-titulo")
const modalMensagem = document.querySelector("#modal-mensagem")



submitBtn.addEventListener('click', () => {
    const formData = new FormData(form);
    const object = {};
    formData.forEach((value, key) => {
        object[key] = value;
    });
    const json = JSON.stringify(object);

    fetch('http://localhost:8000/novo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: json
    })
    .then(response => response.json())
    .then(data => {
        console.log(`Requisição falhou: ${data}`);
    })
    .catch(error => {
        
    }).finally(() => {
        form.style.display = "none";
        modal.style.display = "block";
        modal.setAttribute("id", "cadastros")
        modalTitulo.innerHTML = "Error";
        modalMensagem.innerHTML = "Requisição falhou";
        // Delay the displaying of the initial menu for a few seconds to allow the user to read the error message
        setTimeout(() => {
            modal.style.display = "none";
            menuInicial.style.display = "flex";
        }, 2000);
    }); 
});



const gerandoCadastros = async (n) => {
    containerCadastros.style.display = "none"
    modal.style.display = "block";
    modal.setAttribute("id", "cadastros")
    const url = `http://localhost:8000/gerar-cadastros?cadastros_request=${n}`;
  
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      if (!response.ok) {
        throw new Error("Request failed");
      }
  
      const data = await response.json();
  
      modalTitulo.innerHTML = "Cadastros Gerados";
      modalMensagem.innerHTML = "Cadastros concluídos com sucesso";
    } catch (error) {
      modalTitulo.innerHTML = `Erro: ${error}`;
      modalMensagem.innerHTML = "Requisição falhou";
    } finally {

      setTimeout(() => {
        modal.style.display = "none";
        containerCadastros.style.display = "flex"
      }, 3000);
    }
  };
  
  
  reqBtn.addEventListener("click", () => {
    const n = parseInt(numeroDeRequisicoes.value);
    gerandoCadastros(n);
  });
  
  