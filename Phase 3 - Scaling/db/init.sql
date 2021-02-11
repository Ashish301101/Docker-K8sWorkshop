CREATE DATABASE subjects;
use subjects;

CREATE TABLE my_subjects (
  name VARCHAR(20),
  code VARCHAR(10)
);

INSERT INTO my_subjects
  (name, code)
VALUES
  ('Cloud Computing', 'UE18CS301'),
  ('Compiler Design', 'UE18CS302'),
  ('OOAD&SE', 'UE18CS303'),
  ('HP', 'UE18CS304'),
  ('SNA', 'UE18CS305'),
  ('OS', 'UE19CS251'),
  ('CN', 'UE19CS252'),
  ('BD', 'UE19CS254D'),
  ('DA', 'UE19CS255'),
  ('Machine Intelligence', 'UE19CS253');