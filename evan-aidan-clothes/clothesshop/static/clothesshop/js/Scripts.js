
    window.onscroll = function() {myFunction()};
    
    var header = document.getElementById("dynamic-header");
    var sticky = header.offsetTop;
    
    function myFunction() {
      if ((window.pageYOffset) >= 40) {
        header.classList.add("sticky");
      } else {
        header.classList.remove("sticky");
      }
    }

    const hamburger = document.querySelector(".hamburger-menu");
    const sidebar = document.querySelector(".sidebar");
    hamburger.addEventListener("click", () => {
      hamburger.classList.toggle("active");
      sidebar.classList.toggle("active");
    });