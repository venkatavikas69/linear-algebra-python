# Chapter 3 — Linear Transformations & Matrices
> **3Blue1Brown · Essence of Linear Algebra** · Study Notes

---

## 1. What is a linear transformation?

A **transformation** is a function — it takes a vector in, and spits a vector out. But "linear" transformations have two special geometric properties:

| Rule | What it means |
|---|---|
| **1. Lines stay lines** | All straight lines must remain straight after the transformation. No curving, no bending. |
| **2. Origin stays fixed** | The origin (0, 0) must not move. The transformation can squeeze, stretch, and rotate — but (0,0) is always anchored. |

> 💡 **Grant's visual intuition:** Imagine the entire 2D plane printed on a rubber sheet. A linear transformation is what happens when you grab that sheet and pull it — but you must keep grid lines parallel, evenly spaced, and the origin pinned. Rotations, reflections, and shears are all allowed. Folding or curving is not.

These two geometric rules translate directly into two algebraic properties:

```
Additivity:    T(v + w)  =  T(v) + T(w)
Scaling:       T(a · v)  =  a · T(v)
```

> ⚠️ **Non-linear examples** (these violate the rules):
> - Shift: `T(v) = v + [2, 1]` — moves the origin ✗
> - Squaring: `T([x,y]) = [x², y²]` — curves straight lines ✗

---

## 2. The key insight — track only î and ĵ

This is the **central idea** of the entire chapter:

> Because every vector is a linear combination of î and ĵ, you only need to know where the transformation sends **î and ĵ** to know where it sends *every single vector*.

If a transformation moves î to some new vector **â** and ĵ to some new vector **b̂**, then any vector `[x, y]` lands at:

```
Transformed([x, y])  =  x · â  +  y · b̂
```

> 🔑 The entire transformation is completely described by just two vectors — the new locations of î and ĵ. **That's all a matrix is.**

---

## 3. Matrices — a compact way to store a transformation

A 2×2 matrix is simply a way to package the two destination vectors (where î and ĵ land) into a compact grid:

```
Matrix M = | a  c |     Column 1 = where î = [1,0] lands → [a, b]
           | b  d |     Column 2 = where ĵ = [0,1] lands → [c, d]
```

> ⚠️ The **first column** is where î lands. The **second column** is where ĵ lands. **Columns = destinations of basis vectors.**

### Matrix-vector multiplication

Applying the transformation to a vector `[x, y]`:

```
| a  c |   | x |         | a |         | c |     | ax + cy |
| b  d | · | y |  =  x · | b |  +  y · | d |  =  | bx + dy |
```

This is **not** a formula to memorize — it's the geometric idea: *"scale the new î by x, scale the new ĵ by y, then add."*

**Step-by-step example:**

```
M = | 1  3 |    v = | 4 |
    |-2  0 |        | 3 |

= 4 · [1,-2]  +  3 · [3,0]
= [4,-8]  +  [9,0]
= [13, -8]
```

---

## 4. Common transformations as matrices

| Transformation | Matrix | What happens |
|---|---|---|
| **Identity** | `[[1,0],[0,1]]` | Nothing moves. î stays, ĵ stays. |
| **Rotate 90° CCW** | `[[0,-1],[1,0]]` | î→[0,1], ĵ→[−1,0]. x-axis becomes y-axis. |
| **Shear** | `[[1,1],[0,1]]` | î stays, ĵ→[1,1]. Like leaning a stack of cards. |
| **Scale ×2** | `[[2,0],[0,2]]` | Every vector doubles in length. |
| **Reflect x-axis** | `[[1,0],[0,-1]]` | î stays, ĵ flips. y-coords get negated. |
| **Squish to line** | `[[1,1],[0,0]]` | Entire plane collapses onto a single line. det = 0. |

### Rotation matrix (any angle)

```
M_rotate(θ) = | cos(θ)  -sin(θ) |
              | sin(θ)   cos(θ) |

Example — 90° (θ = π/2):
  cos(90°) = 0,  sin(90°) = 1

M = |  0  -1 |
    |  1   0 |
```

---

## 5. Effect of a transformation on shapes

A shear transforms a unit square into a **parallelogram**:

```
Before (unit square):    After shear M=[[1,1],[0,1]]:

    (0,1)──(1,1)             (1,2)──(2,2)
      |      |        →       /      /
    (0,0)──(1,0)           (0,0)──(1,0)
```

