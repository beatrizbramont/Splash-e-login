const loginBtn = document.getElementById("login-btn");
const message  = document.getElementById("message");

loginBtn.addEventListener("click", async () => {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    message.textContent = "Carregando...";
    message.style.color = "#ffa500";

    try {
        const response = await fetch("https://reqres.in/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        });

        const data = await response.json();

        if (response.ok) {
            message.textContent = "Login bem-sucedido! ✅";
            message.style.color = "#00ff7f";

            localStorage.setItem("token", data.token);

            setTimeout(() => {
                window.location.href = "/html/index.html";
            }, 1000);
        } else {
            message.textContent = data.error || "Falha no login ❌";
            message.style.color = "#ff4b4b";
        }
    } catch (err) {
        message.textContent = "Erro de conexão ❌";
        message.style.color = "#ff4b4b";
    }
});
