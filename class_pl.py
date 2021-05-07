import requests

from bs4 import BeautifulSoup

class Pl:
    """An attempt to pass data between functions."""

    def __init__(self, league):
        """Initialise attributes to store data."""
        self.league = league
        self.data3 = []

    def describe_league(self):
        print(f"You have chosen the {self.league}.")

    def collect_tabulate_data(self):
        """Collects the data into a list of lists."""
        data = requests.get('https://www.theguardian.com/football/premierleague/table').text
        soup = BeautifulSoup(data, 'html.parser')

        # following 9 lines turn the table into a list of lists
        # data3 = []
        table = soup.find('table', attrs={'class':'table table--football table--league-table table--responsive-font table--striped'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            self.data3.append([ele for ele in cols if ele])
        # print(type(self.data3))
        # print(self.data3)

    def print_data(self):
        print(f"{self.data3}")

    def league_pos(self):
        """Prints position/team."""
        for i in self.data3:
            print((i[0]) + ' ' + (i[1]))
            # print(i[1])

    def pos_gd(self):
        """Prints teams with a positive goal difference."""
        for i in self.data3:
            if int(i[8]) > 0:
                print(i[1])

    def neg_gd(self):
        """Prints teams with a negative goal difference."""
        for i in self.data3:
            if int(i[8]) < 0:
                print(i[1])

    def zero_gd(self):
        """Prints teams with no goal difference."""
        for i in self.data3:
            if int(i[8]) == 0:
                print(i[1])

    def math_poss(self):
        """Prints teams that can mathematically still win the title."""
        a = int(self.data3[0][9])
        lst = []
        for i in self.data3:
            if (((38-int(i[2]))*3)+int(i[9])) >= a:
                lst.append(i[1])
            else:
                pass
        lst = '\n'.join(lst)
        print(f"Here is a list of teams that can still win the league:\n{lst}")

    def math_could_drop(self):
        """Prints teams that can still mathematically be relegated."""
        eighteen_points = int(self.data3[17][9])
        eighteen_poss = (((38-int(self.data3[17][2]))*3)+eighteen_points)
        nineteen_points = int(self.data3[18][9])
        nineteen_poss = (((38-int(self.data3[18][2]))*3)+nineteen_points)
        twenty_points = int(self.data3[19][9])
        twenty_poss = (((38-int(self.data3[19][2]))*3)+twenty_points)
        lst = []
        lst.append(eighteen_poss)
        lst.append(nineteen_poss)
        lst.append(twenty_poss)
        lst.sort()
        a = lst[-1]
        lst2 = []
        for i in self.data3:
            if int(i[9]) <= a:
                lst2.append(i[1])
            else:
                pass
        lst2 = '\n'.join(lst2)
        print(f"Here is a list of teams that can still win the league:\n{lst2}")
