# COP4533 Final Project - Stock Profit Maximization

---

## Overview

This repository contains the final project for COP4533. The project explores different algorithmic approaches to solve variations of the **stock buy/sell problem** for maximum profit. The tasks are divided across multiple milestones including problem analysis, algorithm design, implementation, and final presentation.

---

## Problem Variants

### 1. Single Transaction (Problem 1)

Find the best single buy/sell transaction to maximize profit for one stock.

Input: Matrix A[m][n] of predicted stock prices over n days for m stocks.
Output: Tuple (i, j1, j2, profit) representing the stock, buy day, sell day, and maximum profit.
Constraint: Only one buy-sell transaction allowed.

### 2. At Most K Transactions (Problem 2)

Find up to **K** non-overlapping transactions to maximize profit.

Input: Matrix A[m][n], and an integer k (maximum transactions allowed).
Output: A list of at most k buy-sell transactions maximizing total profit.
Constraint: No overlapping transactions.

### 3. Cooldown Constraint (Problem 3)

Maximize profit with a cooldown of **C** days after each sell.

Input: Matrix A[m][n], and integer c (days to wait after each sell).
Output: Sequence of transactions that maximize profit under cooldown constraints.

---

## Tasks

- **Task 1:** Brute Force for Problem 1 (O(m·n²))
- **Task 2:** Greedy for Problem 1 (O(m·n))
- **Task 3:** Dynamic Programming for Problem 1 (O(m·n))
- **Task 4:** Dynamic Programming for Problem 2 (O(m·n²·k))
- **Task 5:** Dynamic Programming for Problem 2 (O(m·n·k))
- **Task 6:** Dynamic Programming for Problem 3 (O(m·n²))
- **Task 7:** Dynamic Programming for Problem 3 (O(m·n))

---

## Project Milestones

**Milestone 1:** Understanding the Problems
Worked out all given examples manually.

**Milestone 2:** Algorithm Design
Designed and documented pseudocode for selected tasks.

**Milestone 3:** Algorithm Implementation
Implemented algorithms in Python/C++/Java.

**Final Presentation**
Recorded walkthrough of pseudocode and design decisions.
