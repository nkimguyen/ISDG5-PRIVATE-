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


function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}