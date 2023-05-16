SELECT students.student_name, AVG(marks.mark) as mark, subjects.subjects_name as subject
FROM students
LEFT JOIN  marks ON students.id = marks.student_id
LEFT JOIN subjects ON subjects.id = marks.subject_id
WHERE subjects_name = "Sensor systems "
GROUP BY student_name
ORDER BY mark DESC
LIMIT 1