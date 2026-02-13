# Task Manager - Quick Start Guide

## 🎉 What You Got

A fully functional Frappe app with PWA (Progressive Web App) capabilities that can be installed on mobile devices like native apps!

### 📱 Features

✅ **4 Doctypes**: Customer, Project, Task, Task Comment
✅ **PWA Enabled**: Install on mobile (Android/iOS) and desktop
✅ **Offline Support**: Works without internet connection
✅ **Mobile Optimized**: Responsive design for all devices
✅ **Service Worker**: Background sync and caching
✅ **Push Notifications**: Ready for notifications (needs backend setup)

## 🚀 Installation

### Step 1: Add to Frappe Bench

```bash
# Navigate to your frappe-bench directory
cd frappe-bench

# Get the app (use full path to this folder)
bench get-app /path/to/test_frappe_app

# Or if in bench directory already, use relative path
bench get-app ../test_frappe_app
```

### Step 2: Install on Site

```bash
# Install the app on your site
bench --site your-site.local install-app task_manager

# Run database migrations
bench --site your-site.local migrate
```

### Step 3: Build Assets

```bash
# Build the app's assets
bench build --app task_manager

# Clear cache
bench --site your-site.local clear-cache

# Restart bench
bench restart
```

### Step 4: Setup PWA Icons (Important!)

The app needs icons to work as PWA. Generate icons:

1. Create a 512x512 PNG icon for your app
2. Use [PWA Builder](https://www.pwabuilder.com/imageGenerator) to generate all sizes
3. Place icons in: `task_manager/public/images/`
   - icon-72x72.png
   - icon-96x96.png
   - icon-128x128.png
   - icon-144x144.png
   - icon-152x152.png
   - icon-192x192.png
   - icon-384x384.png
   - icon-512x512.png

4. Rebuild: `bench build --app task_manager`

## 📲 Installing as PWA

### On Android:
1. Open site in Chrome
2. Tap "Install Task Manager app" prompt
3. Or use Chrome menu → "Install app"

### On iOS:
1. Open site in Safari
2. Tap Share → "Add to Home Screen"

### On Desktop:
1. Look for install icon (⊕) in address bar
2. Click and select "Install"

**Note**: PWA requires HTTPS in production. Use ngrok for local testing:
```bash
ngrok http 8000
```

## 📋 Doctypes Overview

### 1. Customer
- Manage customer information
- Contact details and address
- Linked to projects

### 2. Project
- Manage projects for customers
- Track timelines and progress
- Auto-calculate completion based on tasks

### 3. Task
- Individual tasks within projects
- Status tracking (Open, Working, Completed)
- Priority levels
- Time tracking
- Progress percentage

### 4. Task Comment
- Add comments to tasks
- Track who commented and when
- Collaboration features

## 🎯 Usage Flow

```
Customer → Project → Task → Task Comment
   ↓          ↓        ↓
 Many      Many    Many
Projects   Tasks  Comments
```

1. Create customers
2. Create projects for customers
3. Create tasks within projects
4. Add comments to tasks for collaboration

## 🔧 Configuration

App settings are in `task_manager/hooks.py`:

```python
# PWA Configuration
pwa_enabled = True
pwa_manifest = {
    "name": "Task Manager",
    "short_name": "TaskMgr",
    "theme_color": "#2490ef",
    # ...customize as needed
}
```

## 🧪 Testing

### Test in Browser
```bash
# Start bench
bench start

# Open in browser
http://localhost:8000

# Login and access Task Manager module
```

### Test PWA Features
1. Open Chrome DevTools (F12)
2. Go to "Application" tab
3. Check "Manifest" section
4. Check "Service Workers" section
5. Test offline mode

## 📚 Documentation Files

- **README.md**: Overview and features
- **DEPLOYMENT.md**: Full production deployment guide
- **PWA_INSTALLATION.md**: Detailed PWA setup and troubleshooting
- **license.txt**: MIT License

## 🛠️ Customization

### Change Colors
Edit `task_manager/public/css/task_manager.css`:
```css
:root {
    --primary-color: #2490ef;  /* Your primary color */
    --secondary-color: #4ecb73; /* Your secondary color */
}
```

### Add More Fields
Use Frappe's Customize Form tool:
1. Go to Customize Form
2. Select doctype (Task, Project, etc.)
3. Add/modify fields
4. Save

### Extend Functionality
Edit Python controllers:
- `task_manager/doctype/task/task.py`
- `task_manager/doctype/project/project.py`

Edit JavaScript controllers:
- `task_manager/doctype/task/task.js`
- `task_manager/doctype/project/project.js`

## 🌐 For Production

1. **Enable HTTPS**: PWA requires secure connection
   ```bash
   sudo bench setup lets-encrypt your-site.local
   ```

2. **Setup Nginx & Supervisor**:
   ```bash
   bench setup nginx
   bench setup supervisor
   sudo supervisorctl reload
   sudo service nginx reload
   ```

3. **Add PWA Icons**: Generate and place all required sizes

4. **Test**: Use Lighthouse audit in Chrome DevTools

## 🐛 Troubleshooting

### Service Worker not registering
```bash
bench --site your-site.local clear-cache
bench build --app task_manager --force
bench restart
```

### PWA not installable
- Ensure HTTPS is enabled (or use ngrok for testing)
- Check that manifest.json is accessible
- Verify icons exist
- Check browser console for errors

### Changes not reflecting
```bash
bench build --app task_manager
bench --site your-site.local clear-cache
# Hard refresh browser (Ctrl+Shift+R)
```

## 📞 Support

For issues:
1. Check browser console (F12)
2. Check Frappe logs: `bench --site your-site.local console`
3. Check error logs: `tail -f logs/web.error.log`

## 🎓 Next Steps

1. Install the app on your Frappe site
2. Generate and add PWA icons
3. Create sample customers and projects
4. Test on mobile device
5. Install as PWA
6. Customize colors and branding
7. Deploy to production with HTTPS

## 🎨 Customization Ideas

- Add file attachments to tasks
- Integrate with email notifications
- Add time tracking with timer
- Create dashboards and reports
- Add Kanban board view
- Integrate with calendar
- Add recurring tasks
- Team collaboration features

---

**Enjoy your new mobile-friendly Task Manager app! 📱✨**
