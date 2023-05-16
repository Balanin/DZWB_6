import sqlite3
 

def execute_query(sql: str) -> list:
    with sqlite3.connect("school.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT  students.student_name as name, marks.mark as marks, subjects.subjects_name as subjects, teachers.name as teacher_name
FROM students
LEFT JOIN teachers 
LEFT JOIN subjects 
LEFT JOIN marks ON marks.subject_id = subjects.id
WHERE   subjects =  "Sensor systems "  and  date_of = (SELECT MAX(date_of)
                                                                                  FROM marks
                                                                                  WHERE students.group_id == 1 )
                                                                                               



  
    
   
"""

print(execute_query(sql))