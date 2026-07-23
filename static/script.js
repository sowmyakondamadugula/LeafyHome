const ham=document.querySelector("#hambar");
const leftnav=document.querySelector("#leftnav");
const crossbar=document.querySelector("#cross");
//----open and close the navbar with hambutton-----
ham.addEventListener("click",(evt)=>{
    leftnav.style.right="0px";
});
crossbar.addEventListener("click",(evt)=>{
    leftnav.style.right="-3000px";
})
/*user profile */

const userMenu = document.getElementById("userMenu");

function toggleMenu() {
    const userMenu = document.getElementById("userMenu");
    userMenu.classList.toggle("active");
}

document.addEventListener("click", function(e) {

    if (
        !document.querySelector("#user-icon").contains(e.target) &&
        !userMenu.contains(e.target)
    ) {
        userMenu.classList.remove("active");
    }

});

/*adding to cart message */

document.querySelectorAll(".cart-form").forEach(form => {

    form.addEventListener("submit", async function(e) {
        e.preventDefault();

        const csrf = this.querySelector("[name=csrfmiddlewaretoken]").value;

        try {
            const response = await fetch(this.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrf
                }
            });

            const data = await response.json();

            console.log(response.status);
            console.log(data);
            

            if (response.status === 401) {
                Swal.fire({
                    icon: "warning",
                    title: "Login Required",
                    text: data.message,
                    confirmButtonText: "Login",
                    showCancelButton: true,
                    cancelButtonText: "Cancel"
                }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = "/login/";
                    }
                });

                return;
            }

            Swal.fire({
                toast: true,
                position: "top-end",
                icon: "success",
                title: data.message,
                showConfirmButton: false,
                timer: 2000
            });

        } catch (err) {
            console.error(err);
        }
    });

});



/*-------------------------------*/
function buy_now(){
    alert("Order placed successfully! (Demo Project)");
}