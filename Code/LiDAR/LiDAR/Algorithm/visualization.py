import numpy as np
import open3d as o3d

if __name__ == "__main__":

    with open('../2.csv', 'r') as csv_file:
        PointcloudData = []
        for line in csv_file:
            line_list = line.split()
            x = int(line_list[0])
            y = int(line_list[1])
            z = 0
            PointcloudData.append([x, y, z])
        
        PointcloudArray = np.array(PointcloudData)

        print("Testing IO for point cloud ...")
        # pcd = o3d.io.read_point_cloud("../2.xyzrgb")
        pcd = o3d.io.read_point_cloud("../Recordings/1.xyzrgb")


        axis_pcd = o3d.geometry.TriangleMesh.create_coordinate_frame(size=500, origin=[0, 0, 0])

        test_pcd = o3d.geometry.PointCloud()

        test_pcd.points = o3d.utility.Vector3dVector(PointcloudArray)  # 定义点云坐标位置
        
        o3d.visualization.draw_geometries([pcd]+[axis_pcd])


        