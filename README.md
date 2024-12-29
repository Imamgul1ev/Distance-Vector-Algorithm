# Distance Vector Algorithm

This repository provides a detailed explanation and examples of the **Distance Vector Algorithm**, a distributed algorithm used in networking to calculate the shortest paths between nodes in a network.

---

## Overview

### Key Concepts:
1. **Distance Vector Algorithm**:
   - Each node maintains a table (distance vector) of the least-cost path to every other node in the network.
   - Nodes share their distance vectors with their neighbors periodically or when a change occurs.
   - Uses the **Bellman-Ford Equation** to calculate the least-cost path.

2. **Bellman-Ford Equation**:
Dx(y) = minv { cx,v + Dv(y) }

- `Dx(y)`: Cost of the least-cost path from node `x` to node `y`.
- `cx,v`: Cost of the direct link between node `x` and its neighbor `v`.
- `Dv(y)`: Neighbor `v`’s estimated least-cost path to node `y`.
- The minimum is taken over all neighbors `v` of node `x`.

---

## Algorithm Workflow

1. Each node initializes its distance vector with direct neighbors' costs.
2. Nodes exchange their distance vectors with neighbors periodically or when a change is detected.
3. Nodes update their distance vectors using the Bellman-Ford equation.
4. The algorithm continues until all nodes have consistent distance vectors.

---

## Features of the Algorithm

- **Distributed and Iterative**:
- Each node calculates its distance vector independently.
- Nodes notify neighbors only if their distance vector changes.

- **Self-Stopping**:
- If no distance vectors change, no further messages are exchanged.

- **Handling Link Cost Changes**:
- Nodes detect local link cost changes and update their distance vectors accordingly.

- **Challenges**:
- **Count-to-Infinity Problem**: Occurs when link failures lead to incorrect distance vectors propagating through the network.
