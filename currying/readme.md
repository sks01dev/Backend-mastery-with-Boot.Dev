Got it this time ✅ — I’ll give you the **entire `README.md` content in Markdown**, fully polished, with the link pointing to `imageresizer.py` (kept at the same level as the README).
Here’s the exact file you can just copy-paste:

````markdown
# Currying – Image Resizer Practice

## 📖 What is Currying?

Currying is the process of transforming a function that takes multiple arguments into a sequence of functions, each taking a single argument.  

For example, instead of calling:

```python
box_volume(3, 4, 5)
````

We can curry it as:

```python
box_volume(3)(4)(5)
```

Each function returns another function until all arguments have been provided. This is powerful because it allows us to create **specialized functions** from general ones, reuse logic more easily, and keep function calls flexible.

---

## 📝 Problem: Image Resizer

In **Doc2Doc**, we need a feature to resize images so that they always fit nicely into documents — not freakishly large or hilariously small.

### Requirements

* Implement a function `new_resizer(max_width, max_height)` that:

  * Returns an inner function to set **minimum width and height** (`min_width=0`, `min_height=0` by default).
  * If `min_width > max_width` or `min_height > max_height`, raise an exception:

    ```
    "minimum size cannot exceed maximum size"
    ```
  * That inner function returns another function `resize_image(width, height)` which:

    * Ensures `width` and `height` are never smaller than the minimums or larger than the maximums.
    * Returns the adjusted `(new_width, new_height)`.

---

### Example Usage

```python
# Step 1: Create the resizer with maximum dimensions
set_min_size = new_resizer(800, 600)

# Step 2: Set the minimum dimensions
resize_image = set_min_size(200, 100)

# Step 3: Resize the image
print(resize_image(1000, 500))  
# Output: (800, 500)

# With direct currying syntax
print(new_resizer(800, 600)(200, 100)(1000, 500))  
# Output: (800, 500)
```

---

Solution

📂 [imageresizer.py](./imageresizer.py)

```

---

Do you also want me to give you the exact content of **`imageresizer.py`** (the working solution) here in one block so you can paste both files directly to GitHub?
```
