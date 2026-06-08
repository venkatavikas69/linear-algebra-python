# Chapter 2 — Linear Combinations, Span & Basis Vectors
> **3Blue1Brown · Essence of Linear Algebra** · Study Notes

---

## 1. The two special vectors: î and ĵ (i-hat and j-hat)

Grant starts by introducing the two most important vectors in all of 2D linear algebra — the **basis vectors** of the standard coordinate system:

| Vector | Notation | Value | Meaning |
|---|---|---|---|
| **i-hat** | î | `[1, 0]` | One unit to the right, zero up. Defines "one step in the x direction." |
| **j-hat** | ĵ | `[0, 1]` | Zero right, one unit up. Defines "one step in the y direction." |

> 💡 **Key insight:** Every vector `[x, y]` is secretly just:
>
> ```
> [3, 2]  =  3·î + 2·ĵ
>          =  3·[1,0] + 2·[0,1]
>          =  [3,0] + [0,2]
>          =  [3,2]  ✓
> ```
>
> The coordinates are *instructions*: "scale î by this, scale ĵ by that, then add them."

---

## 2. Linear combinations — the core operation

A **linear combination** of two vectors **v** and **w** is any vector you can make using only scaling and adding:

```
a·v + b·w     where a and b are any scalars (any real numbers)
```

**Example:**

```
v = [1, 2],  w = [3, 0]

2·v + (-1)·w  =  2·[1,2] + (-1)·[3,0]
               =  [2, 4] + [-3, 0]
               =  [-1, 4]
```

The word **"linear"** means you're only allowed to **scale** (multiply by a number) and **add**. No squaring, no square roots, no trig — just those two operations.

> 🎚️ Think of `a` and `b` as two dials. As you turn the dials to different values, the tip of the resulting vector `a·v + b·w` sweeps through space. The question is: *which points in space can the tip reach?* That's the **span**.

---

## 3. Span — "how much of space can you reach?"

The **span** of a set of vectors is the collection of **all vectors reachable** by linear combinations of those vectors. It answers: "if these are the only building blocks I have, what can I build?"

### Case 1: Two independent vectors → Span = entire 2D plane ✓

```
v = [2, 1],  w = [0.5, 2]   ← point in different directions
```

By varying `a` and `b` across all real numbers, the tip of `a·v + b·w` can reach **every single point** in the 2D plane. These two vectors together span all of 2D space.

### Case 2: Parallel (dependent) vectors → Span = one line only

```
v = [2, 1],  w = [4, 2]   ← w is just 2×v
```

Since `w = 2·v`, any combination `a·v + b·w = a·v + b·(2v) = (a + 2b)·v`. You can never escape the single line through the origin that `v` points along. The second vector adds **nothing new**.

### Case 3: Zero vector → Span = just the origin

```
a·[0, 0] = [0, 0]   no matter what a is
```

Scaling zero always gives zero. The span of the zero vector is a single point — the origin.

---

## 4. Linear independence vs dependence

This is one of the most important concepts in all of linear algebra:

### Linearly INDEPENDENT ✓
Each vector adds a genuinely **new direction** to the span. No vector in the set can be made from linear combinations of the others.

```
[1, 0]  and  [0, 1]
```

One goes right, one goes up. Neither can produce the other. → **Independent**

### Linearly DEPENDENT ✗
At least one vector is **redundant** — it's already reachable from the others. Adding it to the set doesn't expand the span.

```
[1, 2]  and  [2, 4]   ← [2,4] = 2 × [1,2]
```

The second is just a scaled copy of the first. → **Dependent**

> 🔑 **Test for linear dependence:** Can you write one vector as a linear combination of the others? If yes → dependent.
> For two vectors in 2D, the easy visual check: do they lie on the same line through the origin?

### Detecting dependence mathematically — the determinant

Place the two vectors as columns of a 2×2 matrix and compute the **determinant**:

```
v = [2, 1],  w = [0.5, 2]

Matrix = | 2    0.5 |
         | 1    2   |

det = (2×2) - (0.5×1) = 4 - 0.5 = 3.5  ≠ 0  →  Independent ✓
```

```
v = [2, 1],  w = [4, 2]

Matrix = | 2    4 |
         | 1    2 |

det = (2×2) - (4×1) = 4 - 4 = 0  →  Dependent ✗
```

| Determinant | Meaning |
|---|---|
| `det ≠ 0` | Vectors are **independent** → span = full plane |
| `det = 0` | Vectors are **dependent** → span = just a line |

> ⚠️ We'll explore determinants fully in Chapter 5 — for now, just know det = 0 is the mathematical fingerprint of "these vectors carry no area between them."

---

## 5. Basis — the minimal complete set

A **basis** of a vector space is a set of vectors that satisfies two conditions simultaneously:

| Condition | Meaning |
|---|---|
| **1. Linearly independent** | No redundancy — every vector earns its place by contributing a new direction |
| **2. Spans the space** | Using linear combinations of the basis, you can reach every point in the space |

**The standard basis of 2D space:**
```
î = [1, 0]   and   ĵ = [0, 1]
```

