
from charts_generator import ChartsGenerator


if __name__ == '__main__':
        generator = ChartsGenerator('statistics/2021-06-04_12_54_40')
        generator.createPieChart()
        generator.createDeathChart()
        generator.createStackedChart()
        generator.createHatChart()
