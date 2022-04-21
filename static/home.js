var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
      document.getElementById('sort').innerHTML = "Sort"
      
    } else {
      content.style.display = "block";
      document.getElementById('sort').innerHTML = "Sort ▼"
      
    }
  });
}