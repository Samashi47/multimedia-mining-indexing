# multimedia-mining-indexing
This repository contains code and resources for a multimedia mining and indexing course.

### Author: Ahmed Samady
### Supervised by: Pr. M'hamed Ait Kbir

## Overview
This repository provides a collection of professor code snippets, exercise solutions, and my assignment submissions.

## Getting Started
To get started with this repository, follow these steps:
Clone the repository:
```bash
git clone -b main --single-branch [https://github.com/Samashi47/multimedia-mining-indexing]
```
Navigate to the directory of the cloned repository:
```bash
cd multimedia-mining-indexing
```
### Python
Create a virtual environment in the repository by typing the followwing command:
```bash
python -m venv .venv
```
After cloning the project and creating your venv, activate the venv by:

```bash
.venv\Scripts\activate
```
You can run the following command to install the dependencies:
```bash
pip3 install -r requirements.txt
```
> [!NOTE]  
> To install PyOpenGL on Windows, I recommend the following method (this may or may not work for you, it depends on you machine):
> Clone the following repo in the base of this repository:
> ```bash
> git clone https://github.com/mcfletch/pyopengl
> ```
> cd to it and install it using pip:
> ```bash
> cd pyopengl
> pip install -e .
> ```
> cd to accelerate and install it using pip:
> ```bash
> cd accelerate
> pip install -e .
> ```
> This should work in most cases, and the vscode settings.json should detect the PyOpenGL and provide IntelliSense.
