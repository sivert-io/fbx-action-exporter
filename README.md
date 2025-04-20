# 🛠️ FBX Action Exporter for Blender

![Add-on Interface Preview](preview.png)

**FBX Action Exporter** is a Blender add-on that streamlines the process of exporting all animation actions (NLA tracks) as individual `.fbx` files.

It's especially useful for game developers and animators working with engines like **Roblox**, **Unreal Engine**, **Unity**, and more.

---

## 📋 Requirements

- **Blender 4.0 or higher**
- Uses Blender's built-in FBX exporter

---

## ✨ Features

- **Batch Export Animations**  
  Automatically exports each action as a separate `.fbx` file.

- **Customizable Export Settings**  
  Adjust transform, geometry, and armature options to fit your project's needs.

- **User-Friendly Interface**  
  Integrates seamlessly into Blender's UI with collapsible panels.

- **Game Engine Compatibility**  
  Works great with Roblox, Unreal Engine, Unity, and others.

---

## 🎮 Use Cases

- **Roblox**: Export custom character animations with proper scaling and orientation.
- **Unreal Engine**: Seamlessly import animations into UE4/UE5.
- **Unity**: Easily generate `.fbx` files for character rigs.
- **Any Game Engine**: Quickly manage and export animation libraries in one click.

---

## 📦 Installation

### 🧩 From GitHub Releases

1. Go to the [Releases page](https://github.com/sivert-io/fbx-action-exporter/releases).
2. Download the latest `fbx_action_exporter.py` file.
3. In Blender, open `Edit > Preferences > Add-ons > Install...`.
4. Select the downloaded `.py` file and install it.
5. Enable the add-on from the list.
6. Find it in the sidebar under `View3D > Armature Tools`.

---

## 🚀 Getting Started

1. Select your armature in the 3D view.
2. Set the export path in the add-on panel.
3. Configure your export settings.
4. Click **Export All Actions** to generate individual `.fbx` files for each protected action.

> 💡 Make sure your actions have **Fake User** enabled so they get saved with the file.

---

## 📄 License

MIT License

Copyright (c) 2025 Sivert Gullberg Hansen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
