
from charts_generator import ChartsGenerator


if __name__ == '__main__':
        generator = ChartsGenerator('statistics/2021-06-02_12_59_29')
        generator.createPieChart()
        generator.createDeathChart()
        generator.createStackedChart()
        generator.createHatChart()
