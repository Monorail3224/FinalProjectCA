// add_entry.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("add-entry-form");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
  
      const websiteName = document.getElementById("website_name").value;
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;
  
      const formData = new FormData();
      formData.append("website_name", websiteName);
      formData.append("username", username);
      formData.append("password", password);
  
      fetch("/api/add_password_entry/", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          // Handle the response as needed (e.g., display a success message)
          console.log(data);
        })
        .catch((error) => {
          // Handle errors (e.g., display an error message)
          console.error(error);
        });
    });
  
    // Function to get CSRF token from cookies
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.startsWith(name + "=")) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  });
  