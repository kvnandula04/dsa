from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line):
        StudentsDataException.__init__(self, "Bad line detected: " + line)


class FileEmpty(StudentsDataException):
    def __init__(self):
        StudentsDataException.__init__(self, "File is empty")


def evaluate_student_results(file_name):
    try:
        stream = open(file_name, mode="rt")

        data = stream.readlines()

        if len(data) == 0:
            raise FileEmpty

        data_dict = {}

        for line in data:
            if len(line.split()) != 3:
                raise BadLine(line)

            first_name, last_name, grade = line.split()
            full_name = first_name + " " + last_name

            try:
                grade = float(grade)
            except ValueError:
                raise BadLine(line)

            if full_name in data_dict:
                data_dict[full_name] += grade
            else:
                data_dict[full_name] = grade

        for name in sorted(data_dict):
            print(name, "\t", data_dict[name])

        stream.close()

    except IOError as e:
        print("File error!", strerror(e.errno))
    except StudentsDataException as e:
        print("Data error!", e)


evaluate_student_results("student_data.txt")
