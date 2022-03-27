# event_denoise
A very simple event denoising method.  
Denoise event-based camera data based on **correlation**.

## Dependency
numpy, pandas, opencv-python

## Usage
```bash
python denoise.py [--root_path][--show_image][--begin]
```

## Principle
For each frame, if an event has more than `N` neighbors in a `K*K` window, then a valid data;  
Othervise, a noise.

Valid data are reserved.
