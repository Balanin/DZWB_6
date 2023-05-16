SELECT  teachers.name as name, subjects.subjects_name as subject
FROM subjects
INNER JOIN teachers ON teachers.id = subjects.teacher_id
WHERE teachers.id == 1
   