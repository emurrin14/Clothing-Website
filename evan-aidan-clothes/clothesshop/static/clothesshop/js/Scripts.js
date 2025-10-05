document.addEventListener('DOMContentLoaded', function() {
    // Sidebar toggle
    const hamburger = document.querySelector('.hamburger-menu');
    const sidebar = document.querySelector('.sidebar');

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