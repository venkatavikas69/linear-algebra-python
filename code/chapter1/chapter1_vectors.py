"""
3Blue1Brown — Essence of Linear Algebra
Chapter 1: Vectors — Python Practice
=====================================
Run this file top to bottom. Each section matches the video.
You need: numpy, matplotlib  (pip install numpy matplotlib)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import os

# Use a workspace-local outputs directory so the script can write files
outputs_dir = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(outputs_dir, exist_ok=True)

# ── nice plot style ───────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': '#faf8f3',
    'axes.facecolor':   '#faf8f3',
    'axes.edgecolor':   '#ccc',
    'axes.grid':        True,
    'grid.color':       '#e0ddd5',
    'grid.linewidth':   0.6,
    'font.family':      'DejaVu Sans',
    'font.size':        11,
})

GREEN  = '#2d6a4f'
ORANGE = '#e76f51'
BLUE   = '#457b9d'
PURPLE = '#6a4c93'

# ═══════════════════════════════════════════════════════════════════
# SECTION 1 — Creating vectors with NumPy
# ═══════════════════════════════════════════════════════════════════
print("=" * 55)
print("SECTION 1 — What is a vector?")
print("=" * 55)

# A vector is just a 1D NumPy array
v = np.array([3, 2])
print(f"Vector v         = {v}")
print(f"Type             = {type(v)}")
print(f"Shape            = {v.shape}   ← 1D array with 2 elements")
print(f"First element    = {v[0]}   ← x-coordinate (right/left)")
print(f"Second element   = {v[1]}   ← y-coordinate (up/down)")

# 3D vector
w = np.array([1, -3, 2])
print(f"\n3D vector w      = {w}")
print(f"Shape            = {w.shape}   ← 3 coordinates (x, y, z)")

# ═══════════════════════════════════════════════════════════════════
# SECTION 2 — Visualise a vector as an arrow from the origin
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("SECTION 2 — Plotting a vector as an arrow")
print("=" * 55)

def draw_vector(ax, vec, color=GREEN, label=None, origin=(0, 0)):
    """Draw a 2D vector as an arrow from `origin`."""
    ax.annotate(
        "", xy=(origin[0] + vec[0], origin[1] + vec[1]),
        xytext=origin,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=16)
    )
    if label:
        mid_x = origin[0] + vec[0] / 2
        mid_y = origin[1] + vec[1] / 2
        ax.text(mid_x + 0.15, mid_y + 0.15, label, color=color, fontsize=11, fontweight='bold')

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 5); ax.set_ylim(-1, 4)
ax.axhline(0, color='#aaa', lw=1.2); ax.axvline(0, color='#aaa', lw=1.2)
ax.set_xlabel("x axis"); ax.set_ylabel("y axis")
ax.set_title("Vector v = [3, 2] as an arrow from the origin", pad=12)
ax.set_aspect('equal')

v = np.array([3, 2])
draw_vector(ax, v, GREEN, "v = [3, 2]")

# Mark the tip
ax.plot(v[0], v[1], 'o', color=GREEN, markersize=7)
ax.plot(0, 0,       'o', color=GREEN, markersize=7)

# Show x and y components with dashed lines
ax.annotate("", xy=(v[0], 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5,
                            linestyle='dashed', mutation_scale=12))
ax.annotate("", xy=(v[0], v[1]), xytext=(v[0], 0),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.5,
                            linestyle='dashed', mutation_scale=12))
ax.text(1.5, -0.35, "3 right (x component)", color=ORANGE, fontsize=9)
ax.text(v[0] + 0.1, 1,  "2 up\n(y comp)", color=BLUE, fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "plot1_vector.png"), dpi=130, bbox_inches='tight')
plt.close()
print("→ Saved: plot1_vector.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 3 — Vector addition
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("SECTION 3 — Vector Addition (tip-to-tail rule)")
print("=" * 55)

a = np.array([1, 2])
b = np.array([3, -1])
result = a + b          # NumPy adds element-by-element

print(f"a          = {a}")
print(f"b          = {b}")
print(f"a + b      = {result}   ← [1+3, 2+(-1)]")
print()
print("Rule: add vectors by adding each element separately.")
print(f"  x: {a[0]} + {b[0]} = {a[0]+b[0]}")
print(f"  y: {a[1]} + {b[1]} = {a[1]+b[1]}")

# Plot tip-to-tail
fig, ax = plt.subplots(figsize=(7, 6))
ax.set_xlim(-0.5, 5.5); ax.set_ylim(-1.5, 3.5)
ax.axhline(0, color='#aaa', lw=1.2); ax.axvline(0, color='#aaa', lw=1.2)
ax.set_title("Vector Addition: a + b (tip-to-tail)", pad=12)
ax.set_aspect('equal')

# Draw a from origin
draw_vector(ax, a, GREEN, "a = [1,2]")
# Draw b from tip of a
draw_vector(ax, b, ORANGE, "b = [3,−1]", origin=tuple(a))
# Draw result from origin
draw_vector(ax, result, PURPLE, f"a+b = {result.tolist()}")

ax.plot(0, 0, 'o', color=GREEN, markersize=6)
ax.plot(*a, 'o', color=ORANGE, markersize=6)
ax.plot(*result, 'o', color=PURPLE, markersize=8)

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "plot2_addition.png"), dpi=130, bbox_inches='tight')
plt.close()
print("\n→ Saved: plot2_addition.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 4 — Scalar multiplication
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("SECTION 4 — Scalar Multiplication (stretching & flipping)")
print("=" * 55)

v = np.array([1, 2])
scalars = [2, 0.5, -1, 0]

print(f"Original vector v = {v}")
print()
for s in scalars:
    scaled = s * v
    print(f"  {s:>4} × {v} = {scaled}  →  ", end="")
    if   s > 1:  print("stretched (longer, same direction)")
    elif s == 1: print("unchanged")
    elif 0 < s < 1: print("shrunk (shorter, same direction)")
    elif s == 0: print("zero vector (no length, no direction)")
    elif s < 0:  print("FLIPPED + scaled")

# Plot scalar multiplication
fig, axes = plt.subplots(1, 4, figsize=(14, 4), sharey=True)
fig.suptitle("Scalar Multiplication of v = [1, 2]", fontsize=13, y=1.02)

for ax, s in zip(axes, scalars):
    scaled = s * v
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.axhline(0, color='#aaa', lw=1); ax.axvline(0, color='#aaa', lw=1)
    ax.set_aspect('equal')
    ax.set_title(f"scalar = {s}")

    # Original (faint)
    ax.annotate("", xy=v, xytext=(0,0),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.2,
                                alpha=0.3, mutation_scale=12))
    ax.text(v[0]+0.05, v[1]+0.05, "v", color=GREEN, fontsize=9, alpha=0.4)

    # Scaled
    color = ORANGE if s >= 0 else BLUE
    if not np.all(scaled == 0):
        ax.annotate("", xy=scaled, xytext=(0,0),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2,
                                    mutation_scale=14))
    ax.plot(*scaled, 'o', color=color, markersize=6)
    ax.text(scaled[0]+0.1, scaled[1]+0.1, f"{s}v={scaled.tolist()}", color=color, fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "plot3_scalar.png"), dpi=130, bbox_inches='tight')
plt.close()
print("\n→ Saved: plot3_scalar.png")

# ═══════════════════════════════════════════════════════════════════
# SECTION 5 — Vector magnitude (length)
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("SECTION 5 — Vector Magnitude (length of the arrow)")
print("=" * 55)

v = np.array([3, 4])
magnitude = np.linalg.norm(v)   # √(3² + 4²)

print(f"v          = {v}")
print(f"||v||      = √(3² + 4²) = √({v[0]**2} + {v[1]**2}) = √{v[0]**2+v[1]**2} = {magnitude}")
print()
print("This is just the Pythagorean theorem — the arrow is the hypotenuse!")
print()

# Normalisation: make the vector length exactly 1 (unit vector)
unit_v = v / magnitude
print(f"Unit vector (v / ||v||) = {unit_v.round(4)}")
print(f"Check: ||unit_v||       = {np.linalg.norm(unit_v):.6f}  ← exactly 1.0")
print()
print("In AI: embedding vectors are usually normalised this way so")
print("cosine similarity (angle) equals dot product similarity.")

# ═══════════════════════════════════════════════════════════════════
# SECTION 6 — Why this matters for AI (bonus)
# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("SECTION 6 — Connection to AI (preview)")
print("=" * 55)

# Pretend these are word embedding vectors (simplified to 2D)
word_vectors = {
    "king":   np.array([0.9, 0.8]),
    "queen":  np.array([0.8, 0.9]),
    "man":    np.array([0.7, 0.2]),
    "woman":  np.array([0.6, 0.3]),
    "apple":  np.array([-0.5, -0.6]),
    "banana": np.array([-0.4, -0.7]),
}

print("Simplified 2D word vectors:")
for word, vec in word_vectors.items():
    print(f"  '{word}': {vec}")

# Famous analogy: king - man + woman ≈ queen
result = word_vectors["king"] - word_vectors["man"] + word_vectors["woman"]
print(f"\n'king' − 'man' + 'woman' = {result}")
print(f"'queen'                  = {word_vectors['queen']}")
print(f"Close? {np.allclose(result, word_vectors['queen'], atol=0.2)}")
print("\n← This is vector addition/subtraction on word meanings!")
print("  Real embeddings have 768–3072 dimensions, not just 2.")

# Visualise word vectors
fig, ax = plt.subplots(figsize=(7, 6))
ax.set_xlim(-1, 1.5); ax.set_ylim(-1, 1.5)
ax.axhline(0, color='#aaa', lw=1); ax.axvline(0, color='#aaa', lw=1)
ax.set_title("Simplified 2D word vectors\n(real ones have 768+ dimensions)", pad=10)

colors = [GREEN, GREEN, ORANGE, ORANGE, BLUE, BLUE]
for (word, vec), color in zip(word_vectors.items(), colors):
    ax.annotate("", xy=vec, xytext=(0,0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=12))
    ax.text(vec[0]+0.03, vec[1]+0.03, word, fontsize=10, color=color, fontweight='bold')

# Draw king - man + woman
ax.annotate("", xy=result, xytext=(0,0),
            arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2,
                            linestyle='dashed', mutation_scale=12))
ax.text(result[0]+0.03, result[1]-0.08, "king−man+woman", color=PURPLE, fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(outputs_dir, "plot4_word_vectors.png"), dpi=130, bbox_inches='tight')
plt.close()
print("\n→ Saved: plot4_word_vectors.png")

# ═══════════════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("ALL DONE! Files saved to outputs/")
print("=" * 55)
print("""
Files created:
  plot1_vector.png       — vector as arrow with components
  plot2_addition.png     — tip-to-tail addition
  plot3_scalar.png       — scalar multiplication (4 cases)
  plot4_word_vectors.png — word vectors (AI connection)

Next steps:
  • Modify the vectors a and b in Section 3 and re-run
  • Try a 3D vector: np.array([1, 2, 3]) — what changes?
  • Watch Chapter 2: Linear combinations, span, basis vectors
""")