import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colorbar import Colorbar
import cmasher as cmr
import mpl_scatter_density
import matplotlib.colors as colors
import read_eagle

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=18)
plt.rc('xtick', direction="in")
plt.rc('xtick.minor', visible=True)
plt.rc("ytick.minor", visible=True)
plt.rc('ytick', labelsize=18)
plt.rc('ytick', direction="in")
plt.rc('axes', labelsize=20)
plt.rc('axes', labelsize=20)
plt.rc('axes', grid=True)
plt.rc("xtick", top=True)
plt.rc("ytick", right=True)
plt.rc("grid", linewidth=0.8)
plt.rc("grid", linestyle=":")
plt.rc("grid", alpha=0.8)





def plot_scatter_density(x, y, ax=None, **kwargs):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(nrows=1, ncols=1, projection='scatter_density')

    im = ax.scatter_density(x, y, **kwargs)

    if ax is not None:
        return im, ax

def plot_scatter_density_histograms(x, y, ax=None, vlines=None, hlines=None, **kwargs):
    pass

if __name__ == "__main__":
    SIMPREFIX = "Ref"
    SIMNAME = "L0100N1504"
    SNAPNUM = "012"


    path = f"/home/abatten/EAGLE/{SIMPREFIX}{SIMNAME}/{SIMPREFIX}{SIMNAME}/snapshot_{SNAPNUM}_z003p017/snap_{SNAPNUM}_z003p017.0.hdf5"

    snap = read_eagle.EagleSnapshot(path)

    snap.select_region(0, 50, 0, 50, 0, 50)

    print("halos")
    halo_ids = snap.read_dataset(0, "GroupNumber")

    print("igm")
    igm = np.where(halo_ids == 1073741824)[0]

    print(igm)
    print(len(igm), len(halo_ids))
    print(len(igm)/len(halo_ids))
    print(len(igm)/len(halo_ids) * 1504**3)