# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

def plot_in_rows(figsize, imgs, img_list=None, suptitle=None, vmin=None, vmax=None, cmap='viridis'):
    '''
    imgs: list of 2d arrays (images)
    img_list: list of strings (name of the images)
    '''
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    import matplotlib.pyplot as plt

    if img_list is None:
        img_list = np.arange(len(imgs))

    plt.figure(figsize=figsize)
    n = len(imgs)
    
    for i, k in enumerate(img_list):
        ax = plt.subplot(1, n, i+1)
        plt.axis('on')
        img = imgs[i]
        if vmin is not None and vmax is not None:
            im = plt.imshow(img, vmin=vmin, vmax=vmax, cmap=cmap)
        elif vmin is not None and vmax is None:
            im = plt.imshow(img, vmin=vmin, cmap=cmap)
        elif vmin is None and vmax is not None:
            im = plt.imshow(img, vmax=vmax, cmap=cmap)
        else:
            im = plt.imshow(img, cmap=cmap)
        plt.tick_params(labelsize=10)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.03)
        cb = plt.colorbar(im, cax=cax)
        cb.ax.tick_params(labelsize=10)
        ax.set_title(k, fontsize=10)
    plt.tight_layout()
    if suptitle is not None:
        plt.suptitle(suptitle, fontsize=12)
    plt.show()
    plt.close()
