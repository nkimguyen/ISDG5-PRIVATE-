document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("staff-register-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const firstName = document.getElementById("staff_first_name").value;
    const lastName = document.getElementById("staff_last_name").value;
    const email = document.getElementById("staff_email").value;
    const staffId = document.getElementById("staff_id").value;

    const user = {"firstName": firstName, "lastName": lastName, "email": email, "staffId": staffId, "role": "staff"
    };

    sessionStorage.setItem("user", JSON.stringify(user));
    window.location.href = "welcome.html";
  });
});
