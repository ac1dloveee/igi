import pandas as pd
import numpy as np

class PLSerivce:
    """
    Provides services related to Premier League (PL) football matches.

    Attributes:
        __data (DataFrame): A DataFrame containing match results.
        __teams (ndarray): An array of unique team names.
        __stats (DataFrame): A DataFrame to store statistics for each team.

    Methods:
        - team_index(name): Get the index of a team in the list of unique team names.
        - match_data(i): Retrieve match data for a given index.
    """

    def __init__(self):
        """
        Initializes an instance of the PLSerivce class.
        Reads match data from a CSV file and initializes statistics.
        """
        self.__data = pd.read_csv('/home/main/igilab/l4/sixth/data/results.csv')

        self.__teams = self.__data['home_team'].unique()
        self.__teams.sort()

        self.__stats = pd.DataFrame(
            {
                'team': self.__teams,
                'home_goals': np.array([0] * self.__teams.size, dtype=int),
                'away_goals': np.array([0] * self.__teams.size, dtype=int),
                'max_home_goals': np.array([0] * self.__teams.size, dtype=int),
                'max_away_goals': np.array([0] * self.__teams.size, dtype=int),
                'goals': np.array([0] * self.__teams.size, dtype=int),
                'max_goals': np.array([0] * self.__teams.size, dtype=int),
                'home_matches_played': np.array([0] * self.__teams.size, dtype=int),
                'away_matches_played': np.array([0] * self.__teams.size, dtype=int),
                'matches_played': np.array([0] * self.__teams.size, dtype=int),
                'victories': np.array([0] * self.__teams.size, dtype=int),
                'draws': np.array([0] * self.__teams.size, dtype=int),
                'looses': np.array([0] * self.__teams.size, dtype=int),
                'average_home_goals': np.array([0.0] * self.__teams.size, dtype=float),
                'average_away_goals': np.array([0.0] * self.__teams.size, dtype=float),
                'average_goals': np.array([0.0] * self.__teams.size, dtype=float),
                'victories_percent': np.array([0.0] * self.__teams.size, dtype=float),
                'draws_percent': np.array([0.0] * self.__teams.size, dtype=float),
                'looses_percent': np.array([0.0] * self.__teams.size, dtype=float),
            }
        )

    def team_index(self, name: str):
        """
        Get the index of a team in the list of unique team names.

        Parameters:
            name (str): The team name.

        Returns:
            int: The index of the team.
        """
        return np.where(self.__teams == name)[0][0]

    def match_data(self, i: int):
        """
        Retrieve match data for a given index.

        Parameters:
            i (int): The index of the match.

        Returns:
            tuple: A tuple containing match data (e.g., home team name, goals, etc.).
        """
        home_team = self.__data.iloc[i, 0]
        home_index = self.team_index(home_team)

        away_team = self.__data.iloc[i, 1]
        away_index = self.team_index(away_team)

        home_goals = int(self.__data.iloc[i, 2])
        away_goals = int(self.__data.iloc[i, 3])

        result = self.__data.iloc[i, 4]

        return home_index, away_index, home_goals, away_goals, result
    
    def refresh_goals(
            self, home_index: int, away_index: int, home_goals: int, away_goals: int):
        """
        Updates goal-related statistics for home and away teams.

        Parameters:
            home_index (int): Index of the home team.
            away_index (int): Index of the away team.
            home_goals (int): Number of goals scored by the home team.
            away_goals (int): Number of goals scored by the away team.
        """
        self.__stats.at[home_index, 'home_goals'] += home_goals
        self.__stats.at[away_index, 'away_goals'] += away_goals

        self.__stats.at[home_index, 'goals'] += home_goals
        self.__stats.at[away_index, 'goals'] += away_goals

        self.__stats.at[home_index, 'max_home_goals'] = max(
            home_goals, self.__stats.at[home_index, 'max_home_goals'])
        self.__stats.at[away_index, 'max_away_goals'] = max(
            away_goals, self.__stats.at[away_index, 'max_away_goals'])

    def refresh_matches(
            self, home_index: int, away_index: int, result: str):
        """
        Updates match-related statistics for home and away teams.

        Parameters:
            home_index (int): Index of the home team.
            away_index (int): Index of the away team.
            result (str): Match result ('H' for home win, 'D' for draw, 'A' for away win).
        """
        self.__stats.at[home_index, 'home_matches_played'] += 1
        self.__stats.at[away_index, 'away_matches_played'] += 1

        if result == 'H':
            self.__stats.at[home_index, 'victories'] += 1
            self.__stats.at[away_index, 'looses'] += 1
        elif result == 'D':
            self.__stats.at[home_index, 'draws'] += 1
            self.__stats.at[away_index, 'draws'] += 1
        else:
            self.__stats.at[home_index, 'looses'] += 1
            self.__stats.at[away_index, 'victories'] += 1

    def overall_stats(self):
        """
        Computes overall statistics for each team based on match data.

        Updates relevant columns in the stats DataFrame.
        """
        size = len(self.__stats)
        for i in range(size):
            home_matches_played = int(self.__stats.at[i, 'home_matches_played'])
            away_matches_played = int(self.__stats.at[i, 'away_matches_played'])
            matches_played = home_matches_played + away_matches_played
            victories = int(self.__stats.at[i, 'victories'])
            draws = int(self.__stats.at[i, 'draws'])
            looses = int(self.__stats.at[i, 'looses'])

            home_goals = int(self.__stats.at[i, 'home_goals'])
            away_goals = int(self.__stats.at[i, 'away_goals'])
            goals = home_goals + away_goals

            self.__stats.at[i, 'max_goals'] = max(
                self.__stats.at[i, 'max_home_goals'], self.__stats.at[i, 'max_away_goals'])

            self.__stats.at[i, 'goals'] = goals
            self.__stats.at[i, 'matches_played'] = matches_played

            self.__stats.at[i, 'victories_percent'] = victories / matches_played
            self.__stats.at[i, 'draws_percent'] = draws / matches_played
            self.__stats.at[i, 'looses_percent'] = looses / matches_played

            self.__stats.at[i, 'average_home_goals'] = home_goals / home_matches_played  
            self.__stats.at[i, 'average_away_goals'] = away_goals / away_matches_played
            self.__stats.at[i, 'average_goals'] = goals / matches_played

    def stats(self):
        """
        Computes match-related statistics and overall team statistics.

        Sorts the stats DataFrame by victories_percent in descending order.
        Saves the stats DataFrame to a JSON file.

        Returns:
            None
        """
        size = len(self.__data)

        for i in range(size):
            home_index, away_index, home_goals, away_goals, result = self.match_data(i)

            self.refresh_goals(
                home_index, away_index, home_goals, away_goals)

            self.refresh_matches(home_index, away_index, result)

        self.overall_stats()

        self.__stats = self.__stats.sort_values(by=['victories_percent'], ascending=False)
        self.__stats.to_json('/home/main/igilab/l4/sixth/data/stats.json', orient='records', indent=1)

        print('Data Was Written Into /home/main/igilab/l4/sixth/data/stats.json')

    def victory_percent_bigger_by(self):
        """
        Compares the victory percentages of teams and prints the team with the highest and lowest percentages.
        Also calculates how many times the highest percentage is bigger than the lowest.

        Prints:
            - The team with the biggest victory percentage.
            - The team with the smallest victory percentage.
            - The ratio of the highest to lowest victory percentage.
        """
        bvtn = self.__stats[self.__stats['victories_percent'] == self.__stats[
            'victories_percent'].max()].team.values[0]
        svtn = self.__stats[self.__stats['victories_percent'] == self.__stats[
            'victories_percent'].min()].team.values[0]

        bvtp = self.__stats[self.__stats['victories_percent'] == self.__stats[
            'victories_percent'].max()].victories_percent.values[0]
        svtp = self.__stats[self.__stats['victories_percent'] == self.__stats[
            'victories_percent'].min()].victories_percent.values[0]

        print(f'Biggest Victory Percent Team Is {bvtn}')
        print(f'Smallest Victory Percent Team Is {svtn}')

        tm = '{:.2f}'.format(bvtp / svtp)
        print(f'{tm} Times Bigger')
    
    def victory_percent_bigger_by_average_goals(self):
        """
        Compares the average victory percentage of teams with more goals than the overall average.
        Prints the average victory percentage of such teams.

        Prints:
            - The average victory percentage of teams with more goals than the overall average.
        """
        md = np.average(self.__stats.average_goals.values)

        vp = np.average(self.__stats[self.__stats.average_goals > md].victories_percent.values)
        vps = '{:.2f}'.format(vp)
        print(f'Average Victory Percent Of Teams With More Goals Than Average Is {vps}')
