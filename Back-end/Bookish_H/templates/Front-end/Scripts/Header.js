// function showMenu(){
//     const menu = document.querySelector('.menu')
//     menu.style.display = 'flex'
// }
// function hideMenu(){
//     const menu = document.querySelector('.menu')
//     menu.style.display = 'none'
// }
// function showAdd() {
//     const addContainer = document.querySelector('.add_container');
//     addContainer.style.display = 'flex';
// }

// function hideAdd() {
//     const addContainer = document.querySelector('.add_container');
//     addContainer.style.display = 'none';
// }
function showRoomForm() {
    var form = document.getElementById("roomForm");
    form.style.display = "block";
}

function submitForm() {
    document.getElementById("createRoomForm").submit();
}