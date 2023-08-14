# Reaction Diffusion Simulator (Python)

This repository contains a Python implementation of a real-time 2D Gray-Scott reaction diffusion simulator. It uses the following equations to generate real-time pixel array color assignments:

![image](https://github.com/Beniam-Kumela/reaction-diffusion-py/assets/106757076/1ca3265b-067e-4e7f-b65f-2e2432a4f565)


![image](https://github.com/Beniam-Kumela/reaction-diffusion-py/assets/106757076/0785ab72-65ff-4124-9877-6d1e771f00cd)


For the most optimized version, the following convolution matrix was used to represent the 2D discrete Laplacian operator using the five-point stencil method:

![image](https://github.com/Beniam-Kumela/reaction-diffusion-py/assets/106757076/7c19561e-3015-4bed-b529-dbbe783d9fb7)

Circles were rastered using the [Midpoint Circle Algorithm](https://en.wikipedia.org/wiki/Midpoint_circle_algorithm) and [here](https://www.karlsims.com/rd.html) is more information about the Gray-Scott model.

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
- Randomized color selection.
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

https://github.com/Beniam-Kumela/reaction-diffusion-py/assets/106757076/1ee19416-a248-4ae1-9161-9e4e27f1f8eb

"Mitosis-growth mode" sped up by 16x:

https://github.com/Beniam-Kumela/reaction-diffusion-py/assets/106757076/8ad93f9d-11b4-49d7-a4f1-19d098d37ea9

Inferno color map of a 500x500 grid for 1000 frames (video.py):

![inferno, 1000 frames, 500 grid](https://github.com/Beniam-Kumela/reaction-diffusion-py/assets/106757076/5597a2bd-a3cc-4d89-9c88-4b22a29078db)


Winter color map of a 200x200 grid for 500 frames (video.py):

![winter, 500 frames, 200 grid (2)](https://github.com/Beniam-Kumela/reaction-diffusion-py/assets/106757076/05cc210a-c7ea-4ec5-a106-584b4d008131)


## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you find a bug, have a feature request, or would like to improve the project in any way. 

For the future, I would like to utilize the graphics card with OpenGL for faster processing and maybe writing some fragment shaders.

## License

This project is licensed under the MIT License.
