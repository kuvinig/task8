import random

class InputData:
    def __init__(self):
        self.matrix = None

    def manual_input(self):
        size = int(input("Enter the size of the matrix (N x N): "))
        self.matrix = []
        for i in range(size):
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
            self.matrix.append(row)

    def random_input(self):
        size = int(input("Enter the size of the matrix (N x N): "))
        self.matrix = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

    def get_matrix(self):
        return self.matrix


class Algorithm:
    def __init__(self):
        self.sorted_by_rows = None
        self.sorted_by_columns = None

    def execute(self, matrix):
        # Sort by row averages in descending order
        row_averages = [(sum(row) / len(row), row) for row in matrix]
        self.sorted_by_rows = [row for _, row in sorted(row_averages, key=lambda x: -x[0])]

        # Sort columns by column averages in descending order
        col_averages = [
            sum(col) / len(col) for col in zip(*self.sorted_by_rows)
        ]
        self.sorted_by_columns = list(zip(*sorted(zip(*self.sorted_by_rows), key=lambda x: -sum(x) / len(x))))

    def get_results(self):
        return self.sorted_by_rows, self.sorted_by_columns


class ResultOutput:
    def __init__(self):
        pass

    def display(self, sorted_by_rows, sorted_by_columns):
        print("Matrix sorted by row averages:")
        for row in sorted_by_rows:
            print(row)

        print("\nMatrix sorted by column averages:")
        for col in zip(*sorted_by_columns):
            print(list(col))


class Application:
    def __init__(self):
        self.data = InputData()
        self.algorithm = Algorithm()
        self.output = ResultOutput()
        self.algorithm_executed = False

    def input_data(self):
        choice = input("Input data manually or randomly? (m/r): ").lower()
        if choice == "m":
            self.data.manual_input()
        elif choice == "r":
            self.data.random_input()
        else:
            print("Invalid choice. Please try again.")
        self.algorithm_executed = False

    def run_algorithm(self):
        if self.data.get_matrix():
            self.algorithm.execute(self.data.get_matrix())
            self.algorithm_executed = True
        else:
            print("No data to process. Please input data first.")

    def show_results(self):
        if self.algorithm_executed:
            sorted_by_rows, sorted_by_columns = self.algorithm.get_results()
            self.output.display(sorted_by_rows, sorted_by_columns)
        else:
            print("Algorithm has not been executed. Please run the algorithm first.")

    def exit_program(self):
        print("Exiting program...")
        exit()

    def run(self):
        menu = {
            1: "Input Data",
            2: "Run Algorithm",
            3: "Show Results",
            4: "Exit"
        }

        while True:
            print("\nMain Menu:")
            for key, value in menu.items():
                print(f"{key}: {value}")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.input_data()
            elif choice == 2:
                self.run_algorithm()
            elif choice == 3:
                self.show_results()
            elif choice == 4:
                self.exit_program()
            else:
                print("Invalid choice. Please try again.")


# Run the application
if __name__ == "__main__":
    app = Application()
    app.run()
