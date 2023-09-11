class LMC:

    def __init__(self):

        # Memory of size 16 (for the sake of this example)

        self.memory = [0] * 16

        # Accumulator register

        self.accumulator = 0

        # Program counter

        self.pc = 0

        # Output register (just for displaying output)

        self.output = None



    def load_program(self, program):

        # Load the given program into memory

        for i, instruction in enumerate(program):

            self.memory[i] = instruction



    def execute(self):

        while True:

            # Fetch instruction from memory

            instruction = self.memory[self.pc]

            # Increment program counter for the next cycle

            self.pc += 1

            # Decode and execute instruction

            op = instruction // 100

            operand = instruction % 100



            if op == 0:      # LDA

                self.accumulator = self.memory[operand]

            elif op == 1:    # ADD

                self.accumulator += self.memory[operand]

            elif op == 2:    # OUT

                self.output = self.accumulator

                print(f"Output: {self.output}")

            elif op == 3:    # HLT

                print("Halting...")

                break



if __name__ == '__main__':

    # Define the program

    # LDA 10 (load number from address 10)

    # ADD 11 (add number from address 11)

    # OUT (display result)

    # HLT (halt)

    program = [10, 111, 200, 300]

    

    # Initialize the LMC and load the program

    computer = LMC()

    computer.load_program(program)

    

    # Place the numbers to be added at memory locations 10 and 11

    computer.memory[10] = 5  # Let's add 5

    computer.memory[11] = 3  # and 3



    # Execute the program

    computer.execute()
