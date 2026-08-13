const button = document.getElementById("login");

button.onclick = async function() {

   const name = document.getElementById("name").value;

   const response = await fetch("/login", {
      method: "POST",
      headers: {
         "Content-Type": "application/json"
      },
      body: JSON.stringify({
         name: name
      })
   });

   if (response.ok) {

      const data = await response.json();

      window.location.href = "/home?id=" + data.id;
   }
};