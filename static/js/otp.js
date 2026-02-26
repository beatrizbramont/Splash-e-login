function verificarOTP() {

    const code = document.getElementById("code").value;
    const user_id = localStorage.getItem("user_id");

    fetch("http://127.0.0.1:5000/verify-otp", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ user_id, code })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert("Login autorizado!");

            localStorage.removeItem("user_id");

            window.location.href = "/index"; 
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error("Erro:", error);
    });
}