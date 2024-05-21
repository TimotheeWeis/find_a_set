import json
import numpy as np
from tabulate import tabulate

class StatsTracker:
    def __init__(self):
        self.stats = {}
        self.categories = ["same_same_same_same", "same_same_same_different", "same_same_different_same", "same_same_different_different",
                      "same_different_same_same", "same_different_same_different", "same_different_different_same", "same_different_different_different",
                      "different_same_same_same", "different_same_same_different", "different_same_different_same", "different_same_different_different",
                      "different_different_same_same", "different_different_same_different", "different_different_different_same", "different_different_different_different"]
        
        for category in self.categories:
            self.load_stats(category)

        
    def reset_stats(self, category):
        try:
            self.stats[category] = {
                "total_sets_found": 0,
                "total_hint_given": 0,
                "time_list": [],
                "average_time": 0
            }
        except KeyError:
            print(f"{category} is not a valid stat")
    
    def reset_raw_stats(self):
        for category in self.categories:
            self.reset_stats(category)
    
    def save_stats(self, category):
        with open("stats/raw_stats/" + category + ".json", "w") as file:
            json.dump(self.stats[category], file)

    def register_stat_on_completion(self, category, time):
        self.stats[category]["total_sets_found"] += 1
        self.stats[category]["time_list"].append(time)
    
    def save_raw_stats(self):
        for category in self.categories:
            self.save_stats(category)
    
    def load_stats(self, category):
        with open("stats/raw_stats/" + category + ".json", "r") as file:
            self.stats[category] = json.load(file)

    def load_raw_stats(self):
        for category in self.categories:
            self.load_stats(category)

    def add_hint(self, solution):
        first_card = solution[0]
        second_card = solution[1]
        third_card = solution[2]
        category = self.find_category(first_card, second_card, third_card)
        self.stats[category]["total_hint_given"] += 1

    def find_category(self, first_card, second_card, third_card):
        """
        Supposes the match is guaranteed
        """

        color_check = (first_card.color == second_card.color and second_card.color == third_card.color)
        shape_check = (first_card.shape == second_card.shape and second_card.shape == third_card.shape)
        number_check = (first_card.number == second_card.number and second_card.number == third_card.number)
        shading_check = (first_card.shading == second_card.shading and second_card.shading == third_card.shading)

        category = f"{'same' if color_check else 'different'}_{'same' if shape_check else 'different'}_{'same' if number_check else 'different'}_{'same' if shading_check else 'different'}"
        
        return category
    
    def mean(self, category):
        """
        Compute the mean of the times of the category
        """
        return np.mean(self.stats[category]["time_list"])
    
    def print_mean(self, category):
        """
        Print the mean of the category
        """
        print(f"the mean of the times of the category: {category} is {self.mean(category)}")

    def first_lettres(self, s):
        """
        Transform the categories into smaller versions
        """
        segments = s.split('_')
        res = ''.join([segment[0] for segment in segments if segment])
        return res

    def print_all_means(self):
        """
        Print all the means
        """
        category_list = [self.first_lettres(category) for category in self.categories]
        mean_list = [[self.mean(category) for category in self.categories]]

        print(tabulate(mean_list, headers=category_list, tablefmt="grid"))

    def indices_min_max(self, l):
        """
        Return the index of the min and the max of a list
        """
        min_index = min(range(len(l)), key=l.__getitem__)
        max_index = max(range(len(l)), key=l.__getitem__)
    
        return min_index, max_index

    def best_worse_category(self):
        """
        Give the fastest and slowest category
        """
        category_list = [self.first_lettres(category) for category in self.categories][1:]
        mean_list = [self.mean(category) for category in self.categories][1:]
        min_index, max_index = self.indices_min_max(category_list)
        print(f"The fastest category is: {category_list[min_index]} with a mean of: {mean_list[min_index]}")
        print(f"The slowest category is: {category_list[max_index]} with a mean of: {mean_list[max_index]}")


    