- The bottom edge (along x-axis) stays fixed — î doesn't move
- The top edge gets pushed right — ĵ moves to [1,1]
- Area is preserved in a shear (det = 1)

---

## 6. Why this chapter matters for AI

| Concept | How it appears in AI |
|---|---|
| **Matrix multiplication** | Every "Dense" or "Linear" layer in a neural network is `output = W · input`. The weight matrix W is a learned linear transformation. |
| **Transformer attention** | The Q, K, V matrices in self-attention are three different linear transformations of the same input embedding — projecting it into different spaces. |
| **PCA** | Finds a rotation matrix that transforms data into a basis aligned with directions of maximum variance. Dimensionality reduction = dropping low-variance directions. |
| **Stacking layers** | `W3 · (W2 · (W1 · input))` — three linear transformations applied in sequence. Chapter 4 shows this equals one big matrix multiplication. |

> 🤖 When a neural network "learns", it adjusts the numbers inside its weight matrices — tuning the linear transformations of space to map inputs to correct outputs. Understanding matrices as **geometric transformations** is the intuition behind why deep learning works.

### Neural network linear layer

```python
# A single linear layer in a neural network:
output = W @ input + b

# W = weight matrix  → the linear transformation
# b = bias vector    → a translation (added AFTER the linear part)
# input              → the input vector (e.g. a word embedding)
# output             → transformed vector passed to the next layer

# Example: transforming a 4-dim embedding to 3-dim
W = np.random.randn(3, 4)   # 3×4 weight matrix
b = np.random.randn(3)       # 3-dim bias
x = np.array([0.5, -1.2, 0.8, 0.3])   # 4-dim input

output = W @ x + b           # → 3-dim output
```

---

## Python Reference

```python
import numpy as np

# Define a transformation by where î and ĵ land
i_lands = np.array([1, -2])   # î goes here
j_lands = np.array([3,  0])   # ĵ goes here
M = np.column_stack([i_lands, j_lands])   # columns = destinations

# Apply transformation to a vector
v = np.array([4, 3])
result = M @ v                 # → [13, -8]

# Same thing manually (linear combination formula):
result_manual = v[0]*i_lands + v[1]*j_lands   # → [13, -8]

# Common transformation matrices
M_identity  = np.eye(2)
M_rotate90  = np.array([[0, -1], [1, 0]])
M_shear     = np.array([[1, 1], [0, 1]])
M_scale2    = np.array([[2, 0], [0, 2]])
M_reflect_x = np.array([[1, 0], [0, -1]])

# Rotation by any angle θ
theta = np.pi / 4   # 45 degrees
M_rotate_theta = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# Test linearity: T(v+w) = T(v) + T(w)
v = np.array([1.0, 2.0])
w = np.array([3.0, -1.0])
print(np.allclose(M_rotate90 @ (v+w), M_rotate90@v + M_rotate90@w))  # True ✓

# Apply transform to multiple points (e.g. corners of a shape)
square = np.array([[0,1,1,0], [0,0,1,1]], dtype=float)  # 2×4
sheared_square = M_shear @ square   # transform all 4 corners at once
```

---

## Quick Check ✅

| Question | Answer |
|---|---|
| What do a matrix's columns represent? | Where the basis vectors î and ĵ land after the transformation. Column 1 = new î. Column 2 = new ĵ. |
| Apply `[[2,0],[0,2]]` to `[3,1]`. Result? | `[6, 2]` — the scale-by-2 matrix doubles every component. |
| What does `[[0,-1],[1,0]]` do to î = `[1,0]`? | î lands at `[0, 1]` — straight up. Column 1 of the matrix is `[0,1]`. |
| What transformation does the identity matrix represent? | Nothing — every vector lands exactly where it started. |
| Why can't `T(v) = v + [2,1]` be a matrix transformation? | It moves the origin: `[0,0]` maps to `[2,1]`, not `[0,0]`. Matrix transformations must always keep the origin fixed. |

---

## What to watch next

**Chapter 4 — Matrix multiplication as composition.**
Two transformations applied one after the other can always be combined into a single matrix. This is the mathematical foundation of how neural network layers stack, and why `W3 · (W2 · (W1 · x))` can be collapsed into a single matrix product.

---

*Notes by following the [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) series.*