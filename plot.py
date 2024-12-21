import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import io


def create_svg_source(width, height, length):
    """
    Create a simple 3D plot of a cuboid with specified dimensions and return it as an SVG string.

    Parameters:
    - width: float, width of the cuboid in cm
    - height: float, height of the cuboid in cm
    - length: float, length of the cuboid in cm

    Returns:
    - svg_content: str, the SVG content as a string
    """
    # Create a figure and 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Define the cuboid vertices
    vertices = [
        [0, 0, 0], [width, 0, 0], [width, length, 0], [0, length, 0],  # Bottom face
        [0, 0, height], [width, 0, height], [width, length, height], [0, length, height]  # Top face
    ]

    # Define the faces of the cuboid
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front face
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right face
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back face
        [vertices[3], vertices[0], vertices[4], vertices[7]],  # Left face
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom face
        [vertices[4], vertices[5], vertices[6], vertices[7]]  # Top face
    ]

    # Plot the cuboid using Poly3DCollection
    ax.add_collection3d(Poly3DCollection(faces, facecolors='skyblue', linewidths=1, edgecolors='black', alpha=0.8))

    # Set axis labels
    ax.set_xlabel("Width (cm)")
    ax.set_ylabel("Length (cm)")
    ax.set_zlabel("Height (cm)")

    # Set the aspect ratio of the plot
    max_dim = max(width, length, height)
    ax.set_box_aspect([width / max_dim, length / max_dim, height / max_dim])

    # Save the plot to an SVG string
    svg_buffer = io.StringIO()
    fig.savefig(svg_buffer, format="svg", transparent=True)
    plt.close(fig)

    # Return the SVG content
    svg_content = svg_buffer.getvalue()
    svg_buffer.close()
    return svg_content

# create_svg_source(24, 3, 2)