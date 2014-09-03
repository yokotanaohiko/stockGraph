
# -*- coding: utf-8 -*-
import datetime

class Stock(object):

    def __init__(self) :
        self.opening_price = []
        self.closing_price = []
        self.high_price = []
        self.low_price = []
        self.date = []
        self.dealings = []
        self.sales_amount = []
        self.span = 0
        self.name = ""
        self.num = ""
    
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setStockNum(self,num):
        self.num=num

    def getStockNum(self):
        return self.num

    def setStock(self,filename) :
        import csv
        csvReader = csv.reader(open(filename,'r'),delimiter=',')

        count = 0
        for rows in csvReader :
            count += 1
            if count == 1 :
                self.setStockNum(rows[0].split("-")[0])
                self.setName(rows[2])
            if count < 3 :
                continue
            self.opening_price.append(rows[1])
            self.closing_price.append(rows[4])
            self.high_price.append(rows[2])
            self.low_price.append(rows[3])
            self.date.append(rows[0])
            self.dealings.append(rows[5])
        
        # 古い情報ほど先に配列に入っている状態にする。
        self.opening_price.reverse()
        self.closing_price.reverse()
        self.high_price.reverse()
        self.low_price.reverse()
        self.dealings.reverse()
        self.date.reverse()

        self.span = count - 2
    
    def getOffsetFromDate(self,date):
        if not isinstance(date,datetime.date) :
            return False 
       
        count = 0
        for str_day in self.date :
            day = self.getDateFromString(str_day)
            count += 1
            if day.year == date.year and day.month == date.month and day.day == date.day :
                return count 
        
        return False
    
    def getDateFromString(self,string):
        tmps = map(int,string.split("-"))
        dates = datetime.date(year=tmps[0],month=tmps[1],day=tmps[2])
        return dates


    def getOpeningPriceList(self,date=None,span=None):
        if date is None :
            date = self.date[0]
        if span is None :
            span = self.span 
        dates = self.getDateFromString(date)
        offset = self.getOffsetFromDate(dates) 
        if offset :
            return self.opening_price[offset-1:offset-1+span]
        else :
            return False 

    def getClosingPriceList(self,date=None,span=None):
        if date is None :
            date = self.date[0]
        if span is None :
            span = self.span 
        dates = self.getDateFromString(date)
        offset = self.getOffsetFromDate(dates) 
        if offset :
            return self.closing_price[offset-1:offset-1+span]
        else :
            return False

    def getHighPriceList(self,date=None,span=None):
        if date is None :
            date = self.date[0]
        if span is None :
            span = self.span 
        dates = self.getDateFromString(date)
        offset = self.getOffsetFromDate(dates) 
        if offset :
            return self.high_price[offset-1:offset-1+span]
        else :
            return False

    def getLowPriceList(self,date=None,span=None):
        if date is None :
            date = self.date[0]
        if span is None :
            span = self.span 
        dates = self.getDateFromString(date)
        offset = self.getOffsetFromDate(dates) 
        if offset :
            return self.low_price[offset-1:offset-1+span]
        else :
            return False

    def getDealingsList(self,date=None,span=None):
        if date is None :
            date = self.date[0]
        if span is None :
            span = self.span 
        dates = self.getDateFromString(date)
        offset = self.getOffsetFromDate(dates) 
        if offset :
            return self.dealings[offset-1:offset-1+span]
        else :
            return False

    def getDateList(self,date=None,span=None):
        if date is None :
            date = self.date[0]
        if span is None :
            span = self.span 
        dates = self.getDateFromString(date)
        offset = self.getOffsetFromDate(dates) 
        if offset :
            return self.date[offset-1:offset-1+span]
        else :
            return False

    def getWeekData(self) :
        weekStock = Stock()
        week_data = [[],[],[],[],[],[]]
        sw = True 
        li = -1 
        for ii in range(self.span) :
            if sw :
                if self.getDate(ii).weekday()!=0 :
                    continue
                else :
                    sw = False
            if self.getDate(ii).weekday()==0 :
                li+=1
                week_data[0].append(self.date[ii])
                week_data[1].append(int(self.getOpeningPrice(ii)))
                week_data[2].append(int(self.getHighPrice(ii)))
                week_data[3].append(int(self.getLowPrice(ii)))
                week_data[4].append(int(self.getClosingPrice(ii)))
                week_data[5].append(int(self.getDealings(ii)))
                #week_data[6].append(self.getSalesAmount(ii))
            elif self.getDate(ii).weekday() <=4 :
                week_data[2][li]=max(week_data[2][li],int(self.getHighPrice(ii)))
                week_data[3][li]=min(week_data[3][li],int(self.getLowPrice(ii)))
                week_data[4][li]=int(self.getClosingPrice(ii))
                week_data[5][li]+=int(self.getDealings(ii))
                #week_data[6][li]+=self.getSalesAmount(ii)
        weekStock.date=week_data[0]
        weekStock.opening_price=map(str,week_data[1])
        weekStock.high_price=map(str,week_data[2])
        weekStock.low_price=map(str,week_data[3])
        weekStock.closing_price=map(str,week_data[4])
        weekStock.dealings=map(str,week_data[5])
        #weekStock.sales_amount=week_data[6]
        weekStock.span = len(week_data[0])
        weekStock.name = self.name
        weekStock.num = self.num
        return weekStock

    def getMonthData(self) :
        monthStock = Stock()
        month_data = [[],[],[],[],[],[]]
        tmp_month= 0
        li = -1 
        for ii in range(self.span) :
            if tmp_month!=self.getDate(ii).month :
                li+=1
                tmp_month=self.getDate(ii).month
                month_data[0].append(self.date[ii])
                month_data[1].append(int(self.getOpeningPrice(ii)))
                month_data[2].append(int(self.getHighPrice(ii)))
                month_data[3].append(int(self.getLowPrice(ii)))
                month_data[4].append(int(self.getClosingPrice(ii)))
                month_data[5].append(int(self.getDealings(ii)))
                #month_data[6].append(self.getSalesAmount(ii))
            else :
                month_data[2][li]=max(month_data[2][li],int(self.getHighPrice(ii)))
                month_data[3][li]=min(month_data[3][li],int(self.getLowPrice(ii)))
                month_data[4][li]=int(self.getClosingPrice(ii))
                month_data[5][li]+=int(self.getDealings(ii))
                #month_data[6][li]+=self.getSalesAmount(ii)
        monthStock.date=month_data[0][1:]
        monthStock.opening_price=map(str,month_data[1])[1:]
        monthStock.high_price=map(str,month_data[2])[1:]
        monthStock.low_price=map(str,month_data[3])[1:]
        monthStock.closing_price=map(str,month_data[4])[1:]
        monthStock.dealings=map(str,month_data[5])[1:]
        #monthStock.sales_amount=month_data[6]
        monthStock.span = len(month_data[0])
        monthStock.name = self.name
        monthStock.num = self.num
        return monthStock

    def printStocks(self,span=None):
        if span is None :
            span = self.span
        for i in range(span):
            line = []
            line.append(self.opening_price[i])
            line.append(self.high_price[i])
            line.append(self.low_price[i])
            line.append(self.closing_price[i])
            print(line)
    
    def getOpeningPrice(self,offset):
        return self.opening_price[offset]

    def getClosingPrice(self,offset):
        return self.closing_price[offset]

    def getHighPrice(self,offset):
        return self.high_price[offset]

    def getLowPrice(self,offset):
        return self.low_price[offset]

    def getDealings(self,offset):
        return self.dealings[offset]

    def getSalesAmount(self,offset):
        return self.sales_amount[offset]

    def getDate(self,offset):
        return self.getDateFromString(self.date[offset])

    def __len__(self):
        return len(self.date)

if __name__ == '__main__' :
    s1 = Stock()
    s2 = Stock()
    filename1 = "kabuka_data/1491.csv"
    filename2 = "kabuka_data/1757.csv"
    s1.setStock(filename1)
    s2.setStock(filename2)
    print s1.getOpeningPriceList()
    print s2.getClosingPriceList()
    from Utils import Utils
    print Utils.correlation_coefficient(s1.getOpeningPrice(),s2.getOpeningPrice())
    s1.printStocks()

