"""
3Blue1Brown — Essence of Linear Algebra
Chapter 3: Linear Transformations & Matrices
=============================================
Run section by section. Each block builds on the last.
Requirements: numpy, matplotlib  (pip install numpy matplotlib)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# Use a workspace-local outputs directory so the script can write files
outputs_dir = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(outputs_dir, exist_ok=True)

plt.rcParams.update({
    'figure.facecolor': '#faf8f3', 'axes.facecolor': '#faf8f3',
    'axes.edgecolor': '#ccc', 'axes.grid': True,
    'grid.color': '#e0ddd5', 'grid.linewidth': 0.6,
    'font.family': 'DejaVu Sans', 'font.size': 11,
})
GREEN = '#2d6a4f'; ORANGE = '#e76f51'; BLUE = '#457b9d'
PURPLE = '#6a4c93'; RED = '#c0392b'; GRAY = '#888'

# ── helpers ───────────────────────────────────────────────────────
def arrow(ax, vec, color, label=None, origin=(0,0), lw=2.5, alpha=1.0, fs=10):
    ax.annotate("", xy=(origin[0]+vec[0], origin[1]+vec[1]), xytext=origin,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                        mutation_scale=16, alpha=alpha))
    if label:
        ax.text(origin[0]+vec[0]/2+0.12, origin[1]+vec[1]/2+0.12,
                label, color=color, fontsize=fs, fontweight='bold', alpha=alpha)

def setup_ax(ax, xlim=(-3,3), ylim=(-3,3), title=""):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axhline(0, color='#888', lw=1.2); ax.axvline(0, color='#888', lw=1.2)
    ax.set_aspect('equal'); ax.set_title(title, pad=10, fontsize=11)

def apply_transform(M, vectors):
    """Apply matrix M to each column vector in `vectors` (list of 1D arrays)."""
    return [M @ v for v in vectors]

def draw_grid(ax, M, color='#c8e6d8', lw=0.6, n=5):
    """Draw the transformed grid lines."""
    for i in range(-n, n+1):
        # horizontal lines y=i
        p1 = M @ np.array([-n, i])
        p2 = M @ np.array([ n, i])
        ax.plot([p1[0],p2[0]], [p1[1],p2[1]], color=color, lw=lw, zorder=0)
        # vertical lines x=i
        p3 = M @ np.array([i, -n])
        p4 = M @ np.array([i,  n])
        ax.plot([p3[0],p4[0]], [p3[1],p4[1]], color=color, lw=lw, zorder=0)

# ═══════════════════════════════════════════════════════════════════
# SECTION 1 — What makes a transformation "linear"?
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("SECTION 1 — Linear vs Non-linear transformations")
print("=" * 60)

# Test the two rules of linearity:
# 1. T(v + w) = T(v) + T(w)   (additivity)
# 2. T(a*v)   = a * T(v)       (scaling)

def test_linearity(T_func, name, v=None, w=None, a=2):
    if v is None: v = np.array([1.0, 2.0])
    if w is None: w = np.array([3.0, -1.0])
    rule1_lhs = T_func(v + w)
    rule1_rhs = T_func(v) + T_func(w)
    rule2_lhs = T_func(a * v)
    rule2_rhs = a * T_func(v)
    add_ok   = np.allclose(rule1_lhs, rule1_rhs)
    scale_ok = np.allclose(rule2_lhs, rule2_rhs)
    linear   = add_ok and scale_ok
    print(f"  {name:30s}  additive={add_ok}  scaling={scale_ok}  → {'LINEAR ✓' if linear else 'NOT LINEAR ✗'}")

# 2×2 rotation matrix (90°)
M_rot = np.array([[0, -1], [1, 0]])
T_rotate   = lambda v: M_rot @ v
T_scale2   = lambda v: 2 * v
T_shear    = lambda v: np.array([v[0] + v[1], v[1]])
T_nonlin1  = lambda v: v + np.array([2.0, 1.0])   # shift — moves origin
T_nonlin2  = lambda v: v ** 2                       # squaring — bends lines

print("Testing the two rules of linearity on 5 transformations:\n")
test_linearity(T_rotate,  "Rotate 90°")
test_linearity(T_scale2,  "Scale by 2")
test_linearity(T_shear,   "Shear")
test_linearity(T_nonlin1, "Shift by [2,1]  (NOT linear)")
test_linearity(T_nonlin2, "Square each element (NOT linear)")

# ═══════════════════════════════════════════════════════════════════
# SECTION 2 — Matrices as transformations: track î and ĵ
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 2 — A matrix = where î and ĵ land")
print("=" * 60)

i_hat = np.array([1, 0])
j_hat = np.array([0, 1])

# Define a transformation by specifying where basis vectors land
i_lands = np.array([1, -2])   # î goes here
j_lands = np.array([3,  0])   # ĵ goes here

# The matrix is just those two vectors as COLUMNS
M = np.column_stack([i_lands, j_lands])
print(f"î lands at: {i_lands}")
print(f"ĵ lands at: {j_lands}")
print(f"\nMatrix M (columns = destinations of î and ĵ):")
print(M)

# Now transform any vector using the matrix
v = np.array([4, 3])
result_matrix = M @ v
result_manual = v[0] * i_lands + v[1] * j_lands   # same thing!

print(f"\nTransform v = {v}:")
print(f"  Matrix multiply M @ v    = {result_matrix}")
print(f"  Manual: {v[0]}·î_new + {v[1]}·ĵ_new = {v[0]}·{i_lands} + {v[1]}·{j_lands} = {result_manual}")
print(f"  Same result? {np.allclose(result_matrix, result_manual)} ✓")
print()
print("Key: matrix multiplication IS the linear combination formula.")
print("The matrix is just a compact way to store the transformation.")

# ═══════════════════════════════════════════════════════════════════
# SECTION 3 — Common transformations visualised
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 3 — Common 2D Transformations")
print("=" * 60)

transforms = {
    "Identity":          (np.array([[1,0],[0,1]]),  GREEN,  "Nothing moves"),
    "Rotate 90° CCW":    (np.array([[0,-1],[1,0]]), BLUE,   "î→[0,1], ĵ→[-1,0]"),
    "Shear":             (np.array([[1,1],[0,1]]),  PURPLE, "î stays, ĵ→[1,1]"),
    "Scale ×2":          (np.array([[2,0],[0,2]]),  ORANGE, "Every vector doubles"),
    "Reflect x-axis":    (np.array([[1,0],[0,-1]]), RED,    "î stays, ĵ flips"),
    "Squish to line":    (np.array([[1,1],[0,0]]),  GRAY,   "Entire plane→x-axis"),
}

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle("6 Common Linear Transformations\n(green = î, blue = ĵ, dashed = original)", 
             fontsize=13, y=1.01)

sample_v = np.array([2, 1])   # sample vector to transform

for ax, (name, (M, color, desc)) in zip(axes.flat, transforms.items()):
    setup_ax(ax, (-3,3), (-3,3), f"{name}\n{desc}")

    # Draw original grid (faint)
    draw_grid(ax, np.eye(2), color='#e8e4da', lw=0.4)
    # Draw transformed grid
    draw_grid(ax, M, color='#c5dfd0', lw=0.6)

    # Original basis (dashed)
    arrow(ax, i_hat, ORANGE, alpha=0.3, lw=1.5)
    arrow(ax, j_hat, BLUE,   alpha=0.3, lw=1.5)
    # Original sample vector (dashed)
    arrow(ax, sample_v, GREEN, alpha=0.25, lw=1.5)

    # Transformed basis
    i_new = M @ i_hat
    j_new = M @ j_hat
    v_new = M @ sample_v

    arrow(ax, i_new, ORANGE, f"î→{i_new.tolist()}", lw=2.5)
    arrow(ax, j_new, BLUE,   f"ĵ→{j_new.tolist()}", lw=2.5)
    arrow(ax, v_new, GREEN,  f"v→{v_new.tolist()}", lw=2)

    ax.plot(0,0,'ko', ms=5, zorder=5)

    # Show matrix in corner
    ax.text(-2.9, 2.4,
            f"M=[{M[0][0]} {M[0][1]}; {M[1][0]} {M[1][1]}]",
            fontsize=8, color='#555', family='monospace')

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "ch3_plot1_transforms.png"), dpi=130, bbox_inches='tight')
plt.close()
print("→ Saved: ch3_plot1_transforms.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 4 — Matrix-vector multiplication step by step
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 4 — Matrix × Vector: step-by-step breakdown")
print("=" * 60)

def mv_multiply_verbose(M, v):
    """Show matrix-vector multiplication step by step."""
    print(f"\n  M = {M[0]}    v = [{v[0]}]")
    print(f"      {M[1]}        [{v[1]}]")
    print()
    # Column interpretation
    col1, col2 = M[:,0], M[:,1]
    scaled1 = v[0] * col1
    scaled2 = v[1] * col2
    result  = scaled1 + scaled2
    print(f"  = {v[0]} · col1  +  {v[1]} · col2")
    print(f"  = {v[0]} · {col1}  +  {v[1]} · {col2}")
    print(f"  = {scaled1}  +  {scaled2}")
    print(f"  = {result}")
    return result

examples = [
    (np.array([[1,0],[0,1]]), np.array([3,2]),   "Identity × [3,2]"),
    (np.array([[0,-1],[1,0]]),np.array([1,0]),   "Rotate90 × î=[1,0]"),
    (np.array([[2,0],[0,2]]), np.array([3,1]),   "Scale×2  × [3,1]"),
    (np.array([[1,1],[0,1]]), np.array([2,3]),   "Shear    × [2,3]"),
]

for M, v, label in examples:
    print(f"\n  {label}:")
    mv_multiply_verbose(M, v)

# ═══════════════════════════════════════════════════════════════════
# SECTION 5 — Visualising a transformation and its effect on a shape
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 5 — Transformation effect on a shape (a unit square)")
print("=" * 60)

# Unit square corners
square = np.array([[0,1,1,0,0],
                   [0,0,1,1,0]], dtype=float)  # 2×5

M_shear = np.array([[1, 1],
                    [0, 1]])
sheared = M_shear @ square

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Effect of a Shear transformation on a unit square", fontsize=13)

# Before
setup_ax(ax1, (-0.5, 3), (-0.5, 3), "Before transformation")
ax1.fill(square[0], square[1], color='#c5dfd0', alpha=0.5)
ax1.plot(square[0], square[1], color=GREEN, lw=2)
arrow(ax1, i_hat, ORANGE, "î=[1,0]", lw=2)
arrow(ax1, j_hat, BLUE,   "ĵ=[0,1]", lw=2)
ax1.plot(0,0,'ko',ms=5)

# After
setup_ax(ax2, (-0.5, 3.5), (-0.5, 3), "After shear: M=[[1,1],[0,1]]")
ax2.fill(sheared[0], sheared[1], color='#fde8de', alpha=0.5)
ax2.plot(sheared[0], sheared[1], color=ORANGE, lw=2)
i_new = M_shear @ i_hat
j_new = M_shear @ j_hat
arrow(ax2, i_new, ORANGE, f"î→{i_new.tolist()}", lw=2)
arrow(ax2, j_new, BLUE,   f"ĵ→{j_new.tolist()}", lw=2)
ax2.plot(0,0,'ko',ms=5)
ax2.text(0.8, 0.4, "Square\nbecomes\na parallelogram",
         fontsize=9, color='#555')

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "ch3_plot2_shear_square.png"), dpi=130, bbox_inches='tight')
plt.close()
print("→ Saved: ch3_plot2_shear_square.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 6 — Connection to AI: the neural network linear layer
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 6 — Connection to AI: Neural Network Linear Layers")
print("=" * 60)

print("""
A neural network 'Linear' or 'Dense' layer does exactly this:

  output = W · input + b

  W  = weight matrix  (a learned linear transformation)
  b  = bias vector    (a translation — added AFTER the linear part)
  input  = the input vector (e.g. a word embedding)
  output = the transformed vector passed to the next layer

