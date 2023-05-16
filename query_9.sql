SELECT  students.student_name as name, subjects.subjects_name as subjects
FROM students 
LEFT JOIN subjects
LEFT JOIN marks ON marks.subject_id = subjects.id
WHERE students.id == 3 
GROUP BY subjects
