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
    }).then(() => {
        limpandoForm()
    })
    .catch(error => {
        console.error(`Requisição falhou: ${error}`);
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
      // Delay the hiding of the modal for a few seconds to allow the user to read the "concluded" message
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
  
  