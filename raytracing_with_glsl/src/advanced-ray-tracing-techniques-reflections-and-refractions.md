---
title: Reflections and Refractions
---

[Back to index](index.html)

---
# Advanced Ray Tracing Techniques
## Reflections and Refractions

Reflections and refractions are two advanced techniques in ray tracing that enhance the realism of rendered scenes by simulating how light interacts with surfaces. Here’s an in-depth look at each:

### Reflections

Reflections occur when a ray of light hits a surface and bounces off in a predictable manner. Simulating reflections in ray tracing involves tracing a secondary ray, known as the reflection ray, from the point of intersection on the surface. Key aspects include:

1. **Reflection Vector Calculation**:
   - The reflection ray direction can be computed using the incident ray direction and the normal at the point of contact. The formula for the reflection vector, \( \vec{R} \), is:
     \[
     \vec{R} = \vec{I} - 2 (\vec{N} \cdot \vec{I}) \vec{N}
     \]
     where \( \vec{I} \) is the incident ray direction and \( \vec{N} \) is the normal at the intersection point.

2. **Recursive Ray Tracing**:
   - When a reflection ray is traced, it might intersect with other objects in the scene. This secondary intersection could generate more reflection rays, leading to recursive ray tracing. Typically, recursion depth is limited to improve performance.

3. **Phong Reflection Model**:
   - The Phong reflection model combines ambient, diffuse, and specular reflections to create realistic lighting effects. The specular component often simulates shiny surfaces where reflections are prominent.

4. **Environment Mapping**:
   - For distant environments, environment maps (such as cubemaps) can be used to provide background details in reflections without the need to trace rays to distant objects.

### Refractions

Refractions involve the bending or changing direction of light as it passes through a transparent material, governed by Snell's Law. Essential elements include:

1. **Snell's Law**:
   - Snell's Law determines the direction of the refracted ray. It is given by:
     \[
     n_1 \sin(\theta_1) = n_2 \sin(\theta_2)
     \]
     where \( n_1 \) and \( n_2 \) are the refractive indices of the two media, and \( \theta_1 \) and \( \theta_2 \) are the angles of incidence and refraction, respectively.

2. **Refractive Index**:
   - The refractive index of a material describes how much the light bends. Common materials have known indices (e.g., air ~1.0, water ~1.33, glass ~1.5).

3. **Refraction Vector Calculation**:
   - The direction of the refracted ray can be calculated using the incident ray direction \( \vec{I} \), the surface normal \( \vec{N} \), and the refractive indices. The refraction direction \( \vec{T} \) can be derived as:
     \[
     \vec{T} = \frac{n_1}{n_2} \vec{I} + \left( \frac{n_1}{n_2} \cos(\theta_1) - \cos(\theta_2) \right) \vec{N}
     \]

4. **Total Internal Reflection**:
   - When light passes from a medium with a higher refractive index to one with a lower refractive index (e.g., from water to air), at a certain angle, no refraction occurs. Here, all light is reflected internally. This critical angle can be calculated and is important to handle properly in the shader logic.

### Implementing Reflections and Refractions in GLSL

1. **Reflection Shader**:
   - In GLSL, compute the reflection vector and cast reflection rays. Use texture maps or recursive ray tracing to determine the color contribution from the reflected rays.

2. **Refraction Shader**:
   - Implement Snell's Law to compute the refraction vector. Cast refraction rays and accumulate the color contribution, considering the transparency and attenuation through the material.

3. **Combining Reflection and Refraction**:
   - Fresnel equations can be used to blend reflection and refraction based on viewing angles. Implementing Fresnel terms ensures more realistic surface interactions.

Here's a brief outline of GLSL code for reflections and refractions:

```glsl
// Calculate Reflection Vector
vec3 reflectionDir = reflect(-incidentRay, normal);

// Calculate Refraction Vector
float eta = refractiveIndex1 / refractiveIndex2;
float cosi = dot(-incidentRay, normal);
float sint2 = eta * eta * (1.0 - cosi * cosi);
vec3 refractionDir = eta * incidentRay + (eta * cosi - sqrt(1.0 - sint2)) * normal;

// Trace and shade object with reflection and refraction contributions
vec4 reflectionColor = traceRay(reflectionDir);
vec4 refractionColor = traceRay(refractionDir);

// Combine based on Fresnel term
float fresnelFactor = fresnel(cosi, eta);
vec4 finalColor = mix(refractionColor, reflectionColor, fresnelFactor);
```

### Conclusion

Simulating reflections and refractions adds significant complexity but also tremendous realism to a scene. These effects require careful computation of vector directions, consideration of recursive ray tracing, and managing performance. As you implement these techniques in GLSL, leveraging the power of modern GPUs can provide efficient and visually stunning results.

---
[Back to index](index.html)
