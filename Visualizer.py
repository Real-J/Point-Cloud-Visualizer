import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def downsample(points, max_points=500):
    if len(points) > max_points:
        idx = np.random.choice(len(points), max_points, replace=False)
        return points[idx]
    return points

def plot_points(xyz, colors=None, size=20, axis=False):  # larger points
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    if colors is None:
        colors = np.full((len(xyz), 3), [1.0, 0.5, 0])  # orange

    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], c=colors, s=size, depthshade=False)

    if axis:
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

    ax.view_init(elev=30, azim=45)
    plt.tight_layout()
    plt.show()

def plot_2d_projection(points):
    plt.figure(figsize=(5, 5))
    plt.scatter(points[:, 0], points[:, 1], s=10, color="orange")  # larger points
    plt.axis("equal")
    plt.title("2D XY Projection of Point Cloud")
    plt.show()

file_path = r"L:point_clouds.h5"

with h5py.File(file_path, "r") as f:
    sample_index = "0"
    group = f[sample_index]

    points = group["points"][:]
    label = group.attrs["label"]

    print(f"Sample {sample_index} → Digit: {label}, Points: {points.shape}")

    points = downsample(points, max_points=5000)

    plot_points(points)  # or plot_2d_projection(points)
