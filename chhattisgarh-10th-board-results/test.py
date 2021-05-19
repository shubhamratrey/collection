from board_10th_results_2021 import Chhattisgarh10thBoardResult2021


def test_result():
    student_result = Chhattisgarh10thBoardResult2021(roll_number=1213300880)
    print('ROLL_NUMBER  - ', student_result.roll_number)
    print('STUDENT_NAME  - ', student_result.student_name)
    print('FATHER_NAME  - ', student_result.father_name)
    print('MOTHER_NAME  - ', student_result.mother_name)
    print('CENTER_CODE  - ', student_result.center_code)
    print("SCHOOL_CODE  - ", student_result.school_code)
    print("SCIENCE_RESULT  - ", student_result.science_result)
    print("ENGLISH_RESULT  - ", student_result.english_result)
    print("HINDI_RESULT  - ", student_result.hindi_result)
    print("MATHEMATICS_RESULT  - ", student_result.mathematics_result)
    print("INFORMATION_TECHNOLOGY_RESULT  - ", student_result.information_technology_result)
    print('SOCIAL_SCIENCE_RESULT  - ', student_result.social_science_result)
    print('GRAND_TOTAL  - ', student_result.grand_total)
    print('DIVISION - ', student_result.division)


def write_to_csv_for_multiple_roll_numbers():
    import csv
    print("Enter Start Roll Number")
    start_roll_number = input()
    print("Enter End Roll Number")
    end_roll_number = input()
    print("Enter CSV name")
    csv_name = input()

    print(start_roll_number, end_roll_number)

    csv_file = open('{}.csv'.format(csv_name), 'w+')
    writer = csv.DictWriter(csv_file,
                            fieldnames=['ROLL_NUMBER',
                                        'STUDENT_NAME',
                                        'FATHERS_NAME',
                                        'MOTHERS_NAME',
                                        'CENTER_CODE',
                                        'SCHOOL_CODE',
                                        'SCIENCE_TOTAL',
                                        'ENGLISH_TOTAL',
                                        'HINDI_TOTAL',
                                        'MATHEMATICS_TOTAL',
                                        'INFORMATION_TECHNOLOGY_TOTAL',
                                        'SOCIAL_SCIENCE_TOTAL',
                                        'GRAND_TOTAL',
                                        'DIVISION',
                                        ])
    writer.writeheader()
    for roll_number in range(int(start_roll_number), int(end_roll_number)):
        student_result = Chhattisgarh10thBoardResult2021(roll_number=roll_number)
        writer.writerow({
            'ROLL_NUMBER': student_result.roll_number,
            'STUDENT_NAME': student_result.student_name,
            'FATHERS_NAME': student_result.father_name,
            'MOTHERS_NAME': student_result.mother_name,
            'CENTER_CODE': student_result.center_code,
            'SCHOOL_CODE': student_result.school_code,
            'SCIENCE_TOTAL': student_result.science_result.get('TOTAL'),
            'ENGLISH_TOTAL': student_result.english_result.get('TOTAL'),
            'HINDI_TOTAL': student_result.hindi_result.get('TOTAL'),
            'MATHEMATICS_TOTAL': student_result.mathematics_result.get('TOTAL'),
            'INFORMATION_TECHNOLOGY_TOTAL': student_result.information_technology_result.get('TOTAL'),
            'SOCIAL_SCIENCE_TOTAL': student_result.social_science_result.get('TOTAL'),
            'GRAND_TOTAL': student_result.grand_total,
            'DIVISION': student_result.division,
        })
    csv_file.close()


write_to_csv_for_multiple_roll_numbers()
