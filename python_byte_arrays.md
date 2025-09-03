# Byte Arrays in Python - Complete Guide

## What are Byte Arrays?

**Byte arrays** are mutable sequences of bytes (integers between 0-255) in Python. They're similar to bytes objects but can be modified after creation.

```python
# Creating byte arrays
ba1 = bytearray()           # Empty bytearray
ba2 = bytearray(10)         # 10 zero bytes
ba3 = bytearray(b'Hello')   # From bytes
ba4 = bytearray('Hello', 'utf-8')  # From string
```

## Byte Arrays vs Struct Packing

### Key Differences

| Aspect | Byte Arrays | Struct Packing |
|--------|-------------|---------------|
| **Mutability** | Mutable | Immutable |
| **Use Case** | Manual byte manipulation | Structured data packing |
| **Performance** | Good for incremental building | Best for fixed structures |
| **Flexibility** | High (any byte manipulation) | Limited (specific formats) |
| **Readability** | Lower (manual offset management) | Higher (declarative format) |

### When to Use Each

**Use Byte Arrays when:**
- Building data incrementally
- Need to modify existing binary data
- Working with variable-length data
- Performing low-level byte manipulation

**Use Struct Packing when:**
- Working with fixed-format structures
- Need to convert between Python values and bytes
- Handling endianness explicitly
- Working with C-compatible data structures

## Byte Array Methods and Operations

```python
# Basic operations
ba = bytearray(b'Hello')
ba[0] = 72                   # Modify individual byte
ba.append(33)                # Add byte (33 = '!')
ba.extend(b' World')         # Add multiple bytes
ba.insert(5, 32)             # Insert space at position 5

# Useful methods
length = len(ba)             # Get length
ba.reverse()                 # Reverse in-place
ba.clear()                   # Remove all bytes
count = ba.count(108)        # Count occurrences of 'l' (108)

# Conversion
bytes_obj = bytes(ba)        # Convert to immutable bytes
string = ba.decode('utf-8')  # Convert to string
```

## Exercises with Byte Arrays

### Exercise 1: Basic Byte Array Manipulation
```python
def exercise_1():
    """
    Create a bytearray from 'Hello', modify it to say 'Hello World!',
    and convert it back to a string.
    """
    # Your code here
    pass

def exercise_1_solution():
    ba = bytearray(b'Hello')
    ba.extend(b' World!')
    result = ba.decode('utf-8')
    print(result)  # Hello World!
```

### Exercise 2: Binary Data Builder
```python
def exercise_2():
    """
    Build a binary packet manually using bytearray:
    Header: 0xAA 0x55
    Length: 1 byte (data length)
    Data: variable bytes
    Checksum: 1 byte (sum of data bytes mod 256)
    """
    data = b'TestData'
    # Your code here
    pass

def exercise_2_solution():
    data = b'TestData'
    packet = bytearray()
    packet.extend(b'\xAA\x55')          # Header
    packet.append(len(data))             # Length
    packet.extend(data)                  # Data
    checksum = sum(data) & 0xFF          # Checksum
    packet.append(checksum)
    
    print(f"Packet: {packet.hex(' ')}")
    return packet
```

### Exercise 3: In-place Data Modification
```python
def exercise_3():
    """
    Modify a bytearray in-place to replace all occurrences 
    of one byte with another.
    """
    data = bytearray(b'Hello World! Hello Universe!')
    old_byte = ord('l')  # 108
    new_byte = ord('x')  # 120
    # Your code here
    pass

def exercise_3_solution():
    data = bytearray(b'Hello World! Hello Universe!')
    old_byte = ord('l')
    new_byte = ord('x')
    
    for i in range(len(data)):
        if data[i] == old_byte:
            data[i] = new_byte
    
    print(data.decode('utf-8'))  # Hexxo Worxd! Hexxo Universe!
```

### Exercise 4: Network Packet Parser
```python
def exercise_4():
    """
    Parse a network packet using bytearray slicing:
    [0-1]: Magic number (0xAA55)
    [2]: Packet type
    [3]: Data length (N)
    [4:4+N]: Data
    [4+N]: Checksum
    """
    packet = bytearray(b'\xAA\x55\x02\x08TestData\x7F')
    # Your code here
    pass

def exercise_4_solution():
    packet = bytearray(b'\xAA\x55\x02\x08TestData\x7F')
    
    if len(packet) < 5:
        raise ValueError("Packet too short")
    
    magic = packet[0:2]
    if magic != b'\xAA\x55':
        raise ValueError("Invalid magic number")
    
    ptype = packet[2]
    length = packet[3]
    
    if len(packet) < 4 + length + 1:
        raise ValueError("Packet incomplete")
    
    data = packet[4:4+length]
    checksum = packet[4+length]
    
    # Verify checksum
    calculated = sum(data) & 0xFF
    valid = (calculated == checksum)
    
    return {
        'type': ptype,
        'length': length,
        'data': data,
        'checksum_valid': valid
    }
```

### Exercise 5: Memory-efficient File Processing
```python
def exercise_5():
    """
    Process a large binary file in chunks using bytearray
    to find a specific pattern without loading entire file into memory.
    """
    pattern = b'\xDE\xAD\xBE\xEF'
    # Your code here
    pass

def exercise_5_solution():
    pattern = b'\xDE\xAD\xBE\xEF'
    chunk_size = 4096
    pattern_len = len(pattern)
    
    with open('large_file.bin', 'rb') as f:
        buffer = bytearray()
        position = 0
        
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            buffer.extend(chunk)
            
            # Search for pattern in buffer
            idx = buffer.find(pattern)
            while idx != -1:
                absolute_pos = position + idx
                print(f"Pattern found at position: 0x{absolute_pos:08X}")
                
                # Continue searching from next position
                idx = buffer.find(pattern, idx + 1)
            
            # Keep the last few bytes to handle pattern across chunks
            if len(buffer) > pattern_len:
                buffer = buffer[-pattern_len:]
            
            position += len(chunk)
```

