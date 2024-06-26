from student import Student
from group import Group
from group_limit_error import GroupLimitError


def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Female', 24, 'Mary', 'Jane', 'AN146')
    st4 = Student('Male', 23, 'Peter', 'Parker', 'AN147')
    st5 = Student('Male', 22, 'Tony', 'Pony', 'AN148')
    st6 = Student('Male', 21, 'Marshall', 'Matters', 'AN149')
    st7 = Student('Male', 20, 'Lil', 'Wayne', 'AN150')
    st8 = Student('Female', 19, 'Diana', 'Prince', 'AN151')
    st9 = Student('Male', 18, 'Barry', 'Allen', 'AN152')
    st10 = Student('Male', 17, 'Arthur', 'Curry', 'AN153')
    st11 = Student('Female', 16, 'Angelina', 'Jolly', 'AN154')

    gr = Group('PD1')

    students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]

    for student in students:
        gr.add_student(student)

    print(gr)

    try:
        gr.add_student(st11)
    except GroupLimitError as e:
        print(e)

    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

    gr.delete_student('Taylor')
    print(gr)  # Only one student

    gr.delete_student('Taylor')  # No error!


if __name__ == "__main__":
    main()
