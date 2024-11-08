These examples illustrate 1-byte keys and their hexadecimal (hex) representations. Each key is shown as a byte (`b''`) with a specific value, followed by its hex representation (`h`). Let's break down each one:

### Key 1: `b'\x12'`
- **Byte Representation**: `b'\x12'` indicates a byte with the hexadecimal value of `12`. The `\x` prefix is used in Python byte literals to specify the following two characters as a hex value.
- **Hex Representation**: `12` is the direct hexadecimal notation of the byte's value, showing that this byte's value is `18` in decimal (1 * 16^1 + 2 * 16^0 = 18).

### Key 2: `b'g'`
- **Byte Representation**: `b'g'` represents the ASCII character `g` as a byte. In ASCII, `g` corresponds to the decimal value `103`.
- **Hex Representation**: `67` is the hexadecimal equivalent of the decimal `103` (`6 * 16^1 + 7 * 16^0 = 103`). This demonstrates how textual (ASCII) data is represented in both bytes and hexadecimal form.

### Key 3: `b'|'`
- **Byte Representation**: `b'|'` is the ASCII character `|` (vertical bar) as a byte. The vertical bar has a decimal ASCII value of `124`.
- **Hex Representation**: `7c` is the hexadecimal form of `124` (`7 * 16^1 + 12 * 16^0 = 124`). This again shows the conversion from an ASCII character to its hexadecimal representation.

### Key 4: `b'B'`
- **Byte Representation**: `b'B'` represents the ASCII character `B` as a byte, which has a decimal value of `66` in the ASCII table.
- **Hex Representation**: `42` is the hexadecimal notation for `66` (`4 * 16^1 + 2 * 16^0 = 66`). This illustrates the byte and hex representation for the uppercase letter `B`.

### Key 5: `b'\xed'`
- **Byte Representation**: `b'\xed'` specifies a byte with the hexadecimal value of `ed`. The `\x` prefix is used to denote hex values in byte literals.
- **Hex Representation**: `ed` corresponds directly to the hexadecimal value `ed`, which is `237` in decimal (`14 * 16^1 + 13 * 16^0 = 237`).

Each example shows how a 1-byte value can be represented as a byte literal in Python and its corresponding hexadecimal value. The hexadecimal representation is a more human-readable way to express binary data, especially in cryptographic contexts where keys and other binary data are commonly represented in hex.