document.addEventListener("DOMContentLoaded", function () {
  const welcomeMessage = document.getElementById("welcome-message");
  const logoutButton = document.getElementById("logoutBtn");


  const user = JSON.parse(sessionStorage.getItem("user"));

  if (user) {
    if (user.role === "staff") {
      welcomeMessage.textContent = `Welcome staff member, ${user.name}! Your email is ${user.email}`;
    } else {
      welcomeMessage.textContent = `Welcome ${user.name}! Your email is ${user.email}`;
    }
  }



  logoutButton.addEventListener("click", function () {
    sessionStorage.clear();
    window.location.href = "logout.html"
  })
});

