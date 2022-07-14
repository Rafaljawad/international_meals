function remove_sigin_btn(){
    var x= document.querySelectorAll(".nav-item ")[2]
    console.log(x);
    x.classList.add("hidden");
}


function alertBox(){
    document.querySelector(".alert").classList.remove("hidden")
}
function deleteMeal(){
    document.querySelector(".alert").classList.add("hidden")

}