from DataProcessor import DataProcessor

if __name__ == '__main__':
    dp = DataProcessor('laptop_dataset_test.csv')
    dp.read()
    dp.run()
    dp.print_result()
