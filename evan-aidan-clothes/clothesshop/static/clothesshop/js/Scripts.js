document.addEventListener('DOMContentLoaded', function() {
    // Sidebar toggle
    const hamburger = document.querySelector('.hamburger-menu');
    const sidebar = document.querySelector('.sidebar');

    let scrollPosition = 0;

    //global page image load in
//    document.addEventListener('DOMContentLoaded', function() {
      

    // Create blackout overlay
    const overlay = document.createElement('div');
    overlay.classList.add('body-overlay');
    document.body.appendChild(overlay);

    function disableScroll() {
        scrollPosition = window.scrollY;
        document.body.style.position = 'fixed';
        document.body.style.top = `-${scrollPosition}px`;
        document.body.style.width = '100%';
    }

    function enableScroll() {
        document.body.style.position = '';
        document.body.style.top = '';
        window.scrollTo(0, scrollPosition);
    }

    if (hamburger && sidebar) {
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            sidebar.classList.toggle('active');
            overlay.classList.toggle('active');   // Show/hide blackout

            if (sidebar.classList.contains('active')) {
                disableScroll();
            } else {
                enableScroll();
            }
        });

        // Close sidebar when clicking the blackout
        overlay.addEventListener('click', function() {
            sidebar.classList.remove('active');
            hamburger.classList.remove('active');
            overlay.classList.remove('active');
            enableScroll();
        });
    }


    // Profile dropdown toggle
    const profileMenuButton = document.getElementById('profile-menu-button');
    const profileDropdown = document.getElementById('profile-dropdown');

    if (profileMenuButton && profileDropdown) {
        profileMenuButton.addEventListener('click', function(event) {
            event.stopPropagation(); // Prevent the window click event from firing
            profileDropdown.classList.toggle('show');
        });

        // Close the dropdown if the user clicks outside of it
        window.addEventListener('click', function(event) {
            if (!profileMenuButton.contains(event.target) && !profileDropdown.contains(event.target)) {
                profileDropdown.classList.remove('show');
            }
        });
    }
});



// Global timer for sales
document.addEventListener('DOMContentLoaded', function() {
    const saleTimerElement = document.getElementById("sale-timer");
    
    // Only run the timer if the element and its data attribute exist
    if (saleTimerElement && saleTimerElement.dataset.targetDate) {
        const targetDateUTC = new Date(saleTimerElement.dataset.targetDate).getTime();
        
        const timerInterval = setInterval(function() {
            const now = new Date().getTime();
            const distance = targetDateUTC - now;
            
            if (distance <= 0) {
                clearInterval(timerInterval); // Stop the timer from running unnecessarily
                saleTimerElement.innerHTML = "EXPIRED";
                return;
            }
            
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            // Use a template literal for cleaner string formatting
            saleTimerElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }, 1000);
    }
});


//animations for topbar text after 5 sec timer
const textBox = document.getElementById('topbar1textleft');
const messages = [
    '<a href="https://discord.gg/vzDV2ddt2V" target="_blank">JOIN OUR DISCORD</a>',
    '<a href="https://www.tiktok.com/@frayyed.com" target="_blank">FOLLOW OUR TIKTOK</a>',
    '<a href="https://www.instagram.com" target="_blank">FOLLOW OUR INSTAGRAM</a>'
];

let current = 0;

function switchText() {
        textBox.style.opacity = 0;


    setTimeout(() => {
      current = (current + 1) % messages.length;
      textBox.innerHTML = messages[current];
      textBox.style.opacity = 1;
    }, 500);
}

  setInterval(switchText, 8000);


  //functionality for product gallery (with fade animations)
document.addEventListener('DOMContentLoaded', function() {
    const primaryImage = document.getElementById('primaryimg');
    const leftArrow = document.getElementById('leftarrowbtn');
    const rightArrow = document.getElementById('rightarrowbtn');
    const thumbnails = document.querySelectorAll('.card2 img');
    

    if (!primaryImage || !leftArrow || !rightArrow || thumbnails.length === 0) return;

    const imageUrls = Array.from(thumbnails).map(thumb => thumb.src);

    //add outline to thumbnail
    if (thumbnails.length > 0) {
        thumbnails[0].classList.add('thumbnail-active');
    }
    

        //global fade function
    function fadeToImage(url) {
        if (primaryImage.src === url) return;

        primaryImage.style.transition = 'none';
        primaryImage.style.opacity = 0;
        primaryImage.offsetWidth;

        //highlight thumbnail
        thumbnails.forEach(thumb => thumb.classList.remove('thumbnail-active'));
        const activeThumb = Array.from(thumbnails).find(thumb => thumb.src === url);
        if (activeThumb) activeThumb.classList.add('thumbnail-active');
        
        setTimeout(() => {
            primaryImage.src = url;
            primaryImage.style.transition = 'opacity 0.4s ease';
            primaryImage.style.opacity = 1;
        }, 20);
    }


    // Arrow functions
    function updateImage(direction) {
        const currentSrc = primaryImage.src;
        let currentIndex = imageUrls.findIndex(url => url === currentSrc);
        if (currentIndex === -1) currentIndex = 0;

        let nextIndex;
        if (direction === 'next') {
            nextIndex = (currentIndex + 1) % imageUrls.length;
        } else {
            nextIndex = (currentIndex - 1 + imageUrls.length) % imageUrls.length;
        }

        fadeToImage(imageUrls[nextIndex]);
    }

    leftArrow.addEventListener('click', () => updateImage('prev'));
    rightArrow.addEventListener('click', () => updateImage('next'));

    //thumbnails
    thumbnails.forEach(thumb => {
        thumb.addEventListener('click', () => {
            fadeToImage(thumb.src);
        });
    });
});
