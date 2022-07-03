SELECT * FROM medical WHERE age='35' AND sex='male' AND bmi='32.4' AND children='0' AND smoker='no' AND region='southeast' AND charges='10000.0000'

UPDATE Medical SET charges='11000.0000' WHERE age='35' AND sex='male' AND bmi='32.4' AND children='0' AND smoker='no' AND region='southeast' AND charges='10000.0000'

DELETE FROM Medical WHERE age='35' AND sex='male' AND bmi='32.4' AND children='0' AND smoker='no' AND region='southeast' AND charges='11000.0000'

CREATE TABLE Horizontal_Filter (age text, sex text, bmi text, children text, smoker text, region text, charges text)
INSERT INTO Horizontal_Filter SELECT * FROM Medical WHERE sex='male'

drop table Vertical_Filter

select * from Vertical_Filter limit 10

SELECT * FROM Medical