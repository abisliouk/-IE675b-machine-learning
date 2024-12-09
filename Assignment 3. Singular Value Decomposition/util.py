# one file to rule them all
#
# Utility functions for IE 675 Machine Learning, University of Mannheim
#
# Autor: Rainer Gemulla <rgemulla@uni-mannheim.de>

import numpy as np
from numpy.linalg import svd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import linear_sum_assignment
from IPython import get_ipython


# def nextplot(force=False):
#     """Start a new plot.

#     In a notebook (or if `force=True`), create a new figure. Otherwise (e.g, in
#     IPython), clear the current figure.

#     """
#     inNotebook = "IPKernelApp" in get_ipython().config
#     if force or inNotebook:
#         plt.figure()  # this creates a new plot
#     else:
#         plt.clf()  # and this clears the current one

def nextplot():
    inTerminal = not "IPKernelApp" in get_ipython().config
    if inTerminal:
        plt.clf()     # this clears the current plot
    else:
        plt.figure()  # this creates a new plot 


def plot_matrix(
    M, lim=None, cmap="PiYG", labels="{:.3g}", rownames=None, colnames=None, **kwargs
):
    """Plot the given matrix in a labeled heatmap.

    `M` is the matrix or Pandas data frame.

    `lim` controls the range for the color scale for the entries. If unset, range of
    (-1,+1)*maximum value in `M`. If its a single integer, use range (-1,+1)*lim. Else
    `lim` should be a tuple of (minimum value, maximum value). `cmap` is the colormap
    being used.

    `labels` is a format string used to print the values of each matrix entry. If set to
    `None`, values are not printed (e.g., that's useful for very large matrices).

    `rownames` and `colnames` can be explicitly specified. If they are unset and `M` is
    a Pandas dataframe, row and column names are used from `M`. Otherwise, use indexes.

    """
    if isinstance(M, pd.DataFrame):
        if not colnames:
            colnames = M.columns.values
        if not rownames:
            rownames = M.index.values
        M = M.to_numpy()
    if lim is None:
        lim = np.max(np.abs((M[:, :])))
    if not isinstance(lim, tuple):
        lim = (-lim, lim)
    lim_mean = (lim[0] + lim[1]) / 2.0
    lim_spread = lim[1] - lim_mean

    nextplot()
    plt.matshow(M, fignum=0, cmap=cmap, vmin=lim[0], vmax=lim[1], **kwargs)
    if labels:
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                plt.text(
                    j,
                    i,
                    labels.format(M[i, j]),
                    color="white"
                    if np.abs(M[i, j] - lim_mean) > lim_spread / 2.0
                    else "black",
                    horizontalalignment="center",
                    verticalalignment="center",
                )
    plt.gca().set_xticks(range(M.shape[1]))
    if colnames is not None:
        plt.gca().set_xticklabels(colnames, rotation="vertical")
    plt.gca().set_yticks(range(M.shape[0]))
    if rownames is not None:
        plt.gca().set_yticklabels(rownames)
    plt.colorbar()


def plot_cov(M, **kwargs):
    """Plot a covariance matrix.

    `kwargs` are passed on to `plot_matrix`.

    """
    names = M.columns if isinstance(M, pd.DataFrame) else None
    Sigma = np.cov(M.transpose())
    plot_matrix(Sigma, labels=None, rownames=names, colnames=names, **kwargs)


def svdcomp(M, components=None):
    """Return sum of the specified components of the SVD of `M``.

    `M` is either a matrix (ndarray) or the SVD of a matrix (3-tuples of U,s,Vt).

    `components` is a list of components to sum up. If unspecified, sum up all the
    components. E.g., if `components=range(k)`, this methods computes the reconstruction
    of the size-k truncated SVD.

    """
    is_matrix = not isinstance(M, tuple)
    if not is_matrix:
        U, s, Vt = M
    if components is None:
        return M if is_matrix else U @ np.diag(s) @ Vt
    else:
        if type(components) == int:
            # this makes sure that shape of factors are retained (e.g., U[:,1] is a
            # vector and U[:,[1]] a matrix with one column)
            components = np.array([components])
        if is_matrix:
            U, s, Vt = svd(M)
        return U[:, components] @ np.diag(s[components]) @ Vt[components, :]


def plot_xy(x, y, z=None, aspect=1.0, axis=None, **kwargs):
    """Create a scatter plot with colored points.

    `x` and `y` are vectors of coordinates.

    If `z` is `None`, no colors are used. If `z` is a vector of integers (of the same
    length as `x` and `y`), each point `(x[i],y[i])` is colored with color `z[i]`. If
    `z` is a vector of floating point numbers, use a continuous color scale.

    `aspect` sets the aspect ratio of the plot.

    If `axis` is set, put the plot on the specified axis.
    """
    if not axis:
        nextplot()
        axis = plt.gca()
    if z is not None:
        if np.issubdtype(type(z[0]), np.signedinteger):
            # http://colorbrewer2.org/#type=qualitative&scheme=Paired&n=12
            colors = np.array(
                [
                    "#a6cee3",
                    "#1f78b4",
                    "#b2df8a",
                    "#33a02c",
                    "#fb9a99",
                    "#e31a1c",
                    "#fdbf6f",
                    "#ff7f00",
                    "#cab2d6",
                    "#6a3d9a",
                    "#ffff99",
                    "#b15928",
                    "#2f3631"
                ]
            )
            axis.scatter(x, y, c=colors[z], **kwargs)
        else:
            range = np.max(np.abs(z))
            im = axis.scatter(x, y, c=z, cmap="PiYG", vmin=-range, vmax=range, **kwargs)
            plt.colorbar(im, ax=axis)
    else:
        axis.scatter(x, y)
    axis.set_aspect(aspect)


def match_categories(categories1, categories2):
    """Match categories of two observation vectors.

    Takes two vectors of categorical observations; both vectors must have the same
    number of observations and the same number of distinct categories. This function
    renames the categories in `categories2` such that the result is as close as possible
    to `categories1` (in Hamming distance).

    This function can be used, for instance, to match two different clusterings. Then
    the categories correspond to cluster numbers and each observation to a data point.

    """

    if len(categories1) != len(categories2):
        raise ValueError("number of instances does not match")
    u1 = np.unique(categories1)
    u2 = np.unique(categories2)
    if len(u1) != len(u2):
        raise ValueError("number of categories does not match")

    C = len(u1)
    dist = np.zeros([C, C])
    for i in range(C):
        pos1 = categories1 == u1[i]
        n1 = np.sum(pos1)
        for j in range(C):
            pos2 = categories2 == u2[j]
            n2 = np.sum(pos2)
            pos12 = pos1 * pos2
            n12 = np.sum(pos12)
            dist[i, j] = (n1 - n12) + (n2 - n12)

    row, col = linear_sum_assignment(dist)
    result = categories1.copy()
    for j in range(C):
        result[categories2 == u2[j]] = u1[row[np.argmax(col == j)]]
    return result
