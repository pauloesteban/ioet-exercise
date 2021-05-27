
# Created by Paulo Chiliguano
# May 2021

from datetime import time

class Employee():
    """A class to represent an employee.

    ...

    Attributes
    ----------
        name : str
            the name of an employee

    Methods
    -------
    pay():
        Returns how much the employee has to be paid.
    """

    def __init__(self, input_data):
        """Construct the employee.

        Parameters
        ----------
            input_data : str
                the name of an employee and the schedule they worked.
        """
        self.name, self.__schedule = input_data.split("=")

        self._weekdays_acronyms = ['MO', 'TU', 'WE', 'TH', 'FR']
        self._weekend_acronyms = ['SA', 'SU']
        self._rates = \
        {
            "weekday":{
                0:25,
                1:15,
                2:20
            },
            "weekend":{
                0:30,
                1:20,
                2:25
            }
        }
        self._hours_range =  \
        {
            "early":[time(0,1), time(9,0)],
            "normal":[time(9,1), time(18,0)],
            "late":[time(18,1), time(0,0)]
        }


    def _classify_hour(self, hour: str) -> int:
        """Assign an hour number to early, normal and late classes

        Parameters
        ----------
        hour : str
            indicates hour marked on clock

        Returns
        -------
        (int) : Class of the hour
        """

        dummy = time.fromisoformat(hour)
        print(dummy)
        if (dummy >= self._hours_range['early'][0]) and (dummy <= self._hours_range['early'][1]):
            return 0
        elif (dummy >= self._hours_range['normal'][0]) and (dummy <= self._hours_range['normal'][1]):
            return 1
        elif (dummy >= self._hours_range['late'][0]) and (dummy <= self._hours_range['late'][1]):
            return 2
        else:
            raise Exception('FormatError: Not a valid hour.')


    def _convert_timeslot_to_usd(self, timeslot: str, is_weekday: bool) -> int:
        """Convert daily hours sequence to USD.

        Parameters
        ----------
        timeslot : str
            Timeslot in format HH:MM-HH:MM
        

        Returns
        -------
        (int) : USD dollars
        """
        begin_timeslot, end_timeslot = timeslot.split('-')
        
        begin_hour_class = self._classify_hour(begin_timeslot)
        end_hour_class = self._classify_hour(end_timeslot)

        # key = 'weekday' if is_weekday else 'weekend'

        if end_hour_class - begin_hour_class == 0:
            # When the timeslot is in-between an interval
            return end_time - begin_time
        elif end_hour_class - begin_hour_class == 1:
            # When the timeslot shares 2 intervals
            return 0
        elif end_hour_class - begin_hour_class == 2:
            # When the timeslot shares 3 intervals
            return 0
        else:
            raise Exception('UnexpectedError: Is the schedule well formated?')

    
    def _convert_daily_work_to_usd(self, day_and_timeslot: str) -> int:
        """Convert daily hours sequence to USD.

        Parameters
        ----------
        day_timeslot : str
            Sequence of daily worked hours

        Returns
        -------
        (int) : USD dollars
        """
        day = day_and_timeslot[:2]
        timeslot = day_and_timeslot[2:]

        if day in self._weekdays_acronyms:
            return self._convert_timeslot_to_usd(timeslot, True)
        elif day in self._weekend_acronyms:
            return self._convert_timeslot_to_usd(timeslot, False)
        else:
            raise Exception('FormatError: Not valid day acronym.')


    def _pay_in_usd(self, schedule: str) -> int:
        """Calculate payment according schedule.

        Parameters
        ----------
        schedule : str
            Hours they worked and the times during which they worked.

        Returns
        -------
        result (int) : Employee payment amount in USD.
        """
        daily_work = schedule.split(',')

        result = 0

        for day_and_timeslot in daily_work:
            result += self._convert_daily_work_to_usd(day_and_timeslot)

        return result


    def pay(self) -> str:
        """Indicate how much the employee has to be paid

        Returns
        -------
        statement (str) : Employee payment statement.
        """
        
        self.payment = self._pay_in_usd(self.__schedule)

        self.statement = f'The amount to pay {self.name} is: {self.payment} USD'

        return self.statement