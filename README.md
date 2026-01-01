# Gameshow Web App

A real-time gameshow application with a control panel for the host and a main display for the audience.

## Structure

```
Gameshow/
├── index.html              # Main display (for projector/audience)
├── control.html            # Control panel (for host's phone)
├── images/
│   ├── original/          # Original images (1.jpg, 2.jpg, etc.)
│   └── altered/           # Altered versions (1.jpg, 2.jpg, etc.)
├── gameshow-realtime-communication.md
└── README.md
```

## How It Works

1. **Main Display** (index.html) - Shows images to the audience
2. **Control Panel** (control.html) - Host controls which image is shown
3. **Firebase** - Syncs state between control panel and display in real-time

## Setup Instructions

### Step 1: Add Your Images

1. Add your original images to `images/original/` folder
2. Name them: `1.jpg`, `2.jpg`, `3.jpg`, etc.
3. Add altered versions to `images/altered/` folder with the same names
4. Supported formats: `.jpg`, `.jpeg`, `.png`

### Step 2: Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Create a new project
3. Enable **Realtime Database**
4. Set database rules:
   ```json
   {
     "rules": {
       "gameState": {
         ".read": true,
         ".write": true
       }
     }
   }
   ```
5. Get your config from Project Settings > General > Your apps > Web app

### Step 3: Add Firebase Config

In **both** `index.html` and `control.html`:

1. Find the `TODO: Add Firebase imports` section
2. Uncomment the import lines
3. Find the `TODO: Add your Firebase configuration` section
4. Uncomment and fill in your Firebase config:
   ```javascript
   const firebaseConfig = {
       apiKey: "YOUR_API_KEY",
       authDomain: "YOUR_PROJECT.firebaseapp.com",
       databaseURL: "https://YOUR_PROJECT.firebaseio.com",
       projectId: "YOUR_PROJECT_ID",
       storageBucket: "YOUR_PROJECT.appspot.com",
       messagingSenderId: "YOUR_SENDER_ID",
       appId: "YOUR_APP_ID"
   };
   ```
5. Uncomment the Firebase initialization code
6. Uncomment the `onValue` listeners in both files

### Step 4: Test Locally

```bash
cd ~/Desktop/Gameshow
python3 -m http.server 8000
```

Open:
- Main display: http://localhost:8000/index.html
- Control panel: http://localhost:8000/control.html

### Step 5: Deploy to GitHub Pages

1. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Add gameshow app with Firebase"
   git push origin main
   ```

2. Enable GitHub Pages:
   - Go to your repo on GitHub
   - Settings > Pages
   - Source: Deploy from branch `main`
   - Folder: `/ (root)`
   - Save

3. Access your app:
   - Main display: `https://yourusername.github.io/Gameshow/`
   - Control panel: `https://yourusername.github.io/Gameshow/control.html`

## Usage

1. Open **index.html** on the projector/TV
2. Open **control.html** on your phone
3. Use the control panel to:
   - **Next Image** - Advance to the next image (shows original)
   - **Reveal Altered Version** - Show the altered version
   - **Reset Game** - Start over from the beginning

## Customization

### Styling
- Edit the `<style>` sections in both HTML files
- Customize colors, fonts, animations, transitions
- Add background effects, borders, shadows

### Firebase Security (Optional)
See `gameshow-realtime-communication.md` for security options:
- Firebase Authentication
- Security rules with secret paths
- Hard-to-guess control panel URLs

## Testing Without Firebase

Both files work without Firebase for local testing:

**index.html**: Open browser console and run:
```javascript
testDisplay(1, false);  // Show image 1, original
testDisplay(1, true);   // Show image 1, altered
```

**control.html**: Buttons will log state changes to console

## Troubleshooting

- **Images not loading**: Check file paths and names match exactly
- **State not syncing**: Verify Firebase config is correct in both files
- **Control panel not connecting**: Check Firebase database rules allow writes
- **CORS errors**: Use `python3 -m http.server` for local testing

## Next Steps

1. Add your images to the folders
2. Style the HTML files to your liking
3. Set up Firebase and add your config
4. Test locally
5. Deploy to GitHub Pages
6. Bookmark the control panel URL on your phone
