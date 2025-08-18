CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N -1;
  RETURN (
      # Write your MySQL query statement below.
      Select Distinct salary
      From Employee
      Order By salary Desc
      Limit 1 OFFSET N
  );
END