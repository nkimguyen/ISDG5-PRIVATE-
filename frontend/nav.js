document.addEventListener("DOMContentLoaded", function () {
  const accountLink = document.getElementById("account-link");

  if (!accountLink) return;

  accountLink.addEventListener("click", function (event) {
    event.preventDefault();

    const user = sessionStorage.getItem("user");

    if (user) {
      window.location.href = "welcome.html";
    } else {
      window.location.href = "login.html";
    }
  });
});