// Task Manager App JavaScript

frappe.provide("task_manager");

// Initialize PWA features
frappe.ready(function() {
    task_manager.init_pwa();
    task_manager.init_offline_detection();
});

task_manager.init_pwa = function() {
    // Register service worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/assets/task_manager/js/service-worker.js')
            .then(function(registration) {
                console.log('Service Worker registered:', registration.scope);
            })
            .catch(function(error) {
                console.log('Service Worker registration failed:', error);
            });
    }

    // Handle install prompt
    let deferredPrompt;
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        
        // Show custom install prompt
        const installPrompt = document.createElement('div');
        installPrompt.className = 'pwa-install-prompt show';
        installPrompt.innerHTML = `
            <span>Install Task Manager app</span>
            <button class="btn btn-sm btn-primary" style="margin-left: 15px;">Install</button>
            <button class="btn btn-sm btn-secondary" style="margin-left: 5px;">Later</button>
        `;
        document.body.appendChild(installPrompt);
        
        // Handle install button
        installPrompt.querySelector('.btn-primary').addEventListener('click', async () => {
            installPrompt.classList.remove('show');
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            console.log(`User response: ${outcome}`);
            deferredPrompt = null;
            installPrompt.remove();
        });
        
        // Handle later button
        installPrompt.querySelector('.btn-secondary').addEventListener('click', () => {
            installPrompt.classList.remove('show');
            setTimeout(() => installPrompt.remove(), 300);
        });
    });
};

task_manager.init_offline_detection = function() {
    // Create offline indicator
    const offlineIndicator = document.createElement('div');
    offlineIndicator.className = 'offline-indicator';
    offlineIndicator.innerHTML = '📴 You are offline. Some features may not be available.';
    document.body.appendChild(offlineIndicator);
    
    // Update online/offline status
    const updateOnlineStatus = () => {
        if (navigator.onLine) {
            offlineIndicator.classList.remove('show');
        } else {
            offlineIndicator.classList.add('show');
        }
    };
    
    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);
    updateOnlineStatus();
};

// Enhance mobile experience
frappe.ui.form.on('Task', {
    refresh: function(frm) {
        // Add mobile-friendly buttons
        if (frm.doc.status === 'Open') {
            frm.add_custom_button(__('Mark Complete'), function() {
                frm.set_value('status', 'Completed');
                frm.save();
            }).addClass('btn-success');
        }
    }
});
