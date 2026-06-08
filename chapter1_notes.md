# Chapter 1 — Vectors
> **3Blue1Brown · Essence of Linear Algebra** · Study Notes

---

## 1. The big question: what IS a vector?

Grant (3B1B) opens by pointing out that three very different communities use the word "vector" — and they're all right:

| Community | What a vector means to them |
|---|---|
| **Physics student** | An arrow in space. It has a **length** (magnitude) and a **direction**. You can move it anywhere — what matters is where it points and how long it is. |
| **CS student** | An ordered list of numbers. Like `[3, -2]` or `[0.5, 1.2, 7.0]`. Just a structured container of values. |
| **Mathematician** | Any object where two operations make sense: **adding** two vectors, and **scaling** a vector by a number. Anything satisfying those rules is a vector. |

> 💡 **3B1B's key insight:** For learning linear algebra, think of vectors as *arrows rooted at the origin*. The tip of the arrow lands at coordinates that match the list of numbers. Both views — arrow and list — describe the same thing.

---

## 2. Coordinates — how arrows become numbers

In 2D, a vector **[3, 2]** means: start at the origin (0,0), walk **3 units right** along the x-axis, then **2 units up** along the y-axis. That's where the arrow tip lands.

```
y
↑
3 ──────────── ● ← tip of vector [3, 2]
2         ↑
1         │ 2 up (y component)
0 ─────────────────→ x
  0  1  2  3
       └──────┘
       3 right (x component)
```

> 💡 The **first number** always tells you movement along x (horizontal). The **second number** tells you movement along y (vertical). In 3D, a third number gives movement along z (depth).

---

## 3. Vector addition — the tip-to-tail rule

To add two vectors, place the tail of the second vector at the tip of the first. The result (the *sum*) is the arrow from the original start to the final tip.

**As numbers:** just add element by element.

```
[1, 2] + [3, -1] = [1+3, 2+(-1)] = [4, 1]
```

**Visually:** walk the first journey, then the second journey. The sum is where you end up.

> 🧭 **Real-world example:** This is why GPS displacement works — drive 3 km north then 4 km east: your total displacement is one diagonal vector, not the winding path you traveled.

---

## 4. Scalar multiplication — stretching & flipping

Multiplying a vector by a plain number (a *scalar*) stretches, shrinks, or flips it. It never changes the direction — only the magnitude — unless the scalar is negative, in which case it reverses direction.

| Operation | Result |
|---|---|
| `2 × [1, 2] = [2, 4]` | Stretched — arrow points same way, twice as long |
| `0.5 × [1, 2] = [0.5, 1]` | Shrunk — shorter, same direction |
| `-1 × [1, 2] = [-1, -2]` | Flipped — points exactly opposite direction |
| `0 × [1, 2] = [0, 0]` | Zero vector — no length, no direction |

> ⚠️ **The word "scalar"** comes from "scale" — it literally scales the vector. In ML/AI, when you normalize a vector you're multiplying by a scalar to make its length exactly 1. This is called a *unit vector*.

---

## 5. Vector magnitude (length)

The magnitude (length) of a vector is calculated using the **Pythagorean theorem**:

```
||v|| = √(x² + y²)

Example: v = [3, 4]
||v|| = √(3² + 4²) = √(9 + 16) = √25 = 5
```

The arrow is the hypotenuse of a right triangle formed by the x and y components.

**Normalizing a vector** (making it length 1):

```
unit_v = v / ||v||

Example: v = [3, 4],  ||v|| = 5
unit_v = [3/5, 4/5] = [0.6, 0.8]
||unit_v|| = 1.0  ← exactly 1
```

> 💡 In AI, embedding vectors are almost always normalized so that cosine similarity (measuring the angle between vectors) equals dot product similarity.

---

## 6. Why this matters for AI

> 🤖 Remember vector databases? Words like "cat" and "kitten" are placed close together in a high-dimensional space. *That's* a vector — a list of numbers. Adding and scaling those vectors is literally what neural networks do millions of times per second. Every weight update in training is scalar multiplication + vector addition.

| In AI | How vectors appear |
|---|---|
| **Word embeddings** | `"king" − "man" + "woman" ≈ "queen"` — this is just vector addition and subtraction on word vectors |
| **Neural networks** | Each layer transforms a vector using matrix multiplication (which is built from dot products of vectors) |
| **Cosine similarity** | Measures the angle between two vectors — used to find "similar" items in a vector database |

---

## Python Reference

```python
import numpy as np

# Creating vectors
v = np.array([3, 2])       # 2D vector
w = np.array([1, -3, 2])   # 3D vector

# Vector addition
a = np.array([1, 2])
b = np.array([3, -1])
result = a + b              # [4, 1]

# Scalar multiplication
scaled = 2 * v              # [6, 4]
flipped = -1 * v            # [-3, -2]

# Magnitude (length)
magnitude = np.linalg.norm(v)   # √(3² + 2²) = 3.606

# Normalize (unit vector)
unit_v = v / np.linalg.norm(v)  # length becomes exactly 1.0

# Word vector analogy (simplified)
king   = np.array([0.9, 0.8])
man    = np.array([0.7, 0.2])
woman  = np.array([0.6, 0.3])
queen  = king - man + woman     # ≈ [0.8, 0.9]
```

---

## Quick Check ✅

| Question | Answer |
|---|---|
| What is `[2, 5] + [-1, 3]`? | `[1, 8]` — add element-by-element: (2−1=1, 5+3=8) |
| What does scaling a vector by 0 give you? | The zero vector `[0, 0]` — a point at the origin with no length and no direction |
| A vector `[0, 5]` points in which direction? | Straight up (along the positive y-axis). No horizontal component at all |
| What's the difference between a vector and a scalar? | A *scalar* is just a single number (like 3 or −0.5). A *vector* is an ordered list of numbers with a direction and magnitude |

---

## What to watch next

**Chapter 2 — Linear combinations, span, and basis vectors.**
After that, Chapter 3 (matrices) is where things get exciting — you'll see how matrices are just bundles of vectors that transform space.

---

*Notes by following the [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) series.*