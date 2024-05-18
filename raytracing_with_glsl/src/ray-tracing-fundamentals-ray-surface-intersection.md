---
title: Ray-Surface Intersection
---

[Back to index](index.html)

---
# Ray Tracing Fundamentals
## Ray-Surface Intersection

Ray-surface intersection is a fundamental concept in ray tracing, which involves calculating the points at which rays (originating from a point, usually the camera, and traveling in a straight line) intersect with surfaces in a 3D scene. Determining these intersection points is crucial for rendering the scene accurately, as it forms the basis for shading, lighting, and visibility calculations.

Here is a detailed explanation of ray-surface intersection for key geometries commonly used in ray tracing:

### 1. **Ray-Plane Intersection**
A plane in 3D space can be defined by a point \(\mathbf{P}\) on the plane and a normal vector \(\mathbf{N}\). A ray can be defined by an origin \(\mathbf{O}\) and a direction \(\mathbf{D}\).
- **Equation of the plane**: \(\mathbf{(Q - P) \cdot N} = 0\), where \(\mathbf{Q}\) is any point on the plane.
- **Ray equation**: \(\mathbf{R(t) = O + tD}\), where \(t\) is a scalar parameter and \(\mathbf{R(t)}\) is a point along the ray.

To find the intersection, substitute the ray equation into the plane equation:
\[ (\mathbf{R(t)} - \mathbf{P}) \cdot \mathbf{N} = 0 \]
\[ (\mathbf{O + tD - P}) \cdot \mathbf{N} = 0 \]
\[ (\mathbf{O - P}) \cdot \mathbf{N} + t (\mathbf{D} \cdot \mathbf{N}) = 0 \]

Solving for \(t\):
\[ t = \frac{(\mathbf{P} - \mathbf{O}) \cdot \mathbf{N}}{\mathbf{D} \cdot \mathbf{N}} \]

If \(\mathbf{D} \cdot \mathbf{N} ≠ 0\), compute \(t\), and if \(t \ge 0\), the intersection point \(\mathbf{R(t)}\) lies on the plane.

### 2. **Ray-Sphere Intersection**
A sphere can be defined by its center \(\mathbf{C}\) and radius \(r\).
- **Equation of the sphere**: \( \| \mathbf{Q} - \mathbf{C} \|^2 = r^2 \)
- **Ray equation**: \(\mathbf{R(t) = O + tD}\), where \(\mathbf{R(t)}\) is a point along the ray.

Substitute the ray equation into the sphere equation:
\[ \| (\mathbf{O + tD}) - \mathbf{C} \|^2 = r^2 \]
\[ \| \mathbf{(O - C) + tD} \|^2 = r^2 \]

This expands to a quadratic equation:
\[ (\mathbf{D \cdot D}) t^2 + 2 (\mathbf{(O - C) \cdot D}) t + (\mathbf{(O - C) \cdot (O - C)}) - r^2 = 0 \]

Using the quadratic formula \(ax^2 + bx + c = 0\), solve for \(t\):
\[ t = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \]
where:
\[ a = \mathbf{D \cdot D} \]
\[ b = 2 (\mathbf{(O - C) \cdot D}) \]
\[ c = \mathbf{(O - C) \cdot (O - C)} - r^2 \]

The discriminant \(b^2 - 4ac\) determines the nature of the intersection:
- If \(b^2 - 4ac < 0\), there are no real intersections (the ray misses the sphere).
- If \(b^2 - 4ac = 0\), there is one intersection (the ray is tangent to the sphere).
- If \(b^2 - 4ac > 0\), there are two intersections (the ray enters and exits the sphere).

### 3. **Ray-Triangle Intersection**
Triangles are often used in mesh modeling due to their simplicity. A triangle can be defined by three vertices \(\mathbf{V0, V1, V2}\).
- **Ray equation**: \(\mathbf{R(t) = O + tD}\)

One common method for ray-triangle intersection is the Möller-Trumbore algorithm:
1. Compute edges of the triangle:
   \[ \mathbf{E1} = \mathbf{V1} - \mathbf{V0} \]
   \[ \mathbf{E2} = \mathbf{V2} - \mathbf{V0} \]

2. Compute the determinant and helpers:
   \[ \mathbf{P} = \mathbf{D} \times \mathbf{E2} \]
   \[ \text{det} = \mathbf{E1} \cdot \mathbf{P} \]

If \(\text{det}\) is close to 0, the ray lies in the plane of the triangle. Otherwise, continue:
   \[ \mathbf{invDet} = 1 / \text{det} \]

3. Compute the distance from \(\mathbf{V0}\) to the ray origin:
   \[ \mathbf{T} = \mathbf{O} - \mathbf{V0} \]

4. Compute barycentric coordinates \(u\) and \(v\):
   \[ u = (\mathbf{T} \cdot \mathbf{P}) \times \mathbf{invDet} \]
   If \(u < 0\) or \(u > 1\), the intersection is outside the triangle.

5. Compute another helper:
   \[ \mathbf{Q} = \mathbf{T} \times \mathbf{E1} \]

6. Compute the second barycentric coordinate \(v\):
   \[ v = (\mathbf{D} \cdot \mathbf{Q}) \times \mathbf{invDet} \]
   If \(v < 0\) or \(u + v > 1\) the intersection is outside the triangle.

7. Finally, compute \(t\):
   \[ t = (\mathbf{E2} \cdot \mathbf{Q}) \times \mathbf{invDet} \]
   If \(t > 0\), the ray intersects the triangle at \(\mathbf{R(t)} = \mathbf{O} + t\mathbf{D}\).

These core intersection tests are the building blocks for more sophisticated ray tracing techniques, and they facilitate accurate rendering by determining where rays interact with the scene geometry.

---
[Back to index](index.html)
