SELECT  students.student_name as name, groups.groups_number as groups
FROM students
INNER JOIN groups ON groups.id = students.group_id
WHERE groups.id == 3