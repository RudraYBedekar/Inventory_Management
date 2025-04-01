import numpy as np

points = np.random.rand(100, 2) * 10  # simulate pick points
central = np.median(points, axis=0)
original_time = np.mean(np.linalg.norm(points - np.mean(points, axis=0), axis=1))
optimized_time = np.mean(np.linalg.norm(points - central, axis=1))
improvement = original_time - optimized_time

print(f"Pick time reduced by ( {improvement:.6f} )seconds per item")
