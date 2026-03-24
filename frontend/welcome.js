document.addEventListener("DOMContentLoaded", function () {
  const welcomeMessage = document.getElementById("welcome-message");
  const logoutButton = document.getElementById("logoutBtn");


  const user = JSON.parse(sessionStorage.getItem("user"));

  if (user) {
    welcomeMessage.textContent = `Welcome! Your email address is ${user.email}.`;
  } else {
    welcomeMessage.textContent = "Please register!";
  }

  logoutButton.addEventListener("click", function () {
    sessionStorage.clear();
    window.location.href = "logout.html"
  })
});
