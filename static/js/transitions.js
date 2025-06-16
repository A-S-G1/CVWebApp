// my_website_project/static/js/transitions.js

document.addEventListener('DOMContentLoaded', () => {
    // Console logs for debugging (can be removed in production)
    console.log('DOM Content Loaded - transitions.js is running!');
    
    const contentWrapper = document.getElementById('content-wrapper');
    console.log('Content Wrapper:', contentWrapper);
    
    const navLinks = document.querySelectorAll('.nav-link');
    console.log('Nav Links found:', navLinks.length);
    
    // Select all sections within the content wrapper that need to animate
    // Ensures animation applies to the main content blocks on each page
    const animatableSections = contentWrapper ? contentWrapper.querySelectorAll('section') : [];
    console.log('Animatable Sections found:', animatableSections.length, animatableSections);

    // Function to animate sections in on page load/navigation
    function animateSectionsIn() {
        console.log('Attempting to animate sections in...');
        if (animatableSections.length > 0) {
            animatableSections.forEach((section, index) => {
                // Remove any 'exit' classes that might be lingering from a previous transition
                section.classList.remove('page-transition-exit', 'page-transition-exit-active');

                // Introduce a staggered delay for a nicer visual effect
                setTimeout(() => {
                    // Remove the starting invisibility (opacity-0) and transform (translate-y-4) classes
                    // This triggers the CSS transition defined on the section itself
                    section.classList.remove('opacity-0', 'translate-y-4');
                    console.log(`Section ${index} animated in.`);
                }, 100 + (index * 100)); // Delay increases for each subsequent section
            });
        } else {
            console.log('No animatable sections found.');
        }
    }

    // Trigger animation for sections when the initial page content has loaded
    animateSectionsIn();

    // Handle navigation clicks for custom transitions
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            const targetUrl = link.getAttribute('href');

            // Prevent default navigation to allow the "exit" transition to complete
            event.preventDefault();

            if (contentWrapper) {
                // Apply "exit" transition to all animatable sections
                animatableSections.forEach((section, index) => {
                    // Re-apply the initial state classes (opacity-0, translate-y-4) for the exit animation
                    // This makes the section fade out and slide away
                    setTimeout(() => {
                        section.classList.add('opacity-0', 'translate-y-4');
                        // If you had specific exit animations, you might add 'page-transition-exit' here
                    }, index * 50); // Small stagger for exit animation
                });

                // After all transitions complete, navigate to the new page
                // The duration here should match or be slightly longer than your CSS transition duration
                setTimeout(() => {
                    window.location.href = targetUrl;
                }, 500); // Matches the longest CSS transition duration (0.5s)
            } else {
                // Fallback: If contentWrapper is not found, just navigate directly
                console.warn('Content wrapper not found for transition. Navigating directly.');
                window.location.href = targetUrl;
            }
        });
    });

    // Handle browser back/forward buttons (popstate event)
    window.addEventListener('popstate', () => {
        // When navigating back/forward, the browser loads the new content.
        // We then re-apply the entrance animation to the new content.
        animateSectionsIn();
    });
});
