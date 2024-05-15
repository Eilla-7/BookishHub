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


    document.getElementById("searchForm").addEventListener('DOMContentLoaded', function(event) {
        event.preventDefault(); // Prevent default form submission
        
        // Get the search query from the current form 
        var formData = new FormData(this);
        
        // Make an AJAX request to the search_rooms view
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Update the search results div with the response
                    document.getElementById("searchResults").innerHTML = xhr.responseText;
                } else {
                    console.error('Error:', xhr.status);
                }
            }
        };
        xhr.open("GET", "/search_rooms/?q=" + new URLSearchParams(formData).toString(), true);
        xhr.send();
    });


function showRoomForm() {
    var form = document.getElementById("roomForm");
    form.style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

function hideRoomForm() {
    var form = document.getElementById("createRoomForm");
    form.style.display = "none";
    document.getElementById("overlay").style.display = "none";
}
function submitForm() {
    document.getElementById("createRoomForm").submit();
    hideRoomForm();
}
