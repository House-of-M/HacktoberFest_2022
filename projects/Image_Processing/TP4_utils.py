import numpy as np
import matplotlib as mpl

# Set colormap to 'gray'
mpl.rc('image', cmap='gray')
# Set np.nan to red
mpl.cm.get_cmap().set_bad(color='red')

# Function to display each pixels in an image with grid
def display_pixels(ax, image, title=None, **kwargs):
    height, width = image.shape[0:2]
    ax.imshow(image, **kwargs)
    for tic in ax.xaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False
    # if image is small enough, draw pixel borders
    if width < 100 and height < 100:
        ax.set_xticks(np.arange(-.5, width, 1), minor=True)
        ax.set_yticks(np.arange(-.5, height, 1), minor=True)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(which='minor', color=(.5,.5,.5), linestyle='-', linewidth=1)

    for tic in ax.xaxis.get_minor_ticks():
        tic.tick1On = tic.tick2On = False
    for tic in ax.yaxis.get_minor_ticks():
        tic.tick1On = tic.tick2On = False
    if title:
        ax.set_title(title)
def assert_binary_uint8(*arrays):
    for i, array in enumerate(arrays):
        assert array.dtype == np.uint8, "input#{} is expected to be 'np.uint8' but is {}".format(i,array.dtype)
        assert np.max(array) <= 1, "input#{} is expected to be 0s or 1s but has a maximum value of {}".format(i,np.max(array))
    
def resize_and_fix_origin(kernel, size):
    """Pads a kernel to reach shape `size`, and shift it in order to cancel phase.
    This is based on the assumption that the kernel is centered in image space.
    """
    # Very specific routine... You don't have to understand it
    pad0, pad1 = size[0]-kernel.shape[0], size[1]-kernel.shape[1]
    # shift less if kernel is even, to start with 2 central items
    shift0, shift1 = (kernel.shape[0]-1)//2, (kernel.shape[1]-1)//2

    kernel = np.pad(kernel, ((0,pad0), (0,pad1)))
    kernel = np.roll(kernel, (-shift0, -shift1), axis=(0,1))
    return kernel