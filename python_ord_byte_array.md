# ByteArray.append() vs ByteArray.extend() and ord() Function

## ByteArray.append() vs ByteArray.extend()

### Key Differences

| Aspect | `append()` | `extend()` |
|--------|------------|------------|
| **What it adds** | Single byte (0-255) | Multiple bytes (iterable) |
| **Parameter type** | Integer (0-255) | Bytes-like object (bytes, bytearray, list, etc.) |
| **Usage** | `ba.append(65)` | `ba.extend(b'Hello')` |
| **Performance** | Fast for single items | Faster for multiple items |
| **Use case** | Adding one byte at a time | Adding sequences of bytes |

### Examples and When to Use Each

```python
# append() - for single bytes
ba = bytearray()
ba.append(72)    # Adds byte 72 (H)
ba.append(101)   # Adds byte 101 (e)
ba.append(108)   # Adds byte 108 (l)
# ba now contains: b'Hel'

# extend() - for multiple bytes
ba = bytearray()
ba.extend(b'Hello')  # Adds all bytes at once
# ba now contains: b'Hello'

# extend() with other iterables
ba = bytearray()
ba.extend([72, 101, 108, 108, 111])  # List of integers
# ba now contains: b'Hello'
```

### When to Use Which

**Use `append()` when:**
- Adding single bytes individually
- Building data byte-by-byte in a loop
- When you have integer values (0-255) to add

**Use `extend()` when:**
- Adding multiple bytes at once
- Concatenating existing bytes objects
- Adding sequences of integer values
- When performance matters for bulk operations

### Performance Comparison

```python
import time

def test_append_vs_extend():
    # Test append() - adding bytes one by one
    start = time.time()
    ba1 = bytearray()
    for i in range(10000):
        ba1.append(i & 0xFF)
    time_append = time.time() - start
    
    # Test extend() - adding in chunks
    start = time.time()
    ba2 = bytearray()
    chunk = bytes(range(256))  # 0-255
    for i in range(0, 10000, 256):
        ba2.extend(chunk)
    time_extend = time.time() - start
    
    print(f"append() time: {time_append:.4f}s")
    print(f"extend() time: {time_extend:.4f}s")
    print(f"extend() is {time_append/time_extend:.1f}x faster")

# extend() is typically much faster for bulk operations
```

## The `ord()` Function

### What `ord()` Does

The `ord()` function returns the **Unicode code point** (integer value) of a single character.

```python
# Basic usage
print(ord('A'))    # 65 (ASCII value)
print(ord('a'))    # 97
print(ord('0'))    # 48
print(ord('€'))    # 8364 (Unicode value)
print(ord('汉'))   # 27721 (Chinese character)

# With special characters
print(ord('\n'))   # 10 (newline)
print(ord('\t'))   # 9 (tab)
print(ord(' '))    # 32 (space)
```

### Why `ord()` is Important with Byte Arrays

Byte arrays work with **integers** (0-255), not characters. `ord()` converts characters to their integer representation:

```python
# Without ord() - ERROR!
try:
    ba = bytearray()
    ba.append('A')  # TypeError: 'str' cannot be interpreted as an integer
except TypeError as e:
    print(f"Error: {e}")

# With ord() - CORRECT!
ba = bytearray()
ba.append(ord('A'))  # Works!
ba.append(ord('B'))
ba.append(ord('C'))
print(ba)  # bytearray(b'ABC')

# Convert string to bytes using ord()
text = "Hello"
byte_values = [ord(char) for char in text]
print(byte_values)  # [72, 101, 108, 108, 111]

ba = bytearray()
ba.extend(ord(char) for char in text)  # Generator expression
print(ba)  # bytearray(b'Hello')
```

### Common Use Cases for `ord()`

```python
# 1. Converting strings to byte arrays
def string_to_bytearray(text, encoding='utf-8'):
    """Convert string to bytearray using specified encoding"""
    return bytearray(text.encode(encoding))

# Or using ord() for ASCII characters
def ascii_string_to_bytearray(text):
    """Convert ASCII string to bytearray using ord()"""
    return bytearray(ord(char) for char in text)

# 2. Character validation
def is_printable_ascii(char):
    """Check if character is printable ASCII"""
    code = ord(char)
    return 32 <= code <= 126

# 3. Custom encoding
def custom_encode(text, offset=1):
    """Simple Caesar cipher encoding"""
    return bytearray((ord(char) + offset) % 256 for char in text)
```

