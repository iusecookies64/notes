import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Set up academic-style LaTeX fonts (matching Figures 6.3 and 6.4)
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

# ==============================================================================
# Mathematical Setup: Symmetric Positive-Definite Matrix S = Q \Lambda Q^T
# ==============================================================================
# Semi-axis lengths at z = 1: r_1 = 1/sqrt(\lambda_1), r_2 = 1/sqrt(\lambda_2)
r1 = 1.65  # Major semi-axis -> \lambda_1 = 1 / 1.65^2 \approx 0.367
r2 = 0.90  # Minor semi-axis -> \lambda_2 = 1 / 0.90^2 \approx 1.235
lam1 = 1.0 / (r1**2)
lam2 = 1.0 / (r2**2)

# Rotation angle \theta = 35 degrees for eigenvectors Q = [q_1, q_2]
theta_deg = 35
theta = np.deg2rad(theta_deg)
q1 = np.array([np.cos(theta), np.sin(theta)])
q2 = np.array([-np.sin(theta), np.cos(theta)])
Q = np.column_stack((q1, q2))
S = Q @ np.diag([lam1, lam2]) @ Q.T  # S = [[a, b], [b, c]] with a > 0, ac - b^2 > 0

# Consistent color palette (Blue, Red, Green, Dark Grey)
col_blue = '#1f618d'
col_red = '#922b21'
col_green = '#2e7d32'
col_grey = '#404040'

# Create Figure
fig = plt.figure(figsize=(13.5, 6.4))
fig.suptitle(r'$\mathbf{Figure\ 6.5\ -\ Energy\ Surface\ } z = x^T S x\ \mathbf{(Elliptic\ Paraboloid\ Bowl)\ and\ the\ Level\ Ellipse\ } x^T S x = 1$', 
             fontsize=14.5, y=0.96)

# ==============================================================================
# 1. LEFT PANEL: 3D Surface Plot of z = x^T S x (Upright Bowl)
# ==============================================================================
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.set_proj_type('ortho')  # Orthographic projection for clean textbook geometry

# Parameterize the elliptic paraboloid in polar-elliptical coordinates (h, \phi)
# so the top rim of the bowl is a clean level curve at z_max = 1.65
z_max = 1.65
h_vals = np.linspace(0, np.sqrt(z_max), 45)
phi_vals = np.linspace(0, 2 * np.pi, 80)
H, PHI = np.meshgrid(h_vals, phi_vals)

Y1 = H * r1 * np.cos(PHI)
Y2 = H * r2 * np.sin(PHI)
X1 = Q[0, 0] * Y1 + Q[0, 1] * Y2
X2 = Q[1, 0] * Y1 + Q[1, 1] * Y2
Z = H**2

# Plot the 3D paraboloid bowl
ax1.plot_surface(X1, X2, Z, cmap='Blues', alpha=0.62, edgecolor='#1f618d', 
                 lw=0.2, rstride=3, cstride=3, antialiased=True, zorder=2)

# Semi-transparent horizontal slicing plane at z = 1
plane_lim = 2.05
px, py = np.meshgrid(np.linspace(-plane_lim, plane_lim, 2), np.linspace(-plane_lim, plane_lim, 2))
pz = np.ones_like(px)
ax1.plot_surface(px, py, pz, color=col_red, alpha=0.12, shade=False, zorder=3)
# Thin border around the z = 1 slicing plane
ax1.plot([-plane_lim, plane_lim, plane_lim, -plane_lim, -plane_lim],
         [-plane_lim, -plane_lim, plane_lim, plane_lim, -plane_lim],
         [1, 1, 1, 1, 1], color=col_red, lw=0.8, alpha=0.45, ls='-')

# Level curve at z = 1 (intersection of paraboloid and plane)
t_curve = np.linspace(0, 2 * np.pi, 300)
y_ell = np.vstack((r1 * np.cos(t_curve), r2 * np.sin(t_curve)))
x_ell = Q @ y_ell

ax1.plot(x_ell[0], x_ell[1], np.ones_like(t_curve), color=col_red, lw=2.6, zorder=6)

# Projected shadow ellipse in the base plane (z = 0)
ax1.plot(x_ell[0], x_ell[1], np.zeros_like(t_curve), color=col_blue, lw=1.6, ls='--', zorder=1)

# Vertical dashed drop-lines from the 4 vertices at z = 1 down to z = 0
for v in [r1 * q1, -r1 * q1, r2 * q2, -r2 * q2]:
    ax1.plot([v[0], v[0]], [v[1], v[1]], [0, 1], color=col_grey, ls=':', lw=1.1, zorder=4)

