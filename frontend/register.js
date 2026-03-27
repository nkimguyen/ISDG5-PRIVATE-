document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("register-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const firstName = document.getElementById("first_name").value;
    const lastName = document.getElementById("last_name").value;
    const email = document.getElementById("email").value;

    const user = {"name": `${firstName} ${lastName}`, "email":email, role: "user"}
    sessionStorage.setItem("user", JSON.stringify(user))
    window.location.href = "welcome.html"
  });
});
