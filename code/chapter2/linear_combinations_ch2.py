"""
3Blue1Brown — Essence of Linear Algebra
Chapter 2: Linear Combinations, Span & Basis Vectors
=====================================================
Run section by section. Each block builds on the last.
Requirements: numpy, matplotlib  (pip install numpy matplotlib)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import warnings
warnings.filterwarnings('ignore')
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
PURPLE = '#6a4c93'; RED = '#c0392b'

def arrow(ax, vec, color, label=None, origin=(0,0), lw=2.5, alpha=1.0):
    ax.annotate("", xy=(origin[0]+vec[0], origin[1]+vec[1]), xytext=origin,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                        mutation_scale=16, alpha=alpha))
    if label:
        ax.text(origin[0]+vec[0]/2+0.12, origin[1]+vec[1]/2+0.12,
                label, color=color, fontsize=10, fontweight='bold', alpha=alpha)

def setup_ax(ax, xlim=(-4,4), ylim=(-4,4), title=""):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axhline(0, color='#888', lw=1.2); ax.axvline(0, color='#888', lw=1.2)
    ax.set_aspect('equal'); ax.set_title(title, pad=10, fontsize=11)

# ═══════════════════════════════════════════════════════════════════
# SECTION 1 — i-hat and j-hat: the standard basis
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("SECTION 1 — î and ĵ: the standard basis vectors")
print("=" * 60)

i_hat = np.array([1, 0])   # x basis vector
j_hat = np.array([0, 1])   # y basis vector

print(f"î (i-hat) = {i_hat}  ← one step RIGHT")
print(f"ĵ (j-hat) = {j_hat}  ← one step UP")
print()

# Any vector is a linear combination of i_hat and j_hat
v = np.array([3, 2])
a, b = v[0], v[1]
reconstructed = a * i_hat + b * j_hat

print(f"Vector v = {v}")
print(f"  = {a}·î + {b}·ĵ")
print(f"  = {a}·{i_hat} + {b}·{j_hat}")
print(f"  = {a*i_hat} + {b*j_hat}")
print(f"  = {reconstructed}  ✓ same as v")
print()
print("Key insight: the numbers in [3, 2] ARE the scalars")
print("for î and ĵ. Coordinates = linear combination instructions.")

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
setup_ax(ax, (-1,5), (-1,4), "v = 3·î + 2·ĵ  (decomposing into basis vectors)")

# Show scaled basis vectors
arrow(ax, 3*i_hat, ORANGE, "3·î", lw=2)
arrow(ax, 2*j_hat, BLUE, "2·ĵ", origin=tuple(3*i_hat), lw=2)
# Show the result
arrow(ax, v, GREEN, "v = [3,2]", lw=3)

ax.plot(0,0,'o', color=GREEN, ms=7)
ax.plot(*v,'o', color=GREEN, ms=7)
ax.text(0.5,-0.35,"î=[1,0]", color=ORANGE, fontsize=9)
ax.text(-0.35,0.5,"ĵ=[0,1]", color=BLUE, fontsize=9)

# Draw small basis vectors
arrow(ax, i_hat, ORANGE, alpha=0.5, lw=1.5)
arrow(ax, j_hat, BLUE, alpha=0.5, lw=1.5)

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "ch2_plot1_basis.png"), dpi=130, bbox_inches='tight')
plt.close()
print("\n→ Saved: ch2_plot1_basis.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 2 — Linear combinations: varying the scalars
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 2 — Linear Combinations: a·v + b·w")
print("=" * 60)

v = np.array([1, 2])
w = np.array([3, 0])

print(f"v = {v},  w = {w}")
print()
print("Linear combination: a·v + b·w  (vary a and b)")
print()

combos = [
    (1, 0,  "1·v + 0·w"),
    (0, 1,  "0·v + 1·w"),
    (1, 1,  "1·v + 1·w"),
    (2, -1, "2·v + (−1)·w"),
    (0.5, 0.5, "0.5·v + 0.5·w"),
]
for a, b, label in combos:
    result = a*v + b*w
    print(f"  {label:25s} = {a}·{v} + {b}·{w} = {result}")

# ═══════════════════════════════════════════════════════════════════
# SECTION 3 — Visualising SPAN
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 3 — Span: what region of space can you reach?")
print("=" * 60)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Span: the set of all reachable vectors from linear combinations", 
             fontsize=12, y=1.01)

# ── Case 1: Two independent vectors → span = full 2D plane ────────
ax = axes[0]
setup_ax(ax, title="Case 1: Independent vectors\nSpan = entire 2D plane")
v1 = np.array([2, 1]); v2 = np.array([0.5, 2])

# Fill the plane
ax.fill_between([-4,4], -4, 4, color='#e8f4ee', alpha=0.5, zorder=0)
ax.text(0, 3.3, "All of 2D space ✓", ha='center', color=GREEN, fontsize=9, fontweight='bold')

# Show many linear combinations
np.random.seed(42)
for _ in range(120):
    a = np.random.uniform(-2, 2)
    b = np.random.uniform(-2, 2)
    pt = a*v1 + b*v2
    ax.plot(*pt, '.', color=GREEN, ms=3, alpha=0.4)

arrow(ax, v1, ORANGE, "v")
arrow(ax, v2, BLUE, "w")

# ── Case 2: Parallel (dependent) vectors → span = one line ────────
ax = axes[1]
setup_ax(ax, title="Case 2: Dependent vectors\nSpan = one line only")
v1 = np.array([2, 1]); v2 = np.array([4, 2])   # v2 = 2*v1

# Draw the line
t = np.linspace(-2, 2, 100)
line_pts = np.array([t_*v1 for t_ in t])
ax.plot(line_pts[:,0], line_pts[:,1], color=GREEN, lw=3, alpha=0.4)

# Show many combos — all land on the same line
for a in np.linspace(-1.5, 1.5, 20):
    for b in np.linspace(-0.8, 0.8, 10):
        pt = a*v1 + b*v2
        ax.plot(*pt, '.', color=GREEN, ms=3, alpha=0.35)

arrow(ax, v1, ORANGE, "v=[2,1]")
arrow(ax, v2, BLUE, "w=[4,2]", lw=1.5, alpha=0.5)
ax.text(0, -3.3, "w = 2·v  →  linearly dependent", ha='center', 
        color=RED, fontsize=9, fontweight='bold')

# ── Case 3: Three vectors in 2D — third is redundant ──────────────
ax = axes[2]
setup_ax(ax, title="Case 3: Three vectors in 2D\nSpan = plane (third is redundant)")
v1 = np.array([2, 0]); v2 = np.array([0, 2]); v3 = np.array([1, 1])  # v3 = 0.5v1+0.5v2

ax.fill_between([-4,4], -4, 4, color='#eef3f8', alpha=0.5, zorder=0)
ax.text(0, 3.3, "Span = 2D plane (same as 2 vectors)", ha='center', 
        color=BLUE, fontsize=9)
arrow(ax, v1, ORANGE, "v₁")
arrow(ax, v2, BLUE, "v₂")
arrow(ax, v3, PURPLE, "v₃=0.5v₁+0.5v₂", lw=1.5, alpha=0.7)
ax.text(0, -3.3, "v₃ is redundant — linearly dependent", ha='center',
        color=PURPLE, fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "ch2_plot2_span.png"), dpi=130, bbox_inches='tight')
plt.close()
print("→ Saved: ch2_plot2_span.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 4 — Detecting linear dependence mathematically
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 4 — Detecting Linear Dependence (the determinant hint)")
print("=" * 60)

def are_independent_2d(v, w):
    """Two 2D vectors are independent iff the 2x2 matrix they form has non-zero determinant."""
    matrix = np.column_stack([v, w])   # put vectors as columns
    det = np.linalg.det(matrix)
    return det, abs(det) > 1e-10

test_pairs = [
    (np.array([1, 0]), np.array([0, 1]),  "î and ĵ (standard basis)"),
    (np.array([2, 1]), np.array([0.5, 2]), "random independent pair"),
    (np.array([2, 1]), np.array([4, 2]),   "dependent: v2 = 2*v1"),
    (np.array([3, 1]), np.array([1, 3]),   "another independent pair"),
    (np.array([1, 2]), np.array([-2, -4]), "dependent: v2 = -2*v1"),
]

print(f"{'Vectors':45s} {'Det':>8}  Independent?")
print("-" * 65)
for v, w, desc in test_pairs:
    det, indep = are_independent_2d(v, w)
    print(f"  {desc:43s} {det:>8.2f}  {'✓ YES' if indep else '✗ NO (dependent)'}")

print()
print("Rule: det ≠ 0  →  independent  →  span = full plane")
print("      det = 0  →  dependent    →  span = just a line")
print()
print("(We'll explore determinants properly in Chapter 5!)")

# ═══════════════════════════════════════════════════════════════════
# SECTION 5 — Changing the basis
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 5 — Custom Basis: coordinates depend on your choice of basis")
print("=" * 60)

# Standard basis
i_hat = np.array([1, 0])
j_hat = np.array([0, 1])

# A custom (non-standard) basis
b1 = np.array([2, 1])   # new "x direction"
b2 = np.array([-1, 2])  # new "y direction"

# Same point in space, described in two different bases
# In standard basis, the point [4, 3] has coordinates (4, 3)
point_standard = np.array([4, 3])

# Find the coordinates of the same point in the custom basis
# Solve: a*b1 + b*b2 = point_standard
# i.e. [b1 | b2] * [a, b]^T = point_standard
B = np.column_stack([b1, b2])
coords_in_custom = np.linalg.solve(B, point_standard)

print(f"Point in standard coordinates: {point_standard}")
print(f"Custom basis: b1={b1}, b2={b2}")
print(f"Same point in custom coordinates: {coords_in_custom.round(4)}")
print()
print(f"Verify: {coords_in_custom[0]:.4f}·{b1} + {coords_in_custom[1]:.4f}·{b2}")
print(f"      = {coords_in_custom[0]*b1} + {coords_in_custom[1]*b2}")
print(f"      = {coords_in_custom[0]*b1 + coords_in_custom[1]*b2}  ✓")

# Plot the two basis systems
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

for ax, (bv1, bv2, title, coords, color_b1, color_b2) in zip(axes, [
    (i_hat, j_hat, "Standard basis: î=[1,0], ĵ=[0,1]",
     point_standard, ORANGE, BLUE),
    (b1, b2, "Custom basis: b₁=[2,1], b₂=[−1,2]",
     coords_in_custom, ORANGE, BLUE),
]):
    setup_ax(ax, (-3, 6), (-3, 6), title)

    # Draw basis vectors
    arrow(ax, bv1, color_b1, f"b₁={bv1}", lw=2)
    arrow(ax, bv2, color_b2, f"b₂={bv2}", lw=2)

    # Show the point
    ax.plot(*point_standard, 'o', color=GREEN, ms=10, zorder=5)
    ax.text(point_standard[0]+0.15, point_standard[1]+0.15,
            f"same point\n[4,3] in standard", color=GREEN, fontsize=9)

    # Show coordinates
    ax.text(0.05, 0.05, f"Coordinates: ({coords[0]:.2f}, {coords[1]:.2f})",
            transform=ax.transAxes, fontsize=9, color='#555',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "ch2_plot3_basis_change.png"), dpi=130, bbox_inches='tight')
plt.close()
print("\n→ Saved: ch2_plot3_basis_change.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 6 — 3D span (bonus)
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 6 — Span in 3D (bonus)")
print("=" * 60)

# Three vectors in 3D
v1 = np.array([1, 0, 0])  # x axis
v2 = np.array([0, 1, 0])  # y axis
v3 = np.array([0, 0, 1])  # z axis

print("Three 3D vectors:")
print(f"  v1 = {v1}")
print(f"  v2 = {v2}")
print(f"  v3 = {v3}")
print()

# Check independence using rank
M = np.row_stack([v1, v2, v3])
rank = np.linalg.matrix_rank(M)
print(f"Matrix of vectors:\n{M}")
print(f"Rank = {rank}")
print(f"→ Rank = 3 = number of vectors → linearly independent → span = all of 3D space ✓")
print()

# Now try a dependent set
v4 = v1 + v2    # dependent: can be made from v1 and v2
M2 = np.row_stack([v1, v2, v4])
rank2 = np.linalg.matrix_rank(M2)
print(f"Swapping v3 for v4={v4} (= v1 + v2):")
print(f"New matrix rank = {rank2}")
print(f"→ Rank = {rank2} < 3 → linearly dependent → span = only a 2D plane inside 3D space")
print()
print("Rule: rank tells you the dimension of the span.")
print("  rank 1 → span is a line")
print("  rank 2 → span is a plane")
print("  rank 3 → span is all of 3D space")

# ═══════════════════════════════════════════════════════════════════
# SECTION 7 — Connection to AI: word embeddings
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("SECTION 7 — Basis & Span in AI (preview of Chapter 6 and beyond)")
print("=" * 60)

print("""
In a 768-dimensional embedding space (like BERT):

  • The BASIS has 768 vectors — 768 independent "directions"
  • Every word/sentence embedding is a LINEAR COMBINATION of these
  • The "king - man + woman ≈ queen" analogy from Chapter 1 is
    vector addition — moving along different basis directions

PCA (Principal Component Analysis) in ML:
  • Finds a NEW BASIS where the first basis vector points in the
    direction of most variation in your data
  • This is called a "change of basis" — the same concept as
    Section 5 above, but applied to thousands of data points

Neural network layers:
  • Each layer takes the current vector (the "input embedding")
    and produces a new linear combination → a transformed vector
  • That's all a linear layer is: a·v₁ + b·v₂ + c·v₃ + ...
    with learned weights a, b, c, ...

You now understand the building blocks of all of this!
""")

print("=" * 60)
print("ALL DONE! Files saved:")
print("  ch2_plot1_basis.png        — î, ĵ decomposition")
print("  ch2_plot2_span.png         — span in 3 cases")
print("  ch2_plot3_basis_change.png — standard vs custom basis")
print("=" * 60)
print("""
Exercises to try:
  1. Change v = np.array([1,2]) and w = np.array([3,0]) in Section 2
     and print several more linear combinations manually
  2. In Section 4, make up your own pair of vectors and check if they're
     independent using the determinant
  3. In Section 5, try a custom basis b1=[1,1], b2=[1,-1] and find
     where [3,1] lives in that new coordinate system
""")