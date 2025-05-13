const menu = document.getElementById("menu");
const itens = document.getElementById("itens");
let state;

window.addEventListener("load", () => {
    menu.style.display = window.innerWidth <= 575 ? "block" : "none";
    itens.style.display = window.innerWidth <= 575 ? "none" : "flex";
    state = 0;
});

function changeSize() {
    if (window.innerWidth <= 575) {
        if (state == 0) {
            itens.style.display = "none";
            menu.textContent = "menu";
        } else {
            itens.style.display = "flex";
            menu.textContent = "menu_open";
        }
    } else {
        itens.style.display = "flex";
    }

    menu.style.display = window.innerWidth <= 575 ? "block" : "none";
}

function openMenu() {
    if (state == 0) {
        menu.textContent = "menu_open";
        menu.classList.remove("burguer");
        menu.classList.add("menu-open");
        itens.style.display = "flex";
        state = 1;
    } else {
        menu.textContent = "menu";
        menu.classList.remove("menu-open");
        menu.classList.add("burguer");
        itens.style.display = "none";
        state = 0;
    }
}