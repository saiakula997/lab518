opcodes = {
    "NO opcode": 0b0000,
    "Prog": 0b0001,
    "ProgStream": 0b0011,
    "A_ADD": 0b0100,
    "A_SUB": 0b0101,
    "A_MUL": 0b0010,
    "A_DIV": 0b0110,
    "A_ADDS": 0b0111,
    "A_SUBS": 0b1000,
    "A_MULS": 0b1001,
    "A_DIVS": 0b1010,
    "Av_ADDS": 0b1011,
    "CMPS": 0b1100,
    "UPDATE": 0b1101,
    "EQUALS": 0b0010
}

class OpcodeCreator:
    def __init__(self, opcodes):
        self.opcodes = opcodes
        self.reverse_opcodes = {v: k for k, v in opcodes.items()}

    def create_opcode(self, opcode_name, destination_address, floating_value, next_opcode_name, result_address):
        # Validate and encode the opcode field
        if opcode_name not in self.opcodes:
            raise ValueError(f"Invalid opcode: {opcode_name}")
        opcode_field = self.opcodes[opcode_name]

        # Validate and encode the next opcode field
        if next_opcode_name not in self.opcodes:
            raise ValueError(f"Invalid next opcode: {next_opcode_name}")
        next_opcode_field = self.opcodes[next_opcode_name]

        # Ensure the fields are within their respective bit ranges
        if not (0 <= destination_address <= 0xFFF):
            raise ValueError("Destination address must be a 12-bit value (0-4095).")
        if not (0 <= floating_value <= 0xFFFFFFFF):
            raise ValueError("Floating value must be a 32-bit value (0-4294967295).")
        if not (0 <= result_address <= 0xFFF):
            raise ValueError("Result address must be a 12-bit value (0-4095).")

        # Construct the 64-bit opcode
        opcode = (opcode_field << 60) | (destination_address << 48) | (floating_value << 16) | (next_opcode_field << 12) | result_address
        return f"{opcode:064b}"

class OpcodeExtractor:
    def __init__(self, opcodes):
        self.opcodes = opcodes

    def extract_fields(self, opcode):
        # Ensure opcode is a 64-bit integer
        if isinstance(opcode, str):
            opcode = int(opcode, 2)

        # Extract fields based on bit positions
        opcode_field = (opcode >> 60) & 0b1111
        destination_address = (opcode >> 48) & 0b111111111111
        floating_value = (opcode >> 16) & 0xFFFFFFFF
        next_opcode_field = (opcode >> 12) & 0b1111
        result_address = opcode & 0b111111111111

        return {
            "opcode": self._decode_opcode(opcode_field),
            "destination_address": destination_address,
            "floating_value": floating_value,
            "next_opcode": self._decode_opcode(next_opcode_field),
            "result_address": result_address
        }

    def _decode_opcode(self, opcode_field):
        # Decode the opcode field into its string representation
        for name, value in self.opcodes.items():
            if opcode_field == value:
                return name
        return "Unknown"
    

class SiteO:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.weight = 0
        self.next_opcode = None
        self.next_site_location = None

    def execute_opcode(self, opcode):
        # Implement logic to execute opcode here
        print(f"Site-O ({self.row}, {self.col}) executing opcode: {opcode}")
        if opcode == 'PROG':
            pass
        elif opcode == 'MUL':
            pass

class Quad:
    def __init__(self, size=64):
        self.size = size
        self.grid = [[SiteO(row, col) for col in range(size)] for row in range(size)]

    def execute_all(self, opcode):
        for row in range(self.size):
            for col in range(self.size):
                self.grid[row][col].execute_opcode(opcode)



# Example Usage
quad = Quad()
opcode = "ADD"  # Example opcode
quad.execute_all(opcode)  # Execute opcode on all Site-Os
