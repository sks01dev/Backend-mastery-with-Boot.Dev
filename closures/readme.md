# Closures – Boot.dev Practice

A **closure** is a function that remembers and can access variables from its enclosing scope, even after that scope has finished executing.  

They’re useful for keeping state across multiple calls, like counters, accumulators, or configuration objects.  
In Boot.dev, we practice closures by solving small, real-world inspired problems.

---

## 📂 Problems

### 1. Word Count Aggregator
**Problem:**  
Create a closure that aggregates word counts across multiple calls. Each call provides a word, and the function returns the updated counts.  

**Solution:**  
➡️ [word_count_aggregator.py](word_count_aggregator.py)

---

### 2. New Collection
**Problem:**  
Implement `new_collection(initial_docs)` that:  
- Copies the initial list (so it’s not modified).  
- Returns a closure which appends new documents.  
- Each call returns the updated list.  

**Solution:**  
➡️ [new_collection.py](new_collection.py)

---

### 3. CSS Styles Closure
**Problem:**  
Implement `css_styles(initial_styles)` that:  
- Makes a deep copy of the initial styles.  
- Returns a closure that adds or updates selectors and properties.  
- Ensures the original dictionary is never modified.  

**Solution:**  
➡️ [css_styles.py](css_styles.py)

---

## 📌 Notes
- All solutions are written in **Python 3**.  
- Code is kept **minimal and clean** for Boot.dev submission standards.  
- Problems demonstrate closures in **lists, dictionaries, and nested structures**.
