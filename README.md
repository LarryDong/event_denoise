# event_denoise
A very simple event denoising method.  
Denoise event-based camera data based on **correlation**.

<div align=center>
<img src="https://github.com/LarryDong/event_denoise/blob/main/Result.png" width="720" height="280" alt="event frame"/><br/>
</div>

## Dependency
numpy, pandas, opencv-python

## Usage
```bash
python denoise.py [--root_path][--show_image][--begin][--K][--N]
```

`K` and `N` are two key parameters for filtering.  
For each frame, if an event has more than `N` neighbors in a `K*K` window, then a valid data; Valid data are reserved.  
Othervise, a noise and filtered. 