Example: transforming a 4-dim input to a 3-dim output
""")

np.random.seed(42)
W = np.random.randn(3, 4).round(2)   # 3×4 weight matrix
b = np.random.randn(3).round(2)       # 3-dim bias
x = np.array([0.5, -1.2, 0.8, 0.3])  # 4-dim input

output_linear = W @ x           # linear part: matrix multiplication
output_full   = W @ x + b       # full layer: linear + bias

print(f"  Input  (4-dim): {x}")
print(f"\n  Weight matrix W (3×4):")
for row in W:
    print(f"    {row}")
print(f"\n  Bias b (3-dim): {b}")
print(f"\n  W @ x        (linear only) = {output_linear.round(3)}")
print(f"  W @ x + b    (full layer)  = {output_full.round(3)}")
print()
print("  The weight matrix W defines a linear transformation from")
print("  4D space → 3D space. Each row of W is a different direction")
print("  in the output space that the layer 'projects onto'.")
print()
print("  In a deep network with layers W1, W2, W3:")
print("  output = W3 · (W2 · (W1 · input))")
print("  = three linear transformations applied one after another")
print("  (Chapter 4 will show this is equivalent to one big matrix!)")

# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("ALL DONE! Files saved:")
print("  ch3_plot1_transforms.png   — 6 common transformations")
print("  ch3_plot2_shear_square.png — shear effect on a square")
print("=" * 60)
print("""
Exercises to try:
  1. In Section 2, change i_lands and j_lands to define your own
     transformation. What does [2,3] map to?

  2. In Section 3, add a 'Rotate 45°' transformation:
     angle = np.pi/4
     M_rot45 = np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle),  np.cos(angle)]])
     What happens to î and ĵ?

  3. In Section 5, change M_shear to the rotation matrix and
     see what a rotated square looks like.

  4. Create a 3×3 identity matrix: np.eye(3)
     Apply it to [1, 2, 3] — what happens?
""")