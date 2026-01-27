from datetime import date

def validate_date_range(check_in, check_out):
    if check_in >= check_out:
        raise ValueError("Check-out date must be after check-in")
    
    if check_in < date.today():
        raise ValueError("Check-in date cannot be in the past")
    
    #availability search
    #booking creation