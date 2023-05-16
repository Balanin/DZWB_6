SELECT  students.student_name as name, AVG(marks.mark) as marks, subjects.subjects_name as subjects, teachers.name as teacher_name 
FROM students
LEfT JOIN teachers 
LEFT JOIN subjects 
LEFT JOIN marks ON marks.subject_id = subjects.id
WHERE students.id == 3 and teachers.id == 3 
GROUP BY subjects
