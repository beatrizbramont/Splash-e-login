function cadastrar() {
    const nome = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/cadastro", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nome, email, senha })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert("Cadastro realizado com sucesso!");
            window.location.href = "/login";
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error("Erro:", error);
    });
}
