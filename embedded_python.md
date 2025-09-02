# Binary File Operations in Python - Concepts & Notes

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Struct Module](#struct-module)
3. [Endianness](#endianness)
4. [Bit Manipulation](#bit-manipulation)
5. [File Operations](#file-operations)
6. [Checksums & CRCs](#checksums--crcs)
7. [Memory Mapping](#memory-mapping)
8. [Advanced Protocols](#advanced-protocols)
9. [Flash Memory Concepts](#flash-memory-concepts)
10. [Real-time Data Processing](#real-time-data-processing)

## Core Concepts

### Binary vs Text Files
```python
# Text files contain human-readable characters
with open('text.txt', 'w') as f:  # 'w' for text writing
    f.write("Hello World")

# Binary files contain raw bytes
with open('binary.bin', 'wb') as f:  # 'wb' for binary writing
    f.write(b'\x48\x65\x6C\x6C\x6F')  # "Hello" in hex
```

### Byte Strings vs Regular Strings
```python
regular_str = "Hello"    # Unicode string
byte_str = b"Hello"      # Bytes object (0x48 0x65 0x6C 0x6C 0x6F)

# Conversion
text_to_bytes = "Hello".encode('ascii')
bytes_to_text = b"Hello".decode('ascii')
```

## Struct Module

### Format Characters
| Character | C Type          | Python Type | Size |
|-----------|-----------------|-------------|------|
| `x`       | pad byte        | no value    | 1    |
| `c`       | char            | bytes(1)    | 1    |
| `b`       | signed char     | integer     | 1    |
| `B`       | unsigned char   | integer     | 1    |
| `?`       | _Bool           | bool        | 1    |
| `h`       | short           | integer     | 2    |
| `H`       | unsigned short  | integer     | 2    |
| `i`       | int             | integer     | 4    |
| `I`       | unsigned int    | integer     | 4    |
| `l`       | long            | integer     | 4    |
| `L`       | unsigned long   | integer     | 4    |
| `q`       | long long       | integer     | 8    |
| `Q`       | unsigned long long | integer  | 8    |
| `f`       | float           | float       | 4    |
| `d`       | double          | float       | 8    |
| `s`       | char[]          | bytes       | 1    |
| `p`       | char[]          | bytes       | 1    |
| `P`       | void *          | integer     | 4/8  |

### Packing/Unpacking Examples
```python
import struct

# Pack data into bytes
data = struct.pack('<I H f', 12345, 255, 3.14)  # Little-endian
# b'\x39\x30\x00\x00\xff\x00\xc3\xf5H@'

# Unpack bytes into values
values = struct.unpack('<I H f', data)
# (12345, 255, 3.14)

# Calculate size
size = struct.calcsize('<I H f')  # 4 + 2 + 4 = 10 bytes
```

## Endianness

### Types of Endianness
```python
# Big-endian (network byte order): MSB first
big_endian = struct.pack('>I', 0x12345678)  # b'\x12\x34\x56\x78'

# Little-endian (x86): LSB first  
little_endian = struct.pack('<I', 0x12345678)  # b'\x78\x56\x34\x12'

# Native endianness (system-dependent)
native = struct.pack('@I', 0x12345678)
```

### When to Use Which
- **Big-endian**: Network protocols, some processors (PowerPC, SPARC)
- **Little-endian**: x86/x64 processors, most embedded ARM
- **Always specify** endianness explicitly for portability

## Bit Manipulation

### Basic Bit Operations
```python
# Setting bits
value = 0
value |= 1 << 3  # Set bit 3

# Clearing bits
value &= ~(1 << 3)  # Clear bit 3

# Toggling bits
value ^= 1 << 3  # Toggle bit 3

# Checking bits
if value & (1 << 3):  # Check if bit 3 is set
    print("Bit 3 is set")

# Extracting bit fields
mode = (value >> 2) & 0x07  # Extract bits 2-4
```

### Bitfield Extraction Function
```python
def extract_bitfield(byte_val, start_bit, length):
    """Extract a bitfield from a byte"""
    mask = (1 << length) - 1
    return (byte_val >> start_bit) & mask

# Example: Extract bits 2-4 (3 bits) from byte
result = extract_bitfield(0xB3, 2, 3)  # 0b100 (4)
```

## File Operations

### File Modes
| Mode | Description | File Position |
|------|-------------|---------------|
| `'rb'` | Read binary | Start |
| `'wb'` | Write binary (truncate) | Start |
| `'ab'` | Append binary | End |
| `'r+b'` | Read/write | Start |
| `'w+b'` | Read/write (truncate) | Start |
| `'a+b'` | Read/append | End |

### Seeking and Positioning
```python
with open('file.bin', 'r+b') as f:
    # Get current position
    pos = f.tell()  # Returns current offset
    
    # Absolute seek
    f.seek(0x100)  # Go to offset 0x100
    
    # Relative seek
    f.seek(16, os.SEEK_CUR)  # Move forward 16 bytes
    f.seek(-8, os.SEEK_CUR)  # Move backward 8 bytes
    
    # Seek from end
    f.seek(-32, os.SEEK_END)  # 32 bytes from end
```

## Checksums & CRCs

### Simple Checksum
```python
def simple_checksum(data):
    """8-bit checksum (sum of all bytes mod 256)"""
    return sum(data) & 0xFF

# Example
data = b'\x01\x02\x03\x04'
checksum = simple_checksum(data)  # 10
```

### CRC32
```python
import zlib
import binascii

def calculate_crc32(data):
    """Calculate CRC32 checksum"""
    crc = zlib.crc32(data)
    return crc & 0xFFFFFFFF  # Ensure unsigned 32-bit

# Example
data = b'Hello World'
crc = calculate_crc32(data)  # 0x4A17B156
```

### Common Checksum Types
- **Simple sum**: Fast, weak error detection
- **CRC32**: Good balance of speed and detection capability  
- **MD5/SHA**: Cryptographic hashes, slower but stronger

## Memory Mapping

### mmap Basics
```python
import mmap

with open('large_file.bin', 'r+b') as f:
    # Memory map the file
    with mmap.mmap(f.fileno(), 0) as mm:
        # Access like a bytearray
        header = mm[0:16]
        
        # Modify data
        mm[0x100] = 0xFF
        
        # Search for patterns
        position = mm.find(b'\xAA\x55')
        
        # Slice operations
        section = mm[0x1000:0x2000]
```

### mmap Advantages
1. **Efficiency**: No system call overhead for random access
2. **Performance**: Faster than read()/write() for large files
3. **Simplicity**: File appears as a large bytearray in memory

## Advanced Protocols

### Protocol Design Patterns
```python
# Typical binary protocol structure
# [SYNC][HEADER][PAYLOAD][CHECKSUM]

def parse_packet(data):
    """Parse a binary protocol packet"""
    if len(data) < 8:  # Minimum packet size
        return None
    
    # Check sync pattern
    if data[0:2] != b'\xAA\x55':
        return None
    
    # Parse header
    sync, ptype, pid, length = struct.unpack('<H B H B', data[0:6])
    
    # Check if we have complete packet
    if len(data) < 6 + length + 1:
        return None
    
    # Extract payload and checksum
    payload = data[6:6+length]
    checksum = data[6+length]
    
    # Verify checksum
    calculated = sum(data[2:6+length]) & 0xFF
    valid = (calculated == checksum)
    
    return {
        'type': ptype,
        'id': pid,
        'payload': payload,
        'valid': valid
    }
```

## Flash Memory Concepts

### Flash Memory Characteristics
```python
class FlashCharacteristics:
    """Flash memory properties"""
    PAGE_SIZE = 256       # Smallest writable unit
    BLOCK_SIZE = 4096     # Smallest erasable unit  
    MAX_ERASES = 10000    # Endurance cycles
    
    # Flash memory states
    ERASED = 0xFF         # After erase operation
    PROGRAMMED = 0x00-0xFE # After write operation
    
    # Write constraints
    CAN_ONLY_CHANGE_1_TO_0 = True  # Bits can only be cleared, not set
```

### Wear Leveling Strategies
1. **Static wear leveling**: Distribute writes across all blocks
2. **Dynamic wear leveling**: Use least-worn blocks first  
3. **Garbage collection**: Reclaim unused space efficiently
4. **Bad block management**: Handle failed memory cells

## Real-time Data Processing

### Time-series Data Handling
```python
from collections import deque
import statistics

class SensorDataProcessor:
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.data_buffer = deque(maxlen=window_size)
        self.sensor_stats = {}
    
    def process_record(self, timestamp, sensor_id, value):
        """Process a sensor reading"""
        # Store data
        record = (timestamp, sensor_id, value)
        self.data_buffer.append(record)
        
        # Update statistics
        if sensor_id not in self.sensor_stats:
            self.sensor_stats[sensor_id] = {
                'count': 0, 'sum': 0.0, 'sum_sq': 0.0,
                'min': float('inf'), 'max': float('-inf')
            }
        
        stats = self.sensor_stats[sensor_id]
        stats['count'] += 1
        stats['sum'] += value
        stats['sum_sq'] += value * value
        stats['min'] = min(stats['min'], value)
        stats['max'] = max(stats['max'], value)
        
        # Check for anomalies
        return self.detect_anomaly(sensor_id, value)
    
    def detect_anomaly(self, sensor_id, value, threshold=3.0):
        """Detect anomalous values using statistical methods"""
        stats = self.sensor_stats.get(sensor_id)
        if not stats or stats['count'] < 10:
            return False
        
        mean = stats['sum'] / stats['count']
        variance = (stats['sum_sq'] / stats['count']) - (mean * mean)
        std_dev = variance ** 0.5
        
        return abs(value - mean) > threshold * std_dev
```

## Spaced Repetition Questions

1. **Q**: What's the difference between `'rb'` and `'r+b'` file modes?
   **A**: `'rb'` is read-only, `'r+b'` allows both reading and writing.

2. **Q**: How do you extract bits 3-5 from a byte?
   **A**: `(byte_val >> 3) & 0x07` - shift right by 3, mask with 3 bits.

3. **Q**: When should you use big-endian vs little-endian?
   **A**: Big-endian for network protocols, little-endian for x86/ARM systems.

4. **Q**: What's the advantage of mmap over regular file I/O?
   **A**: mmap provides faster random access and treats files like memory.

5. **Q**: How does CRC32 differ from a simple checksum?
   **A**: CRC32 provides better error detection capabilities than simple sums.

6. **Q**: Why is wear leveling important in flash memory?
   **A**: It distributes write/erase cycles to prevent premature failure.

7. **Q**: What does `struct.calcsize('<I f')` return?
   **A**: 8 bytes (4 for int + 4 for float).

8. **Q**: How do you seek to 32 bytes from the end of a file?
   **A**: `f.seek(-32, os.SEEK_END)`

9. **Q**: What's the purpose of sync patterns in binary protocols?
   **A**: They help receivers identify the start of packets and synchronize.

10. **Q**: How can you detect anomalous sensor values statistically?
    **A**: By checking if values deviate significantly from the mean (e.g., 3σ).

## Best Practices

1. **Always specify endianness** explicitly in struct format strings
2. **Use context managers** (`with` statements) for file handling
3. **Validate input data** before parsing to avoid exceptions
4. **Implement error recovery** in protocol parsers
5. **Use appropriate checksums** for your error detection needs
6. **Consider memory mapping** for large binary files
7. **Document your binary formats** thoroughly
8. **Test with edge cases** (empty files, corrupted data, boundary values)

These notes cover the essential concepts from both exercise files. Review them regularly and practice implementing the concepts to build muscle memory for binary file operations in Python.
