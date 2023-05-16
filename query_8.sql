SELECT  teachers.name as name, AVG(marks.mark) as mark, subjects.subjects_name as subject
FROM teachers 
LEFT JOIN subjects ON teachers.id = subjects.teacher_id 
LEFT JOIN marks  ON subjects.id = marks.subject_id
WHERE teachers.id == 3  
GROUP BY subject  