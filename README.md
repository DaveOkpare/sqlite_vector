<div style="text-align: center;">
  <h2>VectorD<sub>um</sub>B</h2>
  <h4>Store and Query Vectors in SQLite</h4>
</div>

<p>
VectorD<sub>um</sub>B is a Python script that provides a simple way to store and query vectors in an SQLite database. It leverages the power of NumPy for vector manipulation and SQLite for efficient storage and retrieval of data.
</p>

<b>SQLite does not support arrays. This script extends SQLite to support Numpy Arrays and provides a retrieval method using KNNs.</b>

<em>This code is not intended for production-use. Please explore <a href="https://www.google.com/search?q=list+of+vector+databases">other vector databases.</a></em>

<h3>Features</h3>

<li>Efficient storage of vectors as NumPy arrays in an SQLite database.</li>
<li>Fast nearest neighbor search for query vectors based on Euclidean distance.</li>
<li>Easy-to-use and extendable with support for custom database tables and queries.</li>
<li>Support for <em>SentenceTransformer</em> embeddings, enabling semantic similarity searches.</li>

<h3>Prerequisites</h3>

To use VectorD<sub>um</sub>B, you need to have the following installed on your system:

1. Python (>=3.6)
2. NumPy (>=1.19)
3. SQLite (usually included with Python distributions)

<h3>Getting Started</h3>

Follow these steps to get started with the `sqlite_vector` project:

1. Clone the repository to your local machine:

```sh
git clone https://github.com/DaveOkpare/sqlite_vector
```

2. Install `numpy`:


```sh
cd sqlite_vector

pip install -r requirements.txt

# OR

pip install numpy
```


```python3
# Import the necessary modules in your Python script:
from vector import VectorDB
import numpy

# Create random nd.array datasets
array1 = np.arange(10)
array2 = np.arange(11, 20)
array3 = np.arange(21, 30)

# Initialize the VectorDB class and create a collection name
db = VectorDB("students")
db.create()

# Insert the arrays into the database
db.insert([array1, array2, array3])

# Search for a specific value in the database
query = np.arange(2, 11, 2) 

output = db.search(query=query, num_results=1)

print(f"Results: {output}")

"""
Results: [0 1 2 3 4 5 6 7 8 9]
"""

```

<h3>License</h3>

Feel free to explore and adapt the provided example to suit your needs! For more details, check out the source code in the repository.

This project is licensed under the [MIT License](LICENSE)
