SELECT student_id, COUNT(*) AS num_graded_assignments
FROM assignments
WHERE grade IS NOT NULL
GROUP BY student_id;
