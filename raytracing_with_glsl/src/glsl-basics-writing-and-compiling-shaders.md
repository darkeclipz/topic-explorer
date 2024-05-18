---
title: Writing and Compiling Shaders
---

[Back to index](index.html)

---
# GLSL Basics
## Writing and Compiling Shaders

### Writing and Compiling Shaders (GLSL Basics)

#### Introduction to Shaders
- **Vertex Shaders**: Process each vertex's properties (such as position, color, normal) to determine its screen position.
- **Fragment Shaders**: Handle pixel-level data and determine the color of each pixel on the screen.

#### Writing Shaders
Shaders in GLSL are typically written in GLSL (OpenGL Shading Language). Here are the basic steps:

1. **Shader Program Structure**: 
    - GLSL shaders start with a version declaration (e.g., `#version 330 core`).
    - Variables are declared using specific GLSL data types.
    - Main function (`void main()`) serves as the entry point.

Example Vertex Shader:
```glsl
#version 330 core

layout(location = 0) in vec3 vertexPosition;
layout(location = 1) in vec3 vertexColor;

out vec3 fragColor;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

void main() {
    fragColor = vertexColor;
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
}
```

Example Fragment Shader:
```glsl
#version 330 core

in vec3 fragColor;
out vec4 color;

void main() {
    color = vec4(fragColor, 1.0);
}
```

#### Compiling Shaders

1. **Creating Shader Objects**:
   - Use `glCreateShader(GL_VERTEX_SHADER)` for vertex shaders.
   - Use `glCreateShader(GL_FRAGMENT_SHADER)` for fragment shaders.
   
2. **Shader Source Code**:
   - Attach the GLSL code to the shader object with `glShaderSource(shader, 1, &shaderCode, NULL)`.

3. **Compiling Shaders**:
   - Compile the shader using `glCompileShader(shader)`.
   - Check for compilation errors with `glGetShaderiv(shader, GL_COMPILE_STATUS, &success)` and retrieve the log with `glGetShaderInfoLog(shader, logLength, NULL, log)`.

#### Creating and Linking Shader Program

1. **Creating Program Object**: 
   - Use `glCreateProgram()` to create the shader program object.
   
2. **Attaching Shaders**: 
   - Attach the compiled vertex and fragment shaders using `glAttachShader(program, vertexShader)` and `glAttachShader(program, fragmentShader)`.

3. **Linking**:
   - Link the shader program with `glLinkProgram(program)`.
   - Check the linking status with `glGetProgramiv(program, GL_LINK_STATUS, &success)` and retrieve the log with `glGetProgramInfoLog(program, logLength, NULL, log)`.

4. **Using the Shader Program**:
   - Once the shader program is linked, it can be activated with `glUseProgram(program)`.

Example of Full Shader Compilation and Linking in OpenGL (C):
```c
GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
glShaderSource(vertexShader, 1, &vertexShaderCode, NULL);
glCompileShader(vertexShader);
CheckCompileErrors(vertexShader, "VERTEX");

GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
glShaderSource(fragmentShader, 1, &fragmentShaderCode, NULL);
glCompileShader(fragmentShader);
CheckCompileErrors(fragmentShader, "FRAGMENT");

GLuint shaderProgram = glCreateProgram();
glAttachShader(shaderProgram, vertexShader);
glAttachShader(shaderProgram, fragmentShader);
glLinkProgram(shaderProgram);
CheckLinkErrors(shaderProgram);

glDeleteShader(vertexShader);
glDeleteShader(fragmentShader);
```

#### Best Practices for Writing Shaders
- **Code Modularity**: Use functions to modularize your shader code.
- **Precision Qualifiers**: Utilize precision qualifiers (like `highp`, `mediump`, `lowp`) as needed.
- **Shader Version**: Ensure that the GLSL version declared at the top matches the capabilities of your target hardware.

#### Conclusion
Understanding the basics of writing and compiling shaders is crucial for effectively using GLSL in graphics programming. This involves creating and managing shader objects, handling compilation, and linking them into a shader program that can be used for rendering in OpenGL.

---
[Back to index](index.html)
