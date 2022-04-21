
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("btn3");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


function to() {
    var val = document.getElementById("to").value;
    document.getElementById('h5').value
                = val;

}

function from() {
    var val = document.getElementById("from").value;
    document.getElementById('h6').value
                = val;

}
var m =document.querySelector('[name=m').value;
var l =document.querySelector('[name=l').value;
var xl =document.querySelector('[name=xl').value;
var xxl =document.querySelector('[name=xxl').value;
var xxxl =document.querySelector('[name=xxxl').value;
var a = m+l+xl+xxl+xxxl;
var total = document.getElementById('h7').value=a;


function total(input1){
    var l = document.getElementsById('l').value= input1;
    alert(l)
}