# Eigenvector principal axis rays in the base plane z = 0
ax1.plot([0, r1 * q1[0]], [0, r1 * q1[1]], [0, 0], color=col_red, lw=2.0, zorder=5)
ax1.plot([0, r2 * q2[0]], [0, r2 * q2[1]], [0, 0], color=col_green, lw=2.0, zorder=5)
ax1.plot([0], [0], [0], 'ko', markersize=4, zorder=6)

# 3D Text Annotations
ax1.text(plane_lim - 0.1, -plane_lim + 0.1, 1.08, r'Slice $z = 1$', color=col_red, fontsize=11.5)
ax1.text(0.0, -1.5, 1.52, r'$z = x^T S x$', color=col_blue, fontsize=12.5, fontweight='bold')

# Clean up 3D axes appearance
ax1.set_xlim(-2.1, 2.1)
ax1.set_ylim(-2.1, 2.1)
ax1.set_zlim(0, 1.8)
ax1.set_xticks([-2, -1, 0, 1, 2])
ax1.set_yticks([-2, -1, 0, 1, 2])
ax1.set_zticks([0, 0.5, 1.0, 1.5])
ax1.tick_params(axis='both', which='major', labelsize=9, pad=1)
ax1.set_xlabel(r'$x_1$', fontsize=13, labelpad=-2)
ax1.set_ylabel(r'$x_2$', fontsize=13, labelpad=-2)
ax1.set_zlabel(r'$z$', fontsize=13, labelpad=-4)
ax1.view_init(elev=24, azim=-58)

# Make 3D panes clean white/light-grey
ax1.xaxis.pane.fill = False
ax1.yaxis.pane.fill = False
ax1.zaxis.pane.fill = False
ax1.grid(True, linestyle=':', alpha=0.45)

ax1.set_title("3D Energy Surface (Positive Definite " + r"$S \succ 0$)" + "\n" +
              r"$(z = a x_1^2 + 2 b x_1 x_2 + c x_2^2,\ a > 0,\ ac - b^2 > 0)$", 
              fontsize=12.5, pad=10)
ax1.text2D(0.5, -0.14, "Upright elliptic paraboloid bowl intersected by\n"
                       r"the horizontal slicing plane at height $z = 1$.",
           transform=ax1.transAxes, fontsize=11, ha='center', va='top')

# ==============================================================================
# 2. RIGHT PANEL: Horizontal Slice at z = 1 (Level Ellipse x^T S x = 1)
# ==============================================================================
ax2 = fig.add_subplot(1, 2, 2)
lim = 2.25
ax2.set_xlim(-lim, lim)
ax2.set_ylim(-lim, lim)
ax2.set_aspect('equal')

# Move spines to origin
ax2.spines['left'].set_position('zero')
ax2.spines['bottom'].set_position('zero')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['left'].set_color('#606060')
ax2.spines['bottom'].set_color('#606060')
ax2.set_xticks([])
ax2.set_yticks([])

# Axis arrowheads and labels
ax2.plot(1, 0, ">", color='#606060', transform=ax2.get_yaxis_transform(), clip_on=False, markersize=5)
ax2.plot(0, 1, "^", color='#606060', transform=ax2.get_xaxis_transform(), clip_on=False, markersize=5)
ax2.text(lim - 0.05, -0.26, r'$x_1$', fontsize=14, ha='right')
ax2.text(-0.30, lim - 0.05, r'$x_2$', fontsize=14, va='top')
ax2.plot(0, 0, 'ko', markersize=4.5, zorder=6)

# Faint inner energy contours (z = 0.25, 0.5, 0.75) to reinforce the 3D bowl slice
for z_sub in [0.25, 0.5, 0.75]:
    scale = np.sqrt(z_sub)
    ax2.plot(scale * x_ell[0], scale * x_ell[1], color=col_blue, ls=':', lw=0.9, alpha=0.45, zorder=1)

# Principal Axes Lines (dashed grey extensions along q_1 and q_2)
ext = 2.05
ax2.plot([-ext * q1[0], ext * q1[0]], [-ext * q1[1], ext * q1[1]], color=col_grey, ls='--', lw=1.2, zorder=2)
ax2.plot([-ext * q2[0], ext * q2[0]], [-ext * q2[1], ext * q2[1]], color=col_grey, ls='--', lw=1.2, zorder=2)

# Level Ellipse x^T S x = 1 (matching the red z = 1 intersection curve from 3D panel)
ax2.plot(x_ell[0], x_ell[1], color=col_red, lw=2.4, zorder=3)
ax2.fill(x_ell[0], x_ell[1], color=col_blue, alpha=0.06, zorder=1)

# Orthogonality right-angle marker at origin
sq = 0.20
ra_pts = np.array([sq * q1, sq * (q1 + q2), sq * q2])
ax2.plot(ra_pts[:, 0], ra_pts[:, 1], color=col_grey, lw=1.1, zorder=2)

