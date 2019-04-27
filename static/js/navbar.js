// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navtabs = document.getElementByClass("navtabs");

// Get the offset position of the navbar
var sticky = navtabs.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navtabs.classList.add("sticky")
  } else {
    navtabs.classList.remove("sticky");
  }
}
