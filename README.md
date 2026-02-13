# Task Manager - Frappe Mobile PWA App

<div align="center">

![Frappe](https://img.shields.io/badge/Frappe-Framework-blue)
![PWA](https://img.shields.io/badge/PWA-Enabled-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Mobile](https://img.shields.io/badge/Mobile-Friendly-orange)

A production-ready Progressive Web App (PWA) for task management built on Frappe Framework. Install on mobile devices like a native app with offline support!

[Live Demo](#) • [Documentation](#documentation) • [Installation](#installation) • [Contributing](#contributing)

</div>

---

## 📱 Overview

**Task Manager** is a mobile-first PWA that brings the power of Frappe Framework to your pocket. Create customers, manage projects, track tasks, and collaborate with your team - all from a mobile-friendly interface that works offline.

### ✨ Key Features

- 📲 **Install as Mobile App** - Add to home screen on Android, iOS, and desktop
- 📴 **Offline Support** - Service worker caching for offline functionality
- 🔄 **Background Sync** - Changes sync automatically when connection returns
- 🎨 **Mobile-Optimized UI** - Touch-friendly interface with responsive design
- ⚡ **Fast & Lightweight** - Optimized performance with smart caching
- 🔔 **Push Notifications** - Stay updated with real-time notifications (configurable)
- 🎯 **Quick Actions** - One-tap shortcuts for common tasks
- 🌙 **Modern Design** - Clean, intuitive interface

---

## 🏗️ Architecture

### Doctypes (4)

```
Customer (Master)
    ↓
Project (Document)
    ↓
Task (Document)
    ↓
Task Comment (Child Table)
```

#### 1. 👥 Customer
- Customer information management
- Contact details (email, phone)
- Company and address information
- Status tracking (Active/Inactive)

#### 2. 📊 Project
- Project management with customer linkage
- Timeline tracking (start, expected end, actual end)
- Status workflow (Open → In Progress → Completed/Cancelled)
- Progress percentage (auto-calculated from tasks)
- Priority levels (Low, Medium, High, Urgent)

#### 3. ✅ Task
- Detailed task management
- Assignment to users
- Status tracking (Open → Working → Pending Review → Completed/Cancelled)
- Priority management
- Time estimation and tracking
- Progress monitoring
- Linked to projects and customers

#### 4. 💬 Task Comment
- Inline comments on tasks
- User attribution and timestamps
- Collaboration and discussion tracking

---

## 🚀 Installation

### Prerequisites

- Frappe Framework (v14+)
- Python 3.10+
- Node.js 18+
- MariaDB or PostgreSQL

### Quick Install

```bash
# Navigate to your frappe-bench directory
cd frappe-bench

# Get the app from GitHub
bench get-app https://github.com/sagarmemane135/test-frappe-mobile-app.git

# Install on your site
bench --site your-site.local install-app task_manager

# Run migrations
bench --site your-site.local migrate

# Build assets
bench build --app task_manager

# Clear cache and restart
bench --site your-site.local clear-cache
bench restart
```

### PWA Setup (Important!)

For PWA functionality, you need to add app icons:

1. **Generate Icons**: Use [PWA Builder](https://www.pwabuilder.com/imageGenerator) to generate all sizes
2. **Place Icons** in `task_manager/public/images/`:
   - icon-72x72.png
   - icon-96x96.png
   - icon-128x128.png
   - icon-144x144.png
   - icon-152x152.png
   - icon-192x192.png
   - icon-384x384.png
   - icon-512x512.png
   - badge-72x72.png

3. **Rebuild Assets**:
   ```bash
   bench build --app task_manager --force
   bench restart
   ```

---

## 📲 Installing as PWA

### Android (Chrome)
1. Open your Frappe site in Chrome browser
2. Tap the "Install Task Manager app" prompt that appears
3. Or tap the menu (⋮) → "Install app"
4. App appears on your home screen!

### iOS (Safari)
1. Open your Frappe site in Safari
2. Tap the Share button (□↑)
3. Scroll down and tap "Add to Home Screen"
4. Tap "Add" in the top right
5. App appears on your home screen!

### Desktop (Chrome/Edge)
1. Look for the install icon (⊕) in the address bar
2. Click it and select "Install"
3. App opens in its own window
4. Access from Start menu or Applications

> **Note**: PWA requires HTTPS in production. For local testing, use [ngrok](https://ngrok.com/):
> ```bash
> ngrok http 8000
> ```

---

## 📖 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started in 5 minutes
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment guide
- **[PWA_INSTALLATION.md](PWA_INSTALLATION.md)** - Detailed PWA setup and troubleshooting

---

## 🎯 Usage

### Basic Workflow

1. **Create Customers** → Add customer details and contact information
2. **Create Projects** → Link projects to customers, set timelines
3. **Create Tasks** → Add tasks to projects, assign to team members
4. **Add Comments** → Collaborate through task comments
5. **Track Progress** → Monitor task and project completion

### Mobile Quick Actions

- **Start Working** - Begin work on a task with one tap
- **Mark Complete** - Instantly complete tasks
- **Add Comment** - Quick collaboration with inline comments
- **View Progress** - Visual indicators for completion status

---

## 🎨 Customization

### Change Theme Colors

Edit `task_manager/public/css/task_manager.css`:

```css
:root {
    --primary-color: #2490ef;   /* Your brand color */
    --secondary-color: #4ecb73; /* Success color */
    --danger-color: #f56b6b;    /* Error color */
    --warning-color: #f59d5f;   /* Warning color */
}
```

### Modify App Name & Branding

Edit `task_manager/hooks.py`:

```python
app_title = "Your App Name"
app_description = "Your app description"

pwa_manifest = {
    "name": "Your App Name",
    "short_name": "YourApp",
    "theme_color": "#your-color",
    # ...
}
```

### Add Custom Fields

Use Frappe's built-in Customize Form tool:
1. Go to **Customize Form**
2. Select doctype (Task, Project, Customer, etc.)
3. Add your custom fields
4. Save and refresh

---

## 🛠️ Development

### Project Structure

```
test_frappe_app/
├── task_manager/                    # Main app directory
│   ├── config/                      # Desktop & module config
│   ├── public/                      # Static assets
│   │   ├── css/                     # Stylesheets
│   │   ├── js/                      # JavaScript & Service Worker
│   │   ├── images/                  # PWA icons
│   │   └── manifest.json            # PWA manifest
│   ├── task_manager/                # App module
│   │   └── doctype/                 # Doctypes
│   │       ├── customer/
│   │       ├── project/
│   │       ├── task/
│   │       └── task_comment/
│   ├── templates/                   # Jinja templates
│   └── hooks.py                     # App hooks & configuration
├── setup.py                         # Python package setup
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

### Local Development

```bash
# Start development server
bench start

# Watch for changes
bench watch

# View logs
bench --site your-site.local console

# Run tests (when added)
bench --site your-site.local run-tests --app task_manager
```

---

## 🧪 Testing

### Test PWA Features

1. **Open DevTools** (F12)
2. **Application Tab**:
   - Check Manifest
   - Verify Service Worker registration
   - Test offline mode (Network tab → Offline)
3. **Lighthouse Audit**:
   - Run PWA audit
   - Check performance scores

### Test on Real Devices

- Use Chrome Remote Debugging for Android
- Use Safari Web Inspector for iOS
- Test install flow on both platforms

---

## 🚢 Production Deployment

### Enable HTTPS (Required for PWA)

```bash
# Using Let's Encrypt
sudo bench setup lets-encrypt your-site.com

# Or configure your reverse proxy (nginx/Apache)
```

### Setup Production Services

```bash
# Configure nginx and supervisor
bench setup nginx
bench setup supervisor

# Reload services
sudo supervisorctl reload
sudo service nginx reload
```

### Optimize for Production

```bash
# Build with minification
bench build --app task_manager --production

# Enable caching in nginx config
# Add gzip compression
# Set proper cache headers
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed production setup.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow Frappe's coding standards
- Add docstrings to Python functions
- Comment complex JavaScript logic
- Test on mobile devices before submitting
- Update documentation for new features

---

## 🐛 Troubleshooting

### Service Worker Not Registering

```bash
bench --site your-site.local clear-cache
bench build --app task_manager --force
bench restart
```

### PWA Not Installable

- Ensure HTTPS is enabled (or use ngrok for testing)
- Check manifest.json is accessible at `/assets/task_manager/manifest.json`
- Verify all required icons exist
- Check browser console for errors

### Changes Not Reflecting

```bash
bench build --app task_manager
bench --site your-site.local clear-cache
# Hard refresh browser: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
```

### Offline Mode Not Working

- Check Service Worker registration in DevTools
- Verify cache is populated
- Check Network tab for failed requests
- Review Service Worker console for errors

---

## 📊 Browser Support

| Browser | Version | PWA Install | Offline | Push Notifications |
|---------|---------|-------------|---------|-------------------|
| Chrome (Android) | 80+ | ✅ | ✅ | ✅ |
| Safari (iOS) | 11.3+ | ✅* | ✅ | ❌ |
| Chrome (Desktop) | 80+ | ✅ | ✅ | ✅ |
| Edge | 80+ | ✅ | ✅ | ✅ |
| Firefox | 90+ | ✅ | ✅ | ✅ |

*iOS uses "Add to Home Screen" instead of traditional install prompt

---

## 📄 License

This project is licensed under the MIT License - see the [license.txt](license.txt) file for details.

```
MIT License

Copyright (c) 2026 Sagar Memane

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- Built with [Frappe Framework](https://frappeframework.com/)
- PWA guidance from [web.dev](https://web.dev/progressive-web-apps/)
- Icons can be generated at [PWA Builder](https://www.pwabuilder.com/)
- Inspired by Frappe HRMS mobile experience

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/sagarmemane135/test-frappe-mobile-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sagarmemane135/test-frappe-mobile-app/discussions)
- **Email**: your.email@example.com

---

## 🗺️ Roadmap

- [ ] Add Kanban board view for tasks
- [ ] Implement time tracking with timer
- [ ] Add file attachments to tasks
- [ ] Create dashboard with analytics
- [ ] Add recurring tasks functionality
- [ ] Integrate calendar view
- [ ] Add team collaboration features
- [ ] Implement real-time notifications
- [ ] Add dark mode support
- [ ] Create mobile-specific shortcuts

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ using Frappe Framework

[Report Bug](https://github.com/sagarmemane135/test-frappe-mobile-app/issues) • [Request Feature](https://github.com/sagarmemane135/test-frappe-mobile-app/issues)

</div>
