
# Created by Paulo Chiliguano
# May 2021

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
            "early":[0, 9],
            "normal":[9, 18],
            "late":[18, 24]
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

        if hour >= self._hours_range['early'][0] and hour <= self._hours_range['early'][1]:
            return 0
        elif hour >= self._hours_range['normal'][0] and hour <= self._hours_range['normal'][1]:
            return 1
        elif hour >= self._hours_range['late'][0] and hour <= self._hours_range['late'][1]:
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

        begin_hour_num = int(begin_timeslot[:2])
        end_hour_num = int(end_timeslot[:2])
        
        begin_hour_class = self._classify_hour(begin_hour_num)
        end_hour_class = self._classify_hour(end_hour_num)

        key = 'weekday' if is_weekday else 'weekend'

        if end_hour_class - begin_hour_class == 0:
            # When the timeslot is in-between an interval
            rate = self._rates[key][begin_hour_class]
            end_hour_num = 24 if end_hour_num == 0 else end_hour_num
            return (end_hour_num - begin_hour_num) * rate
        elif abs(end_hour_class - begin_hour_class) == 1:
            # When the timeslot shares 2 intervals
            return 0
        elif abs(end_hour_class - begin_hour_class) == 2:
            # When the timeslot shares 3 intervals
            return 0
        else:
            raise Exception(f'UnexpectedError: Is the schedule well formated? {end_hour_class} {begin_hour_class}')

    
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