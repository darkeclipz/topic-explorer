---
title: Ray Generation
---

[Back to index](index.html)

---
# Ray Tracing Fundamentals
## Ray Generation

### Ray Generation (Ray Tracing Fundamentals)

Ray generation is a crucial step in the ray tracing pipeline, where rays are initially created to simulate the way light interacts with objects in a scene. Here's a deeper look into the key components and steps involved in ray generation:

#### **1. Camera Model**
- **Position**: The camera's position in the scene determines the origin of the rays.
- **Orientation**: This includes the view direction, up vector, and right vector that define the camera's coordinate system.
- **Field of View**: This determines the angle of the viewing frustum, affecting how wide the scene appears.

#### **2. Ray Origins and Directions**
- **Pixel to Ray Mapping**: Each pixel on the screen corresponds to a unique ray. The goal is to map screen coordinates to world coordinates.
- **Ray Origin**: Typically, all rays originate from the camera position.
- **Ray Direction**: Calculated based on the pixel's position on the screen:
  - **Viewport Calculation**: Convert pixel coordinates to normalized device coordinates and then to screen space.
  - **Transform to World Space**: Convert the screen space coordinates to world space using the camera's transformation matrix.
  - **Constructing Ray Directions**: The direction is often normalized, and it's computed by subtracting the eye position from the point on the screen in world space.

#### **3. Viewing Rays Setup**
- **Primary Rays**: These are the initial rays cast directly from the camera into the scene. Every pixel on the screen typically casts one primary ray.
- **Ray Equation**: The parametric form of the ray equation is used:
  \[
  \text{Ray}(t) = \text{Origin} + t \times \text{Direction}
  \]
  where \( t \) is a scalar that varies along the ray's path.

#### **4. Ray Buffering**
- **Ray Structures**: Rays are often stored in buffers. Each ray typically includes:
  - `origin`: The start point of the ray.
  - `direction`: The normalized direction vector along which the ray travels.
  - `t_min` and `t_max`: These define the range along the ray's path for intersection testing.

#### **5. GLSL Implementation**
In GLSL, ray generation typically happens in a fragment shader or compute shader:
- **Fragment Shader**: Each fragment corresponds to a pixel, ideal for generating primary rays.
- **Compute Shader**: More flexible for complex ray generation patterns and managing multiple rays per pixel (e.g., for anti-aliasing).

Example GLSL Code Snippet for Ray Generation:
```glsl
#version 450

in vec2 fragCoord; // Screen coordinates
uniform vec3 cameraPos; // Camera position
uniform mat4 viewMatrix; // View transformation matrix
uniform mat4 projMatrix; // Projection matrix

out vec3 rayOrigin;
out vec3 rayDirection;

void main() {
    // Transform screen coordinates to normalized device coordinates (NDC)
    vec2 ndc = (fragCoord / vec2(SCREEN_WIDTH, SCREEN_HEIGHT)) * 2.0 - 1.0;
    
    // Transform NDC to camera space
    vec4 clipSpace = vec4(ndc, -1.0, 1.0); // Assuming near plane at z = -1
    vec4 viewSpace = inverse(projMatrix) * clipSpace;
    viewSpace.z = -1.0; // Correcting the depth
    viewSpace.w = 0.0;
    
    // Transform to world space
    vec4 worldSpace = inverse(viewMatrix) * viewSpace;
    
    // Calculate the ray direction
    rayOrigin = cameraPos;
    rayDirection = normalize(worldSpace.xyz - cameraPos);
}
```

#### **6. Anti-Aliasing and Sampling**
- **Super-sampling**: Casting multiple rays per pixel (jittered) to achieve anti-aliasing.
- **Random Sampling**: Introduce randomness to the ray directions for effects like depth of field and motion blur.

### Conclusion

Ray generation is the foundational step in ray tracing, setting the stage for subsequent intersection tests, shading, and lighting calculations. Understanding how to generate and manage rays effectively is crucial for crafting realistic and performant ray-traced imagery.

---
[Back to index](index.html)
