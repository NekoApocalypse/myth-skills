# JRJ Market Heatmap (大盘云图)

## 📌 Usage & Context
Fetch a visual representation of the Chinese stock market's daily performance (A-shares) using the JRJ "大盘云图" (Market Cloud Map). 

Use this skill when you need to see the broad market heat, sector rotation, or are explicitly asked for the 大盘云图.

## 🛠️ Execution Steps

To get a perfectly cropped screenshot of the heatmap canvas (without headers, legends, or extra whitespace), use this exact sequence of commands:

1. **Navigate and Resize**: 
First, navigate to the URL and force the viewport to match the canvas dimensions exactly (`1100x888`). Wait a few seconds for the canvas data to load.
```json
{
  "action": "act",
  "kind": "resize",
  "targetId": "...",
  "request": {
    "kind": "resize",
    "width": 1100,
    "height": 888
  }
}
```

2. **Isolate the Canvas via JS Evaluation**:
Run this script to strip away all headers, footers, and margins, placing the canvas exactly at `(0, 0)`.
```json
{
  "action": "act",
  "kind": "evaluate",
  "targetId": "...",
  "request": {
    "kind": "evaluate",
    "fn": "() => { const canvas = document.querySelector('canvas'); if(!canvas) return 'no canvas'; document.body.innerHTML = ''; document.body.style.margin = '0'; document.body.style.padding = '0'; document.body.style.background = '#fff'; canvas.style.position = 'absolute'; canvas.style.top = '0px'; canvas.style.left = '0px'; document.body.appendChild(canvas); return 'ok'; }"
  }
}
```

3. **Take the Final Screenshot**:
Since the viewport is now exactly `1100x888` and only contains the canvas, the screenshot will be perfectly cropped to the heatmap data.
```json
{
  "action": "screenshot",
  "targetId": "...",
  "delayMs": 500
}
```

Once the `browser` tool returns the image attachment (media URL), send the screenshot back to the user or analyze the image using the `image` tool if requested.