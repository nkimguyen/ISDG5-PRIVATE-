document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("login-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;


    const user = {email: email, password: password, role: "user"
    };

    sessionStorage.setItem("user", JSON.stringify(user))
    window.location.href = "welcome.html"
  });
});
