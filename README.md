# Reaction Diffusion Simulator (Python)

This repository contains a Python implementation of a real-time 2D Gray-Scott reaction diffusion simulator. It uses the following equations to generate real-time pixel array color assignments:

<img src = "https://latex.codecogs.com/svg.image?A'=A&plus;(D_{A}\nabla^{2}A-AB^2&plus;f(1-A))\Delta&space;t&space;">

<img src = "https://latex.codecogs.com/svg.image?B'=B&plus;(D_{B}\nabla^{2}B&plus;AB^2-(k&plus;f)B)\Delta&space;t&space;">

For the most optimized version, the following convolution matrix was used to represent the 2D discrete Laplacian operator using the five-point stencil method:

<img src = "https://latex.codecogs.com/svg.image?\nabla^{2}=\begin{bmatrix}0&1&0\\1&-4&1\\0&1&0\\\end{bmatrix}">

There is also a GIF generator of this diffusion model for those that are interested (video.py). This is not compiled into an .exe as the simulator is but is capable of calculating more iterations with higher quality resolutions and more customization.

## Table of Contents

1. [Features](/README.md#features)
2. [Dependencies](/README.md#dependencies)
3. [Building and Running](/README.md#building-and-running)
4. [Example](/README.md#usage)
5. [Contributing](/README.md#contributing)
6. [License](/README.md#license)

## Features

- Start menu with simulator description and key layouts.
- Hardware acceleration is enabled.
- Mitosis and coral growth modes.
- Random color selection.
- Real-time diffusion model with parallel computing for optimal performance.
- Ability for user to diffuse the following shapes into the solution: circles, stars, squares, and crosses.

## Dependencies

This project depends on the following libraries which are all compiled into the .exe:

- pygame
- sys
- numba
- numpy

## Building and Running

### Windows

1. Download the .zip file by pressing the green "Code" button and selecting "Download ZIP".
2. Extract all components of the .zip file.
3. Navigate to the folder titled "dist" and run the main.exe

If you want to use the GIF generator (video.py), make sure to have Python installed into the correct PATH. This program will run in command line and prompt you for info regarding color, frames, grid size, etc. A progress bar will give you updates and let you know when and where the animation is generated and saved. 

### Customization

If any edits want to be made to the code, navigate to the main.py or video.py files to save changes and run in a text editor / virtual environment.

To change feed and kill rates change the following parameters in the main.py file (lines 35-41) to get different designs.

```
feed = 0.0367
k = 0.0649
```
## Example

"Coral-growth mode" sped up by 4x:


"Mitosis-growth mode" sped up by 16x:


Inferno color map of a 500x500 grid for 1000 frames (video.py):


Winter color map of a 200x200 grid for 500 frames (video.py):



## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you find a bug, have a feature request, or would like to improve the project in any way. 

For the future, I would like to utilize the graphics card with OpenGL for faster processing and maybe writing some fragment shaders.

## License

This project is licensed under the MIT License.