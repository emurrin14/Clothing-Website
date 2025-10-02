document.addEventListener('DOMContentLoaded', function() {
    // Sidebar toggle
    const hamburger = document.querySelector('.hamburger-menu');
    const sidebar = document.querySelector('.sidebar');

    if (hamburger && sidebar) {
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            sidebar.classList.toggle('active');
        });
    }

    // Profile dropdown toggle
    const profileMenuButton = document.getElementById('profile-menu-button');
    const profileDropdown = document.getElementById('profile-dropdown');

    if (profileMenuButton && profileDropdown) {
        profileMenuButton.addEventListener('click', function(event) {
            event.stopPropagation(); // Prevent the window click event from firing
            console.log("should be showing");
            profileDropdown.classList.toggle('show');
        });

        // Close the dropdown if the user clicks outside of it
        window.addEventListener('click', function(event) {
            if (!profileMenuButton.contains(event.target) && !profileDropdown.contains(event.target)) {
                console.log("should be hiding"); 
                profileDropdown.classList.remove('show');
            }
        });
    }
});