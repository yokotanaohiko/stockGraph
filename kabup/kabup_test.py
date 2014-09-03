# -*- coding :utf-8 -*-
from meigara import Stock
import unittest
class ModelsTest(unittest.TestCase) :
    def setUp(self) :
        self.filename = "kabuka_data/4689.csv"
        self.s1 = Stock()
        self.s1.setStock(self.filename)

    def test_stockModelCheck1(self) :
#        s1.printStocks(10)
        print(self.s1.getOpeningPriceList(date="2014-04-10",span=1))
        print(self.s1.getClosingPriceList())
        print(self.s1.getHighPriceList(date="2014-04-10",span=3))
        print(self.s1.getLowPriceList(date="2014-04-10",span=4))
        print(self.s1.getDateList(date="2014-04-10",span=5))
    def test_stockModelCheck2(self) :
       tmp = self.s1.getDateFromString("2014-04-10")
       print type(tmp)
       print (tmp.year,tmp.month,tmp.day)
       print self.s1.getOffsetFromDate(tmp)
       print self.s1.span
       print self.s1.getName()
       print self.s1.getStockNum()

    def tearDown(self) :


        pass
if __name__ == "__main__" :
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelsTest)
unittest.TextTestRunner(verbosity=2).run(suite)
