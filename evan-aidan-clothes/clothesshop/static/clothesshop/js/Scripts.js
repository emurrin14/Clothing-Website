document.addEventListener("DOMContentLoaded", () => {
  const revealElements = document.querySelectorAll(".reveal");

  const observerOptions = { root: null, threshold: 0.1 };

  // --- 1️⃣ Lazy-load observer (loads images only when near viewport) ---
  const lazyImageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;

      const img = entry.target;
      const realSrc = img.dataset.src;

      if (realSrc) {
        img.src = realSrc;
        img.removeAttribute("data-src");
      }

      observer.unobserve(img);
    });
  }, {
    rootMargin: "200px", // load slightly before entering viewport
  });

  // Observe all lazy images
  document.querySelectorAll("img[data-src]").forEach(img => {
    lazyImageObserver.observe(img);
  });

  // --- 2️⃣ Reveal animation observer ---
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      const el = entry.target;
      const duration = el.dataset.duration || "600";
      const delay = el.dataset.delay || "0";

      el.style.transitionDuration = `${duration}ms`;
      el.style.transitionDelay = `${delay}ms`;

      if (entry.isIntersecting) {
        el.style.opacity = "1";
        el.style.transform = "translate(0,0) scale(1)";
        el.classList.add("is-visible");
        observer.unobserve(el);
      }
    });
  }, observerOptions);

  // --- 3️⃣ Helper function ---
  const isInViewport = el => {
    const rect = el.getBoundingClientRect();
    return rect.top < window.innerHeight && rect.bottom > 0;
  };

  // --- 4️⃣ Process each reveal element ---
  revealElements.forEach(el => {
    // Add shimmer placeholder
    const placeholder = document.createElement("div");
    placeholder.className = "shimmer-placeholder";
    el.appendChild(placeholder);

    // Find images inside
    const images = el.querySelectorAll("img");

    // Wait for all to load
    const imgPromises = Array.from(images).map(img => {
      if (img.complete && img.src) return Promise.resolve();
      return new Promise(resolve => (img.onload = resolve));
    });

    Promise.all(imgPromises).then(() => {
      placeholder.remove(); // remove shimmer when done

      // Apply starting transform
      const origin = el.dataset.origin || "bottom";
      const distance = el.dataset.distance || "30px";
      const scale = el.dataset.scale || "0.9";

      el.style.opacity = "0";

      switch (origin) {
        case "top":
          el.style.transform = `translateY(-${distance}) scale(${scale})`;
          break;
        case "bottom":
          el.style.transform = `translateY(${distance}) scale(${scale})`;
          break;
        case "left":
          el.style.transform = `translateX(-${distance}) scale(${scale})`;
          break;
        case "right":
          el.style.transform = `translateX(${distance}) scale(${scale})`;
          break;
      }

      // Reveal if already in view or observe for scroll
      if (isInViewport(el)) {
        requestAnimationFrame(() => {
          el.style.transitionDuration = `${el.dataset.duration || "600"}ms`;
          el.style.transitionDelay = `${el.dataset.delay || "0"}ms`;
          el.style.opacity = "1";
          el.style.transform = "translate(0,0) scale(1)";
          el.classList.add("is-visible");
        });
      } else {
        revealObserver.observe(el);
      }
    });
  });
});


document.addEventListener('DOMContentLoaded', () => {
const topbar = document.getElementById('topbar1');
const links = document.getElementById('sidebar-links');

let offset = topbar.getBoundingClientRect().bottom;
if (offset < 0) offset = 0;
links.style.transform = `translateY(${offset}px)`;

window.addEventListener('scroll', () => {
  let offset = topbar.getBoundingClientRect().bottom;
  if (offset < 0) offset = 0;
    links.style.transform = `translateY(${offset}px)`;
  });
});



    
document.addEventListener('DOMContentLoaded', function() {
    // Sidebar toggle
    const hamburger = document.querySelector('.hamburger-svg');
    const x = document.querySelector('.hamburger-x-svg');
    const sidebar = document.querySelector('.sidebar');
    const bars = document.querySelector('.hamburger-menu');

    let scrollPosition = 0;


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
            x.classList.toggle('active');
            sidebar.classList.toggle('active');
            overlay.classList.toggle('active');   // Show/hide blackout


            if (sidebar.classList.contains('active')) {
                disableScroll();
            } else {
                enableScroll();
            }
        });

        x.addEventListener('click', function() {
          sidebar.classList.remove('active');
            hamburger.classList.remove('active');
            x.classList.remove('active');
            overlay.classList.remove('active');
            enableScroll();
            });

        // Close sidebar when clicking the blackout
        overlay.addEventListener('click', function() {
            sidebar.classList.remove('active');
            hamburger.classList.remove('active');
            x.classList.remove('active');
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


    // arrow functions
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

    // Set initial active thumbnail
    if (thumbnails.length > 0) {
        thumbnails[0].classList.add('thumbnail-active');
    }
});