These two vectors are independent (different directions) and their span covers the entire 2D plane.

> ⚠️ The standard basis is **not** the only valid basis. Any two non-parallel vectors work. For example, `[3, 1]` and `[1, 3]` are also a valid basis for 2D space — they're independent and together span the whole plane.

> 🧱 Basis vectors are the **atoms** of a vector space. Every other vector is a unique "recipe" — a specific linear combination of the basis vectors. The coordinates `[3, 2]` are just the recipe: "3 of î, 2 of ĵ."

---

## 6. Coordinates depend on your choice of basis

The same point in space has **different coordinates** depending on which basis you use:

**Standard basis** → coordinates `[4, 3]`
```
4·[1,0] + 3·[0,1] = [4, 3]
```

**Custom basis** `b₁ = [2, 1]`, `b₂ = [-1, 2]` → coordinates `[2.2, 0.4]`
```
2.2·[2,1] + 0.4·[-1,2] = [4.4, 2.2] + [-0.4, 0.8] = [4.0, 3.0]  ✓ same point
```

> 💡 This is why changing the basis is such a powerful technique in ML — the same data can be represented in a new coordinate system where patterns become clearer (like PCA).

---

## 7. Extending to 3D

In 3D, the standard basis has three vectors:

```
î = [1, 0, 0]   ← x direction
ĵ = [0, 1, 0]   ← y direction
k̂ = [0, 0, 1]   ← z direction
```

Three independent vectors in 3D → span = all of 3D space.

**The rank rule:**
```
rank = 1  →  span is a line
rank = 2  →  span is a plane
rank = 3  →  span is all of 3D space
```

Where **rank** = the number of truly independent directions in your set of vectors.

---

## 8. Why this chapter matters for AI

| Concept | How it appears in AI |
|---|---|
| **Basis** | A 768-dim embedding space (like BERT) has a basis of 768 vectors. Every word embedding is a linear combination of those directions. |
| **Linear combination** | A neural network's linear layer computes exactly this: `a·v₁ + b·v₂ + c·v₃ + ...` with learned weights `a, b, c`. |
| **Span** | The span of a neural layer's weight vectors determines which outputs the layer *can possibly* produce. A bottleneck layer with fewer neurons has a smaller span. |
| **Linear independence** | Correlated (linearly dependent) features in ML carry redundant information. This is why feature correlation is a problem — dependent features don't expand the "span" of information. |
| **Change of basis** | PCA finds a new basis where the first basis vector points in the direction of maximum variation in your data. Dimensionality reduction = dropping low-variance basis directions. |

> 🤖 The famous word vector analogy from Chapter 1:
> ```
> "king" - "man" + "woman" ≈ "queen"
> ```
> is just **vector addition and subtraction** — moving along different basis directions in embedding space. You now understand the full machinery behind this.

---

## Python Reference

```python
import numpy as np

# Standard basis vectors
i_hat = np.array([1, 0])
j_hat = np.array([0, 1])

# Any vector as a linear combination of basis vectors
v = np.array([3, 2])
reconstructed = 3 * i_hat + 2 * j_hat   # → [3, 2]  ✓

# Linear combination
v = np.array([1, 2])
w = np.array([3, 0])
result = 2 * v + (-1) * w               # → [-1, 4]

# Check linear independence using the determinant
v = np.array([2, 1])
w = np.array([0.5, 2])
M = np.column_stack([v, w])             # put vectors as columns
det = np.linalg.det(M)                  # 3.5 → independent
# det ≠ 0 → independent  |  det = 0 → dependent

# Check using rank (works for any number of vectors in any dimension)
M = np.row_stack([v, w])
rank = np.linalg.matrix_rank(M)         # 2 → full rank → independent

# Change of basis: find coordinates of a point in a custom basis
b1 = np.array([2, 1])
b2 = np.array([-1, 2])
point = np.array([4, 3])
B = np.column_stack([b1, b2])
coords_in_custom = np.linalg.solve(B, point)  # → [2.2, 0.4]
```

---

## Quick Check ✅

| Question | Answer |
|---|---|
| What is the span of vectors `[1,0]` and `[0,1]`? | The entire 2D plane — these are î and ĵ, the standard basis. Their linear combinations can reach any point `[x, y]`. |
| Are `[2, 4]` and `[1, 2]` linearly independent? | No — they're linearly dependent. `[2,4] = 2 × [1,2]`. They point in the same direction. Their span is just one line, not the whole plane. |
| How many vectors do you need to form a basis for 3D space? | Exactly 3 — one for each dimension. They must be independent and together span all of 3D space. |
| Can `[3, 1]` and `[1, 3]` form a basis for 2D space? | Yes — they point in different directions (not parallel), so they're independent and span the whole plane. |
| What is `2·[1,2] + (−1)·[3,0]`? | `[2,4] + [−3,0] = [−1, 4]` |

---

## What to watch next

**Chapter 3 — Linear transformations and matrices.**
This is the payoff chapter — you'll see how matrices are just a compact way to describe how basis vectors move when space is transformed. Every rotation, scaling, and shear is a matrix. Neural network layers are matrices.

---

*Notes by following the [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) series.*
