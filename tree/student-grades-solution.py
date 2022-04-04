class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.parent = None
        self.left = None
        self.right = None


class Student_Directory:
    def __init__(self) -> None:
        self.root = None

    def insert(self, name, grade):
        """
            Insert a new student into the directory
        """
        # check if directoy is empty
        if self.root is None:
            self.root = Student(name, grade)
        else:
            self._insert(self.root, name, grade)

        # call the tree balancing method

    def _insert(self, curr_student, name, grade):
        """
            Add a new student to the directory. Will recusively search
            the tree until correct placement is found.
        """
        # check the left side
        if grade < curr_student.grade:

            if curr_student.left is None:
                curr_student.left = Student(name, grade)
                curr_student.left.parent = curr_student

            else:
                self._insert(curr_student.left, name, grade)

        elif grade >= curr_student.grade:

            if curr_student.right is None:
                curr_student.right = Student(name, grade)
                curr_student.right.parent = curr_student

            else:
                self._insert(curr_student.right, name, grade)

    def __iter__(self):
        """
            Iterate through every item in the tree.
        """
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, curr_student):
        """
            Move down the tree by one student. Used to go through
            every item in the tree and return it's value.
        """
        if curr_student is not None:
            # left side first
            yield from self._traverse_forward(curr_student.left)
            yield curr_student
            # then the right side
            yield from self._traverse_forward(curr_student.right)


def balance_directory(list):
    """
        Create a student directory that is balanced based on grades 
        using a sorted listed.
    """
    directory = Student_Directory()
    insert_from_middle(list, 0, len(list) - 1, directory)
    return directory


def insert_from_middle(list, i_first, i_last, directory):
    """
        Find the middle element in the list and insert it into the 
        directory. Will run recursively until all elements in the
        list have been added to the directory.
    """
    if i_first > i_last:
        return

    i_middle = (i_first + i_last) // 2

    directory.insert(list[i_middle].name, list[i_middle].grade)

    insert_from_middle(list, i_first, i_middle - 1, directory)
    insert_from_middle(list, i_middle + 1, i_last, directory)


directory = Student_Directory()
done = False

while not done:
    print()
    print("Student Directory")
    print("1. Add new student")
    print("2. View directory")
    print("3. Quit")
    option = int(input("> "))
    print()

    if option == 1:
        name = input("Enter name: ")
        grade = float(input("Enter number grade: "))
        directory.insert(name, grade)
        student_list = [x for x in directory]
        directory = balance_directory(student_list)
    elif option == 2:
        for student in directory:
            if student == directory.root:
                print(student.grade, student.name, "MIDDLE")
            else:
                print(student.grade, student.name)
    elif option == 3:
        done = True
