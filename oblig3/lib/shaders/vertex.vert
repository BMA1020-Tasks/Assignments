#version 150 core
in vec3 position;
in vec4 colors;
in vec3 translation;

out vec4 vertex_colors;

uniform WindowBlock
{
    mat4 projection;
    mat4 view;
} window;

uniform mat4 model;
uniform mat4 u_projection;
uniform mat4 u_view;

void main()
{
    gl_Position = u_projection * u_view * vec4(position + translation, 1.0);
    vertex_colors = colors;
}