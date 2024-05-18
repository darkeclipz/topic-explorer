---
title: Lighting and Shading Models
---

[Back to index](index.html)

---
# Ray Tracing Fundamentals
## Lighting and Shading Models

Lighting and shading are fundamental aspects of creating realistic images in ray tracing. Here’s a detailed explanation of the key concepts:

### Lighting Models

1. **Ambient Lighting**:
   - Ambient lighting represents indirect lighting that is not from any specific direction. It provides a simple way to account for the light scattering around a scene.
   - Formula:
     \[
     I_{\text{ambient}} = k_{\text{ambient}} \cdot I_{\text{ambient\_light}}
     \]
   - Where \( k_{\text{ambient}} \) is the ambient reflectance of the object, and \( I_{\text{ambient\_light}} \) is the intensity of the ambient light.

2. **Point Lighting**:
   - A point light source emits light equally in all directions from a single point in space.
   - Important factors include light position, intensity, and attenuation.
   - Formula:
     \[
     I = \frac{I_{\text{point}}}{a + b \cdot d + c \cdot d^2}
     \]
   - Where \( I_{\text{point}} \) is the intensity of the light, \( a, b, \) and \( c \) are attenuation coefficients, and \( d \) is the distance from the light source.

3. **Directional Lighting**:
   - A directional light simulates a light source that is infinitely far away, such as the sun.
   - The light rays are parallel, and there is no attenuation over distance.

4. **Spot Lighting**:
   - A spot light emits light in a specific direction and within a cone of influence. Useful for effects like flashlights or stage lighting.
   - Parameters include position, direction, cutoff angle, and intensity.

### Shading Models

1. **Lambertian Shading (Diffuse Shading)**:
   - Assumes that light is scattered equally in all directions from a surface.
   - The brightness of the surface is proportional to the cosine of the angle between the light direction and the surface normal (`dot product`).
   - Formula:
     \[
     I_{\text{diffuse}} = k_{\text{diffuse}} \cdot I \cdot \left(N \cdot L\right)
     \]

2. **Phong Shading (Specular Shading)**:
   - Adds specular highlights to the Lambertian model to capture shiny surfaces.
   - Depends on the viewer's position and the reflection of the light direction.
   - Formula:
     \[
     I_{\text{specular}} = k_{\text{specular}} \cdot I \cdot (R \cdot V)^n
     \]
   - Where \( R \) is the reflection vector, \( V \) is the view vector, and \( n \) is the shininess exponent.

3. **Blinn-Phong Shading**:
   - A modification of Phong shading that uses the halfway vector between the light direction and the view direction for the specular calculation.
   - Less computationally expensive and often produces similar results.
   - Formula:
     \[
     I_{\text{specular}} = k_{\text{specular}} \cdot I \cdot (N \cdot H)^n
     \]
   - Where \( H \) is the halfway vector of \( L \) and \( V \).

### Combined Lighting Model
In practice, the overall lighting \( I \) of a point on a surface combines ambient, diffuse, and specular components:

\[
I_{\text{total}} = I_{\text{ambient}} + I_{\text{diffuse}} + I_{\text{specular}}
\]

### Implementation in Ray Tracing with GLSL
1. **Calculating the Surface Normals**:
   - Normals are used to determine how light interacts with surfaces.
   - For each point of intersection, compute or retrieve the normal.

2. **Ray-Surface Intersection**:
   - Determine the points where rays intersect objects in the scene.

3. **Computing Light Contributions**:
   - Calculate the light contributions from all relevant light sources (ambient, diffuse, specular).

4. **Shader Programs**:
   - Write GLSL shaders that perform these calculations. Vertex shaders typically pass data to fragment shaders, where the actual lighting calculations happen.

```glsl
// Example snippet of a GLSL fragment shader
varying vec3 vNormal;
varying vec3 vPosition;
uniform vec3 lightPosition;
uniform vec3 viewPosition;

void main() {
    vec3 N = normalize(vNormal);
    vec3 L = normalize(lightPosition - vPosition);
    vec3 V = normalize(viewPosition - vPosition);
    vec3 R = reflect(-L, N);

    // Ambient
    vec3 ambient = vec3(0.1, 0.1, 0.1);

    // Diffuse
    float diff = max(dot(N, L), 0.0);
    vec3 diffuse = diff * vec3(1.0, 1.0, 1.0);

    // Specular
    float spec = pow(max(dot(V, R), 0.0), 32.0);
    vec3 specular = spec * vec3(1.0, 1.0, 1.0);
    
    // Combine
    vec3 color = ambient + diffuse + specular;
    gl_FragColor = vec4(color, 1.0);
}
```

By understanding and implementing these models in GLSL, you can create realistic lighting effects in ray-traced scenes.

---
[Back to index](index.html)
