import json

class StatsTracker:
    def __init__(self):
        self.stats = {}
        self.categories = ["same_same_same_same", "same_same_same_different", "same_same_different_same", "same_same_different_different",
                      "same_different_same_same", "same_different_same_different", "same_different_different_same", "same_different_different_different",
                      "different_same_same_same", "different_same_same_different", "different_same_different_same", "different_same_different_different",
                      "different_different_same_same", "different_different,same_different", "different_different_different_same", "different_different_different_different"]
        
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
    
    def save_stats(self, category):
        with open("stats/raw_stats/" + category + ".json", "w") as file:
            json.dump(self.stats[category], file)
    
    def save_raw_stats(self):
        for category in self.categories:
            self.save_stats(category)
    
    def load_stats(self, category):
        with open("stats/raw_stats/" + category + ".json", "r") as file:
            self.stats[category] = json.load(file)

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
    


    