### Exercise 6: Binary Data Transformer
```python
def exercise_6():
    """
    Transform binary data by applying XOR encryption
    using a bytearray for in-place modification.
    """
    data = bytearray(b'SecretMessage')
    key = bytearray(b'MyKey')
    # Your code here
    pass

def exercise_6_solution():
    data = bytearray(b'SecretMessage')
    key = bytearray(b'MyKey')
    
    # XOR encryption
    for i in range(len(data)):
        data[i] ^= key[i % len(key)]
    
    print(f"Encrypted: {data.hex(' ')}")
    
    # Decrypt (XOR again with same key)
    for i in range(len(data)):
        data[i] ^= key[i % len(key)]
    
    print(f"Decrypted: {data.decode('utf-8')}")
```

### Exercise 7: Custom Binary Protocol Builder
```python
def exercise_7():
    """
    Build a custom binary protocol with variable-length fields
    using bytearray for efficient construction.
    """
    fields = [
        (1, b'TypeA'),      # Field type 1, data
        (2, b'Data123'),    # Field type 2, data  
        (3, b'Config'),     # Field type 3, data
    ]
    # Your code here
    pass

def exercise_7_solution():
    fields = [
        (1, b'TypeA'),
        (2, b'Data123'), 
        (3, b'Config'),
    ]
    
    message = bytearray()
    message.extend(b'\xAA\x55')  # Header
    
    for field_type, field_data in fields:
        # Field format: [type][length][data]
        message.append(field_type)
        message.append(len(field_data))
        message.extend(field_data)
    
    # Add checksum
    checksum = sum(message[2:]) & 0xFF  # Skip header
    message.append(checksum)
    
    print(f"Protocol message: {message.hex(' ')}")
    return message
```

### Exercise 8: Efficient Data Filtering
```python
def exercise_8():
    """
    Filter binary data by removing specific bytes efficiently
    using bytearray.
    """
    data = bytearray(b'Remove\x00all\x00null\x00bytes\x00')
    # Your code here
    pass

def exercise_8_solution():
    data = bytearray(b'Remove\x00all\x00null\x00bytes\x00')
    
    # Efficient removal using list comprehension
    # (convert to list of bytes, filter, convert back)
    filtered = bytearray(b for b in data if b != 0)
    
    print(f"Original: {data.hex(' ')}")
    print(f"Filtered: {filtered.hex(' ')}")
    print(f"As string: {filtered.decode('utf-8')}")
```

## Real-world Use Cases for Byte Arrays

### 1. Network Protocol Implementation
```python
class NetworkPacket:
    def __init__(self):
        self.buffer = bytearray()
    
    def add_header(self, magic=b'\xAA\x55'):
        self.buffer.extend(magic)
    
    def add_field(self, field_type, data):
        self.buffer.append(field_type)
        self.buffer.append(len(data))
        self.buffer.extend(data)
    
    def finalize(self):
        checksum = sum(self.buffer) & 0xFF
        self.buffer.append(checksum)
        return bytes(self.buffer)
```

### 2. Binary File Patcher
```python
def patch_binary_file(filename, patches):
    """
    Patch a binary file at multiple offsets
    patches: list of (offset, new_data) tuples
    """
    with open(filename, 'r+b') as f:
        # Read into bytearray for modification
        data = bytearray(f.read())
        
        for offset, new_data in patches:
            if offset + len(new_data) > len(data):
                raise ValueError("Patch exceeds file bounds")
            data[offset:offset+len(new_data)] = new_data
        
        # Write back modified data
        f.seek(0)
        f.write(data)
```

### 3. Memory-efficient Stream Processing
```python
def process_stream_with_lookbehind(stream, pattern, callback):
    """
    Process a stream while maintaining lookbehind buffer
    """
    buffer = bytearray()
    pattern_len = len(pattern)
    
    while True:
        chunk = stream.read(4096)
        if not chunk:
            break
        
        buffer.extend(chunk)
        
        # Process complete patterns in buffer
        while len(buffer) >= pattern_len:
            # Your processing logic here
            if buffer[:pattern_len] == pattern:
                callback(buffer[:pattern_len])
            
            # Remove processed byte
            del buffer[0]
```

## Performance Considerations

### Byte Arrays vs Other Approaches

```python
import time

def test_performance():
    # Method 1: Using bytearray (efficient for building)
    start = time.time()
    ba = bytearray()
    for i in range(100000):
        ba.append(i & 0xFF)
    time1 = time.time() - start
    
    # Method 2: Using bytes concatenation (inefficient)
    start = time.time()
    b = b''
    for i in range(100000):
        b += bytes([i & 0xFF])
    time2 = time.time() - start
    
    print(f"Bytearray: {time1:.3f}s")
    print(f"Bytes concat: {time2:.3f}s")

# Bytearray is much faster for incremental building!
```

## Best Practices

1. **Use bytearray for building binary data incrementally**
2. **Pre-allocate space when possible** for better performance
3. **Use slicing and indexing** for efficient data access
4. **Convert to bytes** when you need immutable data
5. **Be careful with encoding** when converting to/from strings
6. **Use memoryview for zero-copy slicing** of large bytearrays

```python
# Memoryview example for efficient slicing
large_data = bytearray(1000000)
mv = memoryview(large_data)
section = mv[5000:6000]  # No copy made!
```

Byte arrays are powerful tools for embedded developers working with binary data. They provide the flexibility of mutable sequences with the efficiency of working directly with bytes, making them ideal for protocol implementation, data transformation, and low-level binary manipulation tasks.
