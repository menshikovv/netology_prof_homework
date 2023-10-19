from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    today = datetime.date.today()
    print(f"Текущая дата: {today}")
    calculate_salary()
    get_employees()
