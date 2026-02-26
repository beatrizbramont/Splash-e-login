function login() {
    const email = document.getElementById("email").value;
    const senha = document.getElementById("password").value; // ← corrigido aqui

    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, senha })
    })
    .then(response => response.json())
    .then(data => {

        if (data.redirect === "cadastro") {
            alert("Usuário não encontrado. Faça o cadastro.");
            window.location.href = "/cadastro";
            return;
        }

        if (data.message) {
            localStorage.setItem("user_id", data.user_id);
            window.location.href = "/otp";
        } else {
            alert(data.error);
        }
    });
}
