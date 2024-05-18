---
title: Shader Pipeline
---

[Back to index](index.html)

---
# GLSL Basics
## Shader Pipeline

In the context of OpenGL and GLSL (OpenGL Shading Language), the shader pipeline refers to the stages that a vertex undergoes from the initial data input to the final rendered output on the screen. Here's a breakdown of the key stages in a typical shader pipeline:

1. **Vertex Shader:**
    - **Function**: The vertex shader processes individual vertices. It typically handles tasks such as transforming vertex positions from model space to screen space and passing per-vertex data such as colors, normals, and texture coordinates to the next stage.
    - **Input**: Vertex attributes such as position, normals, etc.
    - **Output**: Modified vertex attributes, like transformed positions and interpolated data for the fragment shader.

2. **Tessellation (Optional):**
    - **Tessellation Control Shader (TCS)**: This stage takes a patch of vertices and determines how much tessellation (subdivision) should be applied to it.
    - **Tessellation Evaluation Shader (TES)**: This shader processes the tessellated vertices to generate new vertices and their attributes.
    - **Function**: Used to increase the complexity of geometry dynamically.

3. **Geometry Shader (Optional):**
    - **Function**: The geometry shader can modify geometry by transforming, generating, or discarding primitives (points, lines, or triangles). It can create additional vertex data and generate multiple vertices to form new primitives.
    - **Input**: Primitives formed by vertices.
    - **Output**: Modified or new primitives.

4. **Fragment Shader:**
    - **Function**: This shader processes fragments (potential pixels). It colors them based on interpolated data from the vertex shader or geometry shader (such as texture coordinates, lighting information, etc.). It is here that most of the visual effects like texturing, lighting, bump mapping, etc., are applied.
    - **Input**: Interpolated data from the previous stage.
    - **Output**: Color and depth values for the framebuffer.

5. **Clipping and Rasterization:**
    - **Function**: This stage converts the vertex or geometry shader output into fragments. It involves clipping the primitives to the view volume and rasterizing them into a series of fragments for the fragment shader to process.
  
6. **Per-Fragment Operations:**
    - **Function**: After the fragment shader, several operations can be applied, including depth testing, alpha blending, stencil testing, and more, before the final color value is written to the framebuffer.
  
7. **Framebuffer:**
    - **Function**: The final stage where the fully processed fragments are compiled into the final image that appears on the screen. The framebuffer stores this image until it is displayed.

### Summary
- **Vertex Shader**: Transforms vertices and passes data.
- **Tessellation**: (If used) Subdivides and processes patches of vertices.
- **Geometry Shader**: (If used) Alters or creates geometry.
- **Fragment Shader**: Processes fragments to determine their color.
- **Per-Fragment Operations**: Tests and blending operations.
- **Framebuffer**: Stores the final image data for display.

Understanding each of these stages is crucial for effectively writing and optimizing GLSL shaders as they directly impact the rendering pipeline and how efficiently graphics are processed and rendered by the GPU.

---
[Back to index](index.html)
