SELECT  students.student_name as name, marks.mark as mark, subjects.subjects_name as subject, groups.groups_number
FROM students 
LEFT JOIN marks ON students.id = marks.student_id 
LEFT JOIN groups ON students.group_id = groups.id
LEFT JOIN subjects  ON subjects.id = marks.subject_id
WHERE groups.id == 3 and subject == "Sensor systems "
   