# Unit Eigenvectors q_1 (Red) and q_2 (Green)
ax2.annotate('', xy=(q1[0], q1[1]), xytext=(0, 0),
             arrowprops=dict(arrowstyle="-|>", color=col_red, lw=2.2, mutation_scale=15), zorder=5)
ax2.text(q1[0] * 0.62 + 0.12, q1[1] * 0.62 - 0.18, r'$\mathbf{q_1}$', color=col_red, fontsize=13)

ax2.annotate('', xy=(q2[0], q2[1]), xytext=(0, 0),
             arrowprops=dict(arrowstyle="-|>", color=col_green, lw=2.2, mutation_scale=15), zorder=5)
ax2.text(q2[0] * 0.65 - 0.28, q2[1] * 0.65 - 0.05, r'$\mathbf{q_2}$', color=col_green, fontsize=13)

# Dimension Callouts for Semi-Axes 1/sqrt(\lambda_1) and 1/sqrt(\lambda_2)
offset_1 = -0.34 * q2
p0_1, p1_1 = offset_1, -r1 * q1 + offset_1
ax2.plot([0, p0_1[0]], [0, p0_1[1]], color=col_grey, ls=':', lw=0.9)
ax2.plot([-r1 * q1[0], p1_1[0]], [-r1 * q1[1], p1_1[1]], color=col_grey, ls=':', lw=0.9)
ax2.annotate('', xy=p1_1, xytext=p0_1,
             arrowprops=dict(arrowstyle="<->", color=col_red, lw=1.4, mutation_scale=11), zorder=4)
mid_1 = 0.5 * (p0_1 + p1_1) - 0.26 * q2
ax2.text(mid_1[0], mid_1[1], r'$\frac{1}{\sqrt{\lambda_1}}$', color=col_red, fontsize=13, ha='center', va='center')

offset_2 = 0.42 * q1
p0_2, p1_2 = offset_2, -r2 * q2 + offset_2
ax2.plot([0, p0_2[0]], [0, p0_2[1]], color=col_grey, ls=':', lw=0.9)
ax2.plot([-r2 * q2[0], p1_2[0]], [-r2 * q2[1], p1_2[1]], color=col_grey, ls=':', lw=0.9)
ax2.annotate('', xy=p1_2, xytext=p0_2,
             arrowprops=dict(arrowstyle="<->", color=col_green, lw=1.4, mutation_scale=11), zorder=4)
mid_2 = 0.5 * (p0_2 + p1_2) + 0.32 * q1
ax2.text(mid_2[0], mid_2[1], r'$\frac{1}{\sqrt{\lambda_2}}$', color=col_green, fontsize=13, ha='center', va='center')

# Highlight the 4 principal vertices
for v in [r1 * q1, -r1 * q1, r2 * q2, -r2 * q2]:
    ax2.plot(v[0], v[1], 'ko', markersize=4, zorder=5)

# Rotation angle arc \theta
arc = Arc((0, 0), 0.85, 0.85, angle=0, theta1=0, theta2=theta_deg, color=col_grey, lw=1.1)
ax2.add_patch(arc)
ax2.text(0.52 * np.cos(theta / 2), 0.52 * np.sin(theta / 2), r'$\theta$', fontsize=11, color=col_grey, ha='center', va='center')

# Callout pointing to the z = 1 level curve
pt_label = Q @ np.array([r1 * np.cos(np.deg2rad(50)), r2 * np.sin(np.deg2rad(50))])
ax2.annotate(r'Level Curve $x^T S x = 1$' + '\n' + r'$(z = 1\ \mathrm{slice})$', 
             xy=(pt_label[0], pt_label[1]), xytext=(0.65, 1.65),
             fontsize=11.5, color=col_red,
             arrowprops=dict(arrowstyle="->", color=col_red, lw=1.2, connectionstyle="arc3,rad=-0.15"))

ax2.set_title("Horizontal Slice at " + r"$z = 1$" + "\n" + r"$(x^T S x = \lambda_1 y_1^2 + \lambda_2 y_2^2 = 1)$", 
              fontsize=12.5, pad=16)
ax2.text(0, -2.56, r"The level ellipse aligns with eigenvectors $q_1, q_2$" + "\n" +
                   r"with semi-axis half-lengths $1/\sqrt{\lambda_1}$ and $1/\sqrt{\lambda_2}$.", 
         fontsize=11, ha='center', va='top')

plt.tight_layout()
plt.subplots_adjust(top=0.80, bottom=0.18, wspace=0.18)

# Save high-resolution PNG and lossless vector PDF
plt.savefig("figure_6_5_energy_surface_bowl.png", dpi=300, bbox_inches='tight')
plt.savefig("figure_6_5_energy_surface_bowl.pdf", bbox_inches='tight')
plt.show()