// function remove_sigin_btn(){
//     var x= document.querySelectorAll(".nav-item ")[2]
//     console.log(x);
//     x.classList.add("hidden");
// }


function alertBox(){
    document.querySelector(".alert").classList.remove("hidden")
    document.querySelector("main").classList.add("overlay")
}
function deleteMeal(){
    document.querySelector(".alert").classList.add("hidden")
    document.querySelector("main").classList.remove("overlay")

}

function makeShadow(element){
    element.classList.add("shadow")
} 
function removeShadow(element){
    element.classList.remove("shadow")
}
function changStarColor(element){
    element.classList.toggle("toggle")
}