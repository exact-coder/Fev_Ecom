let xmark_icon = document.querySelector(".xmark_icon");
let cart_hover_list_item = document.querySelector(".cart_hover_list_item");

function removeItem(e) {
    e.target.parentNode.remove();
}

xmark_icon.addEventListener("click", removeItem);