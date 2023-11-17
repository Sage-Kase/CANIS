import pandas as p
import math
datas = p.read_excel('CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx')
wanted_data = ["Name (English)", "Region of Focus", "Language", "Entity owner (English)", "Parent entity (English)", "X (Twitter) URL",
               "X (Twitter) Follower #", "Facebook URL", "Facebook Follower #"]

list_data = []


class Data:
    """Data from the Excel is read here

    """
    def __init__(self, name: str):
        """Initialize it with a str name and an empty list for the values in the set
            Can change it to dictionary later"""
        self.name = name
        self.values = []

    def add_values(self, value: tuple) -> None:
        """Add the value to the list as tuple"""
        self.values.append(value)

    def print_data(self) -> None:
        """Print the data in this class"""
        print(f"Name: {self.name}")
        for i in range(len(self.values)):

            curr_value = self.values[i]
            print(f"{curr_value[0]}: {curr_value[1]}")


def extract_all_data() -> None:
    """Extract all data from the DataFrame
        Only if the data exist
    """
    for i in range(1, 50):
        curr = datas.iloc[i].to_dict()
        new_data = Data(curr[wanted_data[0]])
        # read the current data
        for j in range(1, len(wanted_data)):
            if type(curr[wanted_data[j]]) != float:
                # If the type is not a float
                curr_value = wanted_data[j]
                new_data.add_values((curr_value, curr[curr_value]))
            elif not math.isnan(curr[wanted_data[j]]):
                # If it's a float and the value exist
                curr_value = wanted_data[j]
                new_data.add_values((curr_value, curr[curr_value]))
        list_data.append(new_data)


def print_all_data() -> None:
    """ Print all Data in the class"""
    for i in range(len(list_data)):
        print(f"{i + 1}-------------------------------------")
        list_data[i].print_data()


if __name__ == '__main__':
    extract_all_data()
    print_all_data()