## Practical Exercises Combining These Concepts

### Exercise 1: Character Frequency Counter
```python
def char_frequency(text):
    """Count frequency of each character using ord()"""
    freq = {}
    for char in text:
        code = ord(char)
        freq[code] = freq.get(code, 0) + 1
    return freq

# Usage
text = "hello world"
freq = char_frequency(text)
for code, count in sorted(freq.items()):
    print(f"'{chr(code)}' (ASCII {code}): {count}")
```

### Exercise 2: String to ByteArray Converter
```python
def string_to_bytearray_exercise(text):
    """
    Convert string to bytearray using both append() and extend()
    """
    # Method 1: Using append() with ord()
    ba1 = bytearray()
    for char in text:
        ba1.append(ord(char))
    
    # Method 2: Using extend() with generator
    ba2 = bytearray()
    ba2.extend(ord(char) for char in text)
    
    # Method 3: Using bytes conversion
    ba3 = bytearray(text.encode('utf-8'))
    
    return ba1, ba2, ba3

# All three should give same result for ASCII text
```

### Exercise 3: Binary Data Filter
```python
def filter_non_printable(data):
    """
    Filter out non-printable ASCII characters from bytearray
    """
    result = bytearray()
    for byte in data:
        if 32 <= byte <= 126:  # Printable ASCII range
            result.append(byte)
        else:
            result.append(ord('?'))  # Replace with question mark
    
    return result

# Usage
data = bytearray(b'Hello\x00World\x07Test')
filtered = filter_non_printable(data)
print(f"Original: {data}")
print(f"Filtered: {filtered}")
```

### Exercise 4: Simple XOR Encryptor
```python
def xor_encrypt(text, key):
    """
    Simple XOR encryption using ord() and append()
    """
    encrypted = bytearray()
    key_length = len(key)
    
    for i, char in enumerate(text):
        # XOR character with key character (cycling key)
        encrypted_byte = ord(char) ^ ord(key[i % key_length])
        encrypted.append(encrypted_byte)
    
    return encrypted

def xor_decrypt(encrypted_data, key):
    """
    XOR decryption (same as encryption)
    """
    return xor_encrypt(encrypted_data.decode('latin-1'), key)

# Usage
text = "Secret Message"
key = "MyKey"

encrypted = xor_encrypt(text, key)
print(f"Encrypted: {encrypted.hex(' ')}")

decrypted = xor_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
```

## Common Pitfalls and Solutions

### Pitfall 1: Forgetting `ord()` with `append()`
```python
# WRONG:
ba = bytearray()
# ba.append('A')  # TypeError!

# RIGHT:
ba = bytearray()
ba.append(ord('A'))  # Correct
```

### Pitfall 2: Mixing `append()` and `extend()`
```python
# Inefficient:
ba = bytearray()
for char in "Hello":
    ba.append(ord(char))  # 5 separate operations

# Efficient:
ba = bytearray()
ba.extend(ord(char) for char in "Hello")  # 1 operation
```

### Pitfall 3: Unicode vs ASCII
```python
# For non-ASCII characters, use encode() instead of ord()
text = "café"  # Contains non-ASCII character

# Using ord() - may not work correctly
try:
    ba1 = bytearray(ord(char) for char in text)
    print(ba1)  # May not represent 'é' correctly
except:
    pass

# Using encode() - correct approach
ba2 = bytearray(text.encode('utf-8'))
print(ba2)  # Correct representation
```

## Key Takeaways

1. **`append()`** adds single bytes (integers 0-255)
2. **`extend()`** adds multiple bytes (bytes-like objects or iterables)
3. **`ord()`** converts characters to their integer Unicode values
4. Use **`append()`** for individual bytes, **`extend()`** for sequences
5. Use **`ord()`** when you need to convert characters to integer values for byte arrays
6. For non-ASCII text, prefer **`.encode()`** over **`ord()`** for proper encoding

These concepts are fundamental for working with binary data in Python, especially in embedded systems where you often need to convert between character data and byte representations for communication protocols, file formats, and hardware interfaces.
