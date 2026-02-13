// Loader on page load
window.onload = () => {
    document.getElementById("loader").style.display = "none";
};

document.getElementById("loader").style.display = "block";


// Dark mode toggle
const toggle = document.getElementById("darkToggle");
if(toggle){
    toggle.onclick = () => {
        document.body.classList.toggle("dark");
    };
}
function saveToHistory(mail) {

    let history = JSON.parse(localStorage.getItem("mailHistory")) || [];

    if(!history.includes(mail)){
        history.push(mail);
    }

    localStorage.setItem("mailHistory", JSON.stringify(history));
}


// Email preview modal
const modal = document.getElementById("emailModal");
const modalText = document.getElementById("modalText");
const closeModal = document.getElementById("closeModal");

document.querySelectorAll(".email-card").forEach(card => {
    card.addEventListener("click", () => {
        modal.style.display = "block";
        modalText.innerText = card.innerText;
    });
});

if(closeModal){
    closeModal.onclick = () => modal.style.display = "none";
}


const search = document.getElementById("searchBox");

if(search){
    search.addEventListener("keyup", () => {
        const value = search.value.toLowerCase();
        document.querySelectorAll(".email-card").forEach(card => {
            card.style.display =
                card.innerText.toLowerCase().includes(value)
                ? "block"
                : "none";
        });
    });
}
