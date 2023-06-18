procedures = """
CREATE PROCEDURE calculate_tour_cost()
BEGIN
	DECLARE excursion_cost DECIMAL(10,2);
	DECLARE hotel_cost DECIMAL(10,2);
    SET SQL_SAFE_UPDATES = 0;
	UPDATE customertour
    SET costTour = (SELECT costHotel FROM hotel WHERE hotel.idHotel = customertour.idHotel) * durationOfTour + (SELECT cost FROM excursion WHERE excursion.idExcursion = customertour.idExcursion);
    SET SQL_SAFE_UPDATES = 1;

END;

CREATE PROCEDURE calculate_tour_discount()
BEGIN
    DECLARE last_tour_id INT;
    DECLARE tour_count INT;
    SELECT idCustomer INTO last_tour_id FROM customertour ORDER BY idCustomerTour DESC LIMIT 1;
    SELECT COUNT(idCustomer) INTO tour_count FROM customertour WHERE idCustomer = last_tour_id;
  
    IF tour_count >= 3 THEN
        SELECT idCustomerTour INTO last_tour_id FROM customertour WHERE idCustomer = last_tour_id ORDER BY idCustomerTour DESC LIMIT 1;
    
        UPDATE customertour
        SET sumSale = costTour - (costTour * 0.1)
        WHERE idCustomerTour = last_tour_id;
    END IF;

END;
"""