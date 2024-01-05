from pandas import read_csv


class DataPreprocessing:
    @classmethod
    def main(cls, data=None):
        if data is None:
            return None

        if cls.__check_result(cls.__format_check, data):
            return "Except"

        df = cls.to_pandas(data)
        return df

    @staticmethod
    def __check_result(func, data) -> bool:
        if func(data) in (None, False):
            return True
        else:
            return False

    @staticmethod
    def __format_check(data) -> bool:
        return data.name.lower().endswith(".csv")

    @staticmethod
    def to_pandas(data):
        data = read_csv(data, sep=",")
        return data


def data_preprocessing(data):
    return DataPreprocessing.main(data)
