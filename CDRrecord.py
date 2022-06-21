from asyncio.windows_events import NULL
from pickle import FALSE
import random
class CDRrecord:
    columns = ["RecordType","SystemIdentity","FileNum","SwitchNum","CallingNum","CallingIMSI","CalledNum","CalledIMSI","Date","Time","TimeType","CallPeriod","CallingCellID","CalledCellID","ServiceType","Transfer","IMEI","EndType","IncomingTrunk","OutgoingTrunk","MSRN","CalledNum2","FCIFlag","DateTime"]
    ServiceTypeList = [ "a", "b", "S", "V" ]
    TimeTypeList = [ "a", "d", "r", "s" ]
    EndTypeList = ["0", "3", "4"]
    OutgoingTrunkList = [ "F", "442", "623", "418", "425", "443", "426", "621", "614", "609", "419", "402", "411", "422", "420", "423", "421", "300", "400", "405", "409", "424" ]
    IMSIList = [ "466923300507919","466921602131264","466923200348594","466922002560205","466922201102759","466922702346260","466920400352400","466922202546859","466923000886460","466921302209862","466923101048691","466921200135361","466922202613463","466921402416657","466921402237651","466922202679249","466923300236137","466921602343040","466920403025604","262021390056324","466920401237309","466922000696024","466923100098619","466922702341485","466922200432822","466923000464324","466923200779222","466923100807296","466923200408045" ]
    MSRNList = [ "886932428687", "886932429021", "886932428306", "1415982715962", "886932429979", "1416916990491", "886937415371", "886932428876", "886932428688", "1412983121877", "886932429242", "1416955584542", "886932428258", "1412930064972", "886932429155", "886932423548", "1415980332015", "14290800303585", "14290800033338", "886932429626", "886932428112", "1417955696232", "1418986850453", "886932428927", "886932429827", "886932429507", "1416960750071", "886932428242", "886932428134", "886932429825" ,""]

    def __init__(self):
        self.data=dict()
        self.data["SystemIdentity"]= "d0"
        self.data["RecordType"]= "MO"
        self.SystemIdentity = "d0"
        self.RecordType = "MO"
        self.CallPeriod=0
        self.CalledNum=""
        self.DateTime=NULL

        idx=random.randint(0, len(CDRrecord.TimeTypeList)-1)
        self.data["TimeType"]= idx
        self.TimeType=idx
       
        idx=random.randint(0, len(CDRrecord.ServiceTypeList)-1)
        self.data["ServiceType"]=idx
        self.ServiceType=CDRrecord.ServiceTypeList[idx]



        idx=random.randint(0, len(CDRrecord.EndTypeList)-1)
        self.data["EndType"]=CDRrecord.EndTypeList[idx]

        idx=random.randint(0, len(CDRrecord.OutgoingTrunkList)-1)
        self.data["OutgoingTrunk"]=CDRrecord.OutgoingTrunkList[idx] 
        self.OutgoingTrunk =CDRrecord.OutgoingTrunkList[idx]


        idx=random.randint(0, 2)
        self.data["Transfer"]=idx
        self.Transfer=idx

        
        idx=random.randint(0, len(CDRrecord.IMSIList)-1)
        self.data["CallingIMSI"]=CDRrecord.IMSIList[idx]
        self.CallingIMSI=  CDRrecord.IMSIList[idx]

        idx=random.randint(0,len(CDRrecord.IMSIList)-1)    
        self.data["CalledIMSI"]=CDRrecord.IMSIList[idx]
        self.CalledIMSI=CDRrecord.IMSIList[idx]
        
        idx=random.randint(0,len(CDRrecord.MSRNList)-1)    
        self.data["MSRN"]=CDRrecord.MSRNList[idx]
        self.MSRN=CDRrecord.MSRNList[idx]

    def setData(self,key,value):
        if self.data.get(key,FALSE):
            self.data[key]=value
        else:
            self.data[key]=value
            # //setting instance variable data at runtime is remaining..
        if key=="SwitchNum":
            self.SwitchNum=value
        if key=="CallingIMSI":
            self.CallingIMSI=value
        if key=="CalledNum":
            self.CalledNum=value
        if key=="CalledIMSI":
            self.CalledIMSI=value
        if key=="Date":
            self.DateS = value
        if key=="Time":
            self.TimeS = value
        if key== "CallPeriod":
            self.CallPeriod=int(value)
        if key == "ServiceType":
            self.ServiceType=value
        if key=="MSRN":
            self.MSRN=value
        if key =="FCIFlag":
            self.FCIFlag = value
        if key== "DateTime":
            if len(value)>13:
                self.DateTime=value
            else:
                self.DateTime="F F"
        

if __name__=="__main__":
    pass