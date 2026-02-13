# PWA Installation Guide

## For Users

### Installing on Android

1. Open the Frappe site in Chrome browser
2. Wait for the "Install Task Manager app" prompt to appear
3. Tap "Install" button
4. The app will be added to your home screen
5. Open the app from your home screen like any native app

**Alternative method:**
1. Open the site in Chrome
2. Tap the three-dot menu (⋮)
3. Select "Install app" or "Add to Home screen"
4. Follow the prompts

### Installing on iOS (iPhone/iPad)

1. Open the Frappe site in Safari browser
2. Tap the Share button (box with arrow pointing up)
3. Scroll down and tap "Add to Home Screen"
4. Tap "Add" in the top right corner
5. The app icon will appear on your home screen

### Installing on Desktop (Chrome/Edge)

1. Open the Frappe site in Chrome or Edge
2. Look for the install icon (⊕) in the address bar
3. Click it and select "Install"
4. The app will open in its own window
5. Find it in your Start menu or Applications folder

## Features When Installed as PWA

✅ **Offline Access**: View cached data even without internet
✅ **App Icon**: Access from home screen like native apps
✅ **Full Screen**: No browser UI, more screen space
✅ **Fast Load**: Cached resources load instantly
✅ **Push Notifications**: Get updates even when app is closed
✅ **Background Sync**: Changes sync when connection returns

## For Developers

### Testing PWA Features Locally

1. PWA requires HTTPS. For local testing:
   ```bash
   # Use ngrok or similar tunnel
   ngrok http 8000
   ```

2. Check PWA readiness in Chrome DevTools:
   - Open DevTools (F12)
   - Go to "Application" tab
   - Click "Manifest" to verify manifest.json
   - Click "Service Workers" to check registration

3. Test offline functionality:
   - Open DevTools
   - Go to "Application" > "Service Workers"
   - Check "Offline" checkbox
   - Try navigating the app

### Generating PWA Icons

Use one of these tools to generate all required icon sizes:

- [PWA Builder](https://www.pwabuilder.com/imageGenerator)
- [RealFaviconGenerator](https://realfavicongenerator.net/)

Required sizes:
- 72x72, 96x96, 128x128, 144x144, 152x152, 192x192, 384x384, 512x512

Place all icons in:
```
task_manager/public/images/
```

### Customizing PWA Settings

Edit `task_manager/hooks.py`:

```python
pwa_manifest = {
    "name": "Your App Name",
    "short_name": "App",
    "theme_color": "#your-color",
    # ... other settings
}
```

### Service Worker Customization

Edit `task_manager/public/js/service-worker.js` to:
- Add more URLs to cache
- Implement custom caching strategies
- Add background sync logic
- Handle push notifications

## Troubleshooting

### App doesn't show install prompt

- PWA requires HTTPS (except localhost)
- Check browser console for errors
- Verify manifest.json is accessible
- Ensure service worker registered successfully

### Offline mode not working

- Check if service worker is registered
- Verify cache is populated
- Check browser console for SW errors
- Try clearing cache and re-registering

### Icons not showing

- Ensure all icon files exist in public/images/
- Check paths in manifest.json
- Clear browser cache
- Verify file permissions

## Browser Support

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| Install | ✅ | ✅ | ✅* | ✅ |
| Offline | ✅ | ✅ | ✅ | ✅ |
| Push | ✅ | ✅ | ❌ | ✅ |

*Safari uses "Add to Home Screen" instead of traditional install prompt
