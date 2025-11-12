# 🎨 HiDream AI Text-to-Image Generator with Python

> Transform text into stunning high-quality images with HiDream AI I1

<p align="center">
 <img src="https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-cover.jpg" alt="HiDream AI I1 Cover" width="100%">
</p>

---

<div align="center">

[![python](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Wiro.ai](https://img.shields.io/badge/Powered%20by-Wiro.ai-brightgreen)](https://wiro.ai)

</div>

---

## ✨ Features

- ✨ **High-Quality Image Generation** - Create detailed scenes with diverse artistic styles
- ✨ **Multiple Model Variants** - Choose between Fast, Dev, or Full versions for different needs
- ✨ **Controlled Output** - Fine-tune results with Guidance Scale, Flow Shift, and Steps
- ✨ **Customizable Parameters** - Set prompt, negative prompt, dimensions, samples, seed, and more
- ✨ **Seamless Integration** - Easy-to-use Python client with built-in polling and HMAC authentication

## 🛠️ Operations

1. **Go to [wiro.ai](https://wiro.ai)** and sign up for a free account
2. **Create a new project** at [wiro.ai/panel/project/new](https://wiro.ai/panel/project/new)
3. **Copy your credentials** from the project dashboard:
 - API Key (your public key)
 - API Secret (your private secret)
4. **Add to your project** using the exact format below:

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment file and update credentials
cp .env.example .env
# Edit .env with your Wiro credentials

## 📚 Resources

<div align="center">

<img src="https://wiro.ai/images/illustrations/koala-404.png" alt="Wiro Koala Mascot" height="100">

### Learn More

📖 [**wiro/text-to-image-hidreamai-i1 Model**](https://wiro.ai/models/wiro/text-to-image-hidreamai-i1)
📋 [**API Documentation**](https://wiro.ai/models/wiro/text-to-image-hidreamai-i1/llms-full.txt)
👨‍💻 [**API Samples (PYTHON)**](https://wiro.ai/models/wiro/text-to-image-hidreamai-i1#apisamples-python)
🌐 [**Wiro Example Projects**](https://wiro.ai/docs/example-projects)

</div>

## 🧠 Compatibility

This project requires Python 3.8 or higher and is compatible with all operating systems that support Python.

## 📁 Folder Structure

project-root/
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── .gitignore # Git ignore patterns
├── main.py # Main application entry point
├── wiro_client.py # Wiro API client with polling
└── examples/
 └── basic.py # Basic usage example

## 📦 Installation

Install required packages:

```bash
pip install -r requirements.txt

Set up environment variables:

```bash
# Copy and update credentials
cp .env.example .env

Run the project:

```bash
python main.py

## 📚 Inspire Examples

### Example 1: Futuristic Cyberpunk City

```python
from wiro_client import WiroClient
import os
from dotenv import load_dotenv

load_dotenv()

client = WiroClient(os.getenv("WIRO_KEY"), os.getenv("WIRO_SECRET"))

params = {
 "selectedModel": "1557",
 "prompt": "A futuristic cyberpunk city at night, glowing neon lights, flying cars in the sky, ultra-detailed, cinematic atmosphere",
 "negativePrompt": "low quality, blurry, pixelated",
 "steps": 45,
 "scale": 5.0,
 "flowShift": 3.0,
 "samples": 1,
 "seed": 0,
 "width": 1024,
 "height": 1024
}

print("🚀 HiDream AI Text-to-Image Generator - Python")
print("Running HiDream AI I1...")
print("Parameters:", params)
result = client.execute(params)
print("✅ Result:", result)

### Example 2: Golden Retriever Astronaut

```python
from wiro_client import WiroClient
import os
from dotenv import load_dotenv

load_dotenv()

client = WiroClient(os.getenv("WIRO_KEY"), os.getenv("WIRO_SECRET"))

params = {
 "selectedModel": "1557",
 "prompt": "A golden retriever astronaut floating in space, wearing a space suit, Earth in the background, photorealistic, 8k",
 "negativePrompt": "low quality, deformed, distorted",
 "steps": 45,
 "scale": 5.0,
 "flowShift": 3.0,
 "samples": 1,
 "seed": 0,
 "width": 1024,
 "height": 1024
}

print("🚀 HiDream AI Text-to-Image Generator - Python")
print("Running HiDream AI I1...")
print("Parameters:", params)
result = client.execute(params)
print("✅ Result:", result)

### Example 3: Fantasy Castle on Floating Island

```python
from wiro_client import WiroClient
import os
from dotenv import load_dotenv

load_dotenv()

client = WiroClient(os.getenv("WIRO_KEY"), os.getenv("WIRO_SECRET"))

params = {
 "selectedModel": "1557",
 "prompt": "A fantasy castle on top of a floating island, surrounded by waterfalls and glowing crystals, magical atmosphere, highly detailed",
 "negativePrompt": "low quality, cartoonish, unrealistic",
 "steps": 45,
 "scale": 5.0,
 "flowShift": 3.0,
 "samples": 1,
 "seed": 0,
 "width": 1024,
 "height": 1024
}

print("🚀 HiDream AI Text-to-Image Generator - Python")
print("Running HiDream AI I1...")
print("Parameters:", params)
result = client.execute(params)
print("✅ Result:", result)

## 🎬 Sample Output Gallery

| Sample 1 | Sample 2 | Sample 3 |
|:--------:|:--------:|:--------:|
| ![Sample 1](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-1.jpg) | ![Sample 2](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-2.jpg) | ![Sample 3](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-3.jpg) |
| ![Sample 4](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-4.jpg) | ![Sample 5](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-5.jpg) | ![Sample 6](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-6.jpg) |
| ![Sample 7](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-7.jpg) | ![Sample 8](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-8.jpg) | ![Sample 9](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-9.jpg) |
| ![Sample 10](https://cdn.wiro.ai/uploads/models/wiro-text-to-image-hidreamai-i1-sample-10.jpg) | | |

## 📦 What Happens Next

When you run `python main.py`, the following will happen:

```python
from wiro_client import WiroClient
import os
from dotenv import load_dotenv

load_dotenv()

client = WiroClient(os.getenv("WIRO_KEY"), os.getenv("WIRO_SECRET"))

# Real API request with actual parameters from Model Inputs
params = {
 "selectedModel": "1557",
 "prompt": "A golden retriever astronaut floating in space, wearing a space suit, Earth in the background, photorealistic, 8k",
 "negativePrompt": "",
 "steps": 45,
 "scale": 5.0,
 "flowShift": 3.0,
 "samples": 1,
 "seed": 0,
 "width": 1024,
 "height": 1024
}

print('🚀 HiDream AI Text-to-Image Generator - Python')
print('Running HiDream AI I1...')
print('Parameters:', params)

result = client.execute(params)
print('✅ Result:', result)

**Console Output:**

🚀 HiDream AI Text-to-Image Generator - Python
Running HiDream AI I1...
Parameters: {'selectedModel': '1557', 'prompt': 'A golden retriever astronaut floating in space, wearing a space suit, Earth in the background, photorealistic, 8k', 'negativePrompt': '', 'steps': 45, 'scale': 5.0, 'flowShift': 3.0, 'samples': 1, 'seed': 0, 'width': 1024, 'height': 1024}
🚀 Submitting task to Wiro API...
✅ Task submitted - ID: 789012
🔄 Polling for result...
✅ Task completed!
✅ Result: https://cdn.wiro.ai/output-file.ext

---

## 🌟 Built with [Wiro.ai](https://wiro.ai) 🌟

⭐ Star this repo • 🐍 Python Implementation

<sub>**Keywords:** text to image, ai images, python, automation, studio photos, hi dream ai, image generation, generative ai</sub>