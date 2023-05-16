SELECT students.group_id as groups, AVG(marks.mark) as mark, subjects.subjects_name as subject
FROM students
JOIN  marks ON students.id = marks.student_id
LEFT JOIN subjects ON subjects.id = marks.subject_id
WHERE subjects_name = "Sensor systems "
GROUP BY group_id
ORDER BY groups