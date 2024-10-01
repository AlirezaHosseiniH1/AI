def my_final_grade_calculation():
    final_results = {}
    
    num_students = int(input("tedad daneshjo: "))
    
    for _ in range(num_students):
        name = input("nam daneshjo: ").lower()

        quizzes = []
        for i in range(1, 7):
            quiz = int(input(f"nomreh azmon{i} (q{i}) vared konid: "))
            quizzes.append(quiz)
        
        assignments = []
        for i in range(1, 5):
            assignment = int(input(f"nomreh taklif {i} (a{i}) vared konid: "))
            assignments.append(assignment)
        
        midterm = int(input("nomreh miyan term: "))
        
        final_exam = int(input("nomreh emtehan nahayi: "))
        
        quiz_average = sum(quizzes) / len(quizzes)  
        assignment_average = sum(assignments) / len(assignments) 
        
        final_grade = (quiz_average * 0.3) + (assignment_average * 0.2) + (midterm * 0.2) + (final_exam * 0.3)
        
        if final_grade >= 60:
            final_results[name] = "PASS"
        else:
            final_results[name] = "Fail"
    
    return final_results


results = my_final_grade_calculation()
print(results)
