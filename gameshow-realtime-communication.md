# Gameshow Web App - Real-Time Communication Guide

## Problem
Connect a **control panel** (your phone) with a **main display** (audience view) to advance slides remotely.

## Recommended Solution: Firebase Realtime Database

### Why Firebase?
- ✅ You already know it (IBA website experience)
- ✅ Works with GitHub Pages (static hosting)
- ✅ Real-time updates (~100ms latency)
- ✅ No server needed
- ✅ Free tier available
- ✅ Built-in authentication

---

## Architecture

```
Control Panel (phone) → Firebase Realtime DB → Main Display (projector)
    Press "Next"              State stored              Auto-updates
```

---

## Implementation Overview

### 1. Firebase Setup
```bash
# Add to both HTML files (in <head>)
<script src="https://www.gstatic.com/firebasejs/9.x.x/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.x.x/firebase-database.js"></script>
```

### 2. Control Panel (private.html)
```javascript
// Initialize Firebase
const firebaseConfig = { /* your config */ };
firebase.initializeApp(firebaseConfig);

// Button click handler
document.getElementById('nextBtn').addEventListener('click', () => {
    firebase.database().ref('gameState').set({
        imageIndex: currentIndex++,
        revealed: false,
        timestamp: Date.now()
    });
});

document.getElementById('revealBtn').addEventListener('click', () => {
    firebase.database().ref('gameState/revealed').set(true);
});
```

### 3. Main Display (index.html)
```javascript
// Listen for changes
firebase.database().ref('gameState').on('value', (snapshot) => {
    const state = snapshot.val();
    
    // Update displayed image
    displayImage(state.imageIndex, state.revealed);
});
```

---

## File Structure

```
your-repo/
├── index.html          # Public gameshow display
├── control.html        # Private control panel
├── images/
│   ├── original/
│   │   ├── 1.jpg
│   │   └── 2.jpg
│   └── altered/
│       ├── 1.jpg
│       └── 2.jpg
└── README.md
```

---

## Deployment Checklist

1. **Create Firebase project** at [console.firebase.google.com](https://console.firebase.google.com)
2. **Enable Realtime Database** in Firebase Console
3. **Set database rules** (allow read for all, write only for authenticated users)
4. **Add Firebase config** to both HTML files
5. **Push to GitHub** and enable GitHub Pages
6. **Bookmark control.html** URL on your phone

---

## Security

### Firebase Database Rules
```json
{
  "rules": {
    "gameState": {
      ".read": true,
      ".write": "auth != null"
    }
  }
}
```

### Control Panel Access
- Use Firebase Authentication (Google Sign-In)
- Or use Security Rules with a secret path
- Or make control.html URL hard to guess (e.g., `control-a8f3b9d2.html`)

---

## Alternative Solutions

| Solution | Pros | Cons |
|----------|------|------|
| **WebSockets** | Full control | Requires server, more complex |
| **Pusher/Ably** | Easy setup | Third-party dependency |
| **Polling** | Simple | Delays, inefficient |
| **Firebase** | ✅ Best fit | Requires Google account |

---

## Quick Start Commands

```bash
# Clone your repo
git clone <your-repo>

# Add Firebase config to both files
# Test locally
python3 -m http.server 8000

# Push and deploy
git add .
git commit -m "Add gameshow app"
git push origin main
```

---

## Next Steps
1. Create the two HTML files (display + control)
2. Set up Firebase project
3. Test locally before deploying
4. Deploy to GitHub Pages
