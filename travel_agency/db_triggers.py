triggers = """
CREATE TRIGGER customertour_BEFORE_INSERT
BEFORE INSERT ON customertour
FOR EACH ROW
BEGIN
	SET NEW.durationOfTour = NEW.endDateOfTour - NEW.beginDateOfTour;
END;

CREATE TRIGGER customertour_BEFORE_UPDATE
BEFORE UPDATE ON customertour
FOR EACH ROW BEGIN
	SET NEW.durationOfTour = NEW.endDateOfTour - NEW.beginDateOfTour;
END
"""