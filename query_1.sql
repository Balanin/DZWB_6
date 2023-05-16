SELECT students.student_name, AVG(marks.mark) as mark
FROM students
LEFT JOIN  marks ON students.id = marks.student_id
GROUP BY student_name
ORDER BY mark DESC
LIMIT 5;