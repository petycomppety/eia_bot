from .rigcount_model import RigCountModel

class RigCountController:
    def __init__(self):
        self.model = RigCountModel()

    def get_rig_count_data(self):
        try:
            data = self.model.get_data()
            cleaned_data = self.model.clean_data(data)
            return cleaned_data
        except Exception as e:
            print("An error occurred:", e)
            return None