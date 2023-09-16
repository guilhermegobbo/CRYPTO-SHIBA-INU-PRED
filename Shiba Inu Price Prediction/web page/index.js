function BtnClick() {
    const start_date = document.getElementById("start-date").value;
    const end_date = document.getElementById("end-date").value;
    const mensagemElement = document.getElementById("mensagem");

    if (!start_date || !end_date) {
        mensagemElement.textContent = 'Preencha ambas as datas!';
        return;
    }

    mensagemElement.textContent = '';

    var url = 'http://localhost:5000/previsao';

    var xhr = new XMLHttpRequest();

    xhr.open('GET', `${url}/${start_date}/${end_date}`, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var previsoes = JSON.parse(xhr.responseText).previsoes;
                mensagemElement.innerHTML = "";
                for (var i = 0; i < previsoes.length; i++) {
                    var previsao = previsoes[i];
                    var p = document.createElement("p");
                    p.textContent = 'Data: ' + previsao.data + ', Previsão: ' + previsao.previsao;
                    mensagemElement.appendChild(p);
                }
            } else {
                mensagemElement.textContent = 'Erro: ' + JSON.parse(xhr.responseText);
            }
        }
    };

    xhr.send();
}