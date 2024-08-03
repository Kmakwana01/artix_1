var acc11 = document.getElementsByClassName("accordion11");
var j;


function openNav() {
  document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
  document.getElementById("myNav").style.width = "0%";
}

for (j = 0; j < acc11.length; j++) {
  acc11[j].addEventListener("click", function() {
    this.classList.toggle("active11");
    var panel11 = this.nextElementSibling;
    if (panel11.style.maxHeight) {
      panel11.style.maxHeight = null;
    } else {
      panel11.style.maxHeight = panel11.scrollHeight + "px";
    } 
  });
}