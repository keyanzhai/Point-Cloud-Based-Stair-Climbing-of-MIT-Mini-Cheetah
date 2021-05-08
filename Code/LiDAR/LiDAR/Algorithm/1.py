import numpy as np
import open3d as o3d
from pyntcloud import PyntCloud

points = np.random.rand(10000, 3)
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)
o3d.visualization.draw_geometries([point_cloud])