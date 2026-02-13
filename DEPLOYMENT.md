# Deployment Guide for Task Manager

## Prerequisites

- Frappe Bench installed
- Python 3.10+
- Node.js 18+
- MariaDB/PostgreSQL

## Installation Steps

### 1. Get the App

```bash
# Navigate to your bench directory
cd frappe-bench

# Get the app from repository (or local path)
bench get-app task_manager /path/to/task_manager

# Or from git
bench get-app https://github.com/yourusername/task_manager.git
```

### 2. Install on Site

```bash
# Install app on your site
bench --site your-site.local install-app task_manager

# Migrate the site
bench --site your-site.local migrate
```

### 3. Build Assets

```bash
# Build frontend assets
bench build --app task_manager

# Or build all
bench build
```

### 4. Restart Services

```bash
# Clear cache
bench --site your-site.local clear-cache

# Restart bench
bench restart
```

## PWA Configuration

### 1. Enable HTTPS

PWA requires HTTPS in production. Configure SSL:

```bash
# Using Let's Encrypt with Certbot
sudo bench setup lets-encrypt your-site.local
```

Or configure your reverse proxy (nginx/Apache) for HTTPS.

### 2. Add PWA Icons

Generate and place icons in:
```
task_manager/public/images/icon-*.png
```

Use [PWA Builder](https://www.pwabuilder.com/imageGenerator) to generate all sizes from one image.

### 3. Verify PWA Setup

Visit your site and:
1. Open Chrome DevTools (F12)
2. Go to "Application" tab
3. Check "Manifest" - should show Task Manager details
4. Check "Service Workers" - should show registered worker
5. Lighthouse audit should show PWA score

## Production Deployment

### Using Supervisor

```bash
# Setup production config
bench setup supervisor
bench setup nginx

# Reload services
sudo supervisorctl reload
sudo service nginx reload
```

### Using Docker

```dockerfile
# Dockerfile
FROM frappe/erpnext:latest

# Copy app
COPY task_manager /home/frappe/frappe-bench/apps/task_manager

# Install app
RUN cd /home/frappe/frappe-bench && \
    bench get-app task_manager && \
    bench build --app task_manager

# Expose port
EXPOSE 8000
```

### Using Frappe Cloud

1. Push code to Git repository
2. Add repository in Frappe Cloud dashboard
3. Deploy to your site
4. App will be automatically built and installed

## Configuration

### Site Config

Add to `site_config.json`:

```json
{
  "enable_pwa": true,
  "pwa_manifest_path": "/assets/task_manager/manifest.json",
  "service_worker_path": "/assets/task_manager/js/service-worker.js"
}
```

### Hooks Configuration

The app's PWA settings are in `task_manager/hooks.py`:

```python
# PWA Configuration
pwa_enabled = True
service_worker_path = "/assets/task_manager/js/service-worker.js"
pwa_manifest = { ... }
```

## Mobile Testing

### Android Testing

```bash
# Enable remote debugging
# Connect Android device via USB
# Open chrome://inspect in Chrome
# Select your device and site
```

### iOS Testing

```bash
# Use Safari Web Inspector
# Enable "Web Inspector" in iOS Settings
# Connect device and open Safari > Develop menu
```

### Responsive Testing

```bash
# Use Chrome DevTools device emulation
# Test various screen sizes:
# - Mobile: 375x667 (iPhone SE)
# - Tablet: 768x1024 (iPad)
# - Desktop: 1920x1080
```

## Performance Optimization

### 1. Enable Caching

```python
# In hooks.py, add:
website_route_rules = [
    {"from_route": "/assets/task_manager/<path:file>", "to_route": "/assets/task_manager/<file>"},
]
```

### 2. Minify Assets

```bash
# Build with minification
bench build --app task_manager --production
```

### 3. Enable Compression

In nginx config:
```nginx
gzip on;
gzip_types text/css application/javascript application/json;
```

## Monitoring

### Check Service Worker Status

```javascript
// In browser console
navigator.serviceWorker.getRegistrations().then(registrations => {
    console.log('Registered SWs:', registrations);
});
```

### Check Cache Status

```javascript
// In browser console
caches.keys().then(keys => {
    console.log('Cache keys:', keys);
});
```

### Monitor Performance

Use Lighthouse in Chrome DevTools:
- Performance score
- PWA score
- Accessibility score
- SEO score

## Troubleshooting

### Service Worker Not Registering

```bash
# Clear all caches
bench --site your-site.local clear-cache
bench clear-cache

# Rebuild assets
bench build --app task_manager --force

# Check console for errors
```

### PWA Not Installable

1. Verify HTTPS is enabled
2. Check manifest.json is accessible
3. Ensure all required icons exist
4. Check browser console for errors

### Offline Mode Not Working

1. Verify service worker is registered
2. Check network tab in DevTools
3. Verify URLs are being cached
4. Check SW console for errors

## Updates and Maintenance

### Updating the App

```bash
# Pull latest changes
cd apps/task_manager
git pull

# Update site
cd ../..
bench --site your-site.local migrate
bench build --app task_manager

# Clear cache
bench --site your-site.local clear-cache
bench restart
```

### Version Management

Update version in `task_manager/__init__.py`:
```python
__version__ = '0.0.2'
```

Then:
```bash
bench --site your-site.local migrate
```

## Security

### Content Security Policy

Add to nginx config:
```nginx
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';";
```

### HTTPS Enforcement

```nginx
# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name your-site.local;
    return 301 https://$server_name$request_uri;
}
```

## Support

For issues:
1. Check browser console
2. Check bench logs: `bench --site your-site.local console`
3. Check error logs: `tail -f logs/*.log`
4. Report issues on GitHub
