
from ast import arg
from datetime import datetime
import time
import random
from CallStore import CallStore
from GenConfig import GenConfig
from CDRrecord import *
import datetime
from datetime import timedelta
import re

class TelcoGenerationEngine:
    def GenerateData(self,args):
        # print(args)
        args=args.split(" ")
        # print(args)
        cdr_records=int(re.findall("\d+", args[1])[0])
        # print(cdr_records)
        probability_of_fraud=int(re.findall("\d+", args[2])[0])
        number_of_hours=int(re.findall("\d+", args[3])[0])


        mobileNos=CallStore(100000)
        config=GenConfig(cdr_records,probability_of_fraud,number_of_hours)
        numCallbackPerFile=int(config.nCallBackPercent * config.nCDRPerFile)

        #  Data generation always start with the current time
        timeAdvancementPerSet = (0.0 + config.nDurationHours) / config.nSets
        simulationTime =datetime.datetime.now()

        invalidRec = False
        genCallback = False
        #  TOOD: Update this to number of hours
        # start time
        ptTime = datetime.datetime.now()
        endTime=ptTime + timedelta(hours=number_of_hours)
        # cdr=0
        while ptTime < endTime:
            cdr=0
            currentTime = ptTime
            print(simulationTime)
            while cdr<config.nCDRPerFile:
                currentTime = ptTime
                # print(round(random.random(), 1))
                pvalue =round(random.random(), 1)
                if pvalue < 0.1:
                    invalidRec = True
                else:
                    invalidRec = False
                
                # Determine whether there will be a callback
                pvalue = round(random.random(), 1)
                if pvalue >= config.nCallBackPercent:
                    genCallback = False
                else:
                    genCallback = True


                # // Determine called and calling num
                calledIdx = random.randint(0, len(mobileNos.callNos)-1)
                callingIdx = random.randint(0, len(mobileNos.callNos)-1)

                rec = CDRrecord()
                rec.setData("FileNum", str(cdr))
                
                
                switchIdx = random.randint(0, len(mobileNos.switchCountries)-1)
                switchAltIdx = random.randint(0, len(mobileNos.switchCountries)-1)

                while switchAltIdx == switchIdx:
                    switchAltIdx = random.randint(0, len(mobileNos.switchCountries)-1)

                rec.setData("SwitchNum", mobileNos.switchCountries[switchIdx])

                if invalidRec:
                    rec.setData("Date", "F")
                    rec.setData("Time", "F")
                    rec.setData("DateTime", "F F")
                else:
                    d = datetime.datetime.strptime("12/10/2020", "%d/%m/%Y")
                    s = d.strftime('%Y%m%d')
                    # callTime = datetime.datetime.strptime(str(ptTime)[0:10],"%Y-%m-%d")
                    callDate = datetime.datetime.strptime(str(currentTime)[0:10],"%Y-%m-%d")
                    callTime = currentTime.strftime("%H:%M:%S.%f")

                    # writting below code is remaining...
                    rec.setData("Date", callDate)
                    rec.setData("Time", callTime)
                    rec.setData("DateTime", "{} {}".format(callDate,callTime))

                    calledNum = mobileNos.callNos[calledIdx]
                    callingNum = mobileNos.callNos[callingIdx]
                    rec.setData("CalledNum", calledNum)
                    rec.setData("CallingNum", callingNum)

                    # // Sim card fraud record
                    if genCallback:
                        rec.setData("CallPeriod", "0")
                        # need to generate another set of no
                        calledIdx = callingIdx
                        callingIdx = random.randint(0, len(mobileNos.callNos)-1)
                        callbackRec =CDRrecord()
                        callbackRec.setData("FileNum", cdr)
                        callbackRec.setData("SwitchNum", mobileNos.switchCountries[switchAltIdx])

                        # Pertub second
                        pertubs = random.randint(0, 30)
                        
                        # setup date and time
                        callDate = datetime.datetime.strptime(str(currentTime)[0:10],"%Y-%m-%d")
                        future_time = currentTime + timedelta(minutes=pertubs)
                        callTime = future_time.strftime("%H:%M:%S.%f")
                        # print("current time {} call Date {}".format(currentTime,callDate))
                        # print(pertubs)
                        # print("future time {} call time {}".format(future_time,callTime))
                        callbackRec.setData("Date", callDate)
                        callbackRec.setData("Time", callTime)
                        callbackRec.setData("DateTime","{} {}".format(callDate,callTime))


                        #// Set it as the same calling IMSI
                        callbackRec.setData("CallingIMSI", rec.CallingIMSI)
                        calledNum = mobileNos.callNos[calledIdx]
                        callingNum = mobileNos.callNos[callingIdx]

                        callbackRec.setData("CalledNum", calledNum)
                        callbackRec.setData("CallingNum", callingNum)
                        callPeriod = random.randint(1, 1000)
                        callbackRec.setData("CallPeriod", callPeriod)
                        print(callPeriod)
                        print("{},{},{},{},{},{},{},{},{}".format(callbackRec.SystemIdentity,callbackRec.RecordType, callbackRec.SwitchNum,callbackRec.CallingIMSI,callbackRec.CalledIMSI,callbackRec.CalledNum,callbackRec.CallPeriod,callbackRec.ServiceType,callbackRec.DateTime))
                        cdr=cdr+1
                    else:
                        callPeriod = random.randint(1, 1000)
                        rec.setData("CallPeriod", callPeriod)
                # // send cdr rec to output
                # //if (genCallback)  Console.Write("callback A->B ");

                print("{},{},{},{},{},{},{},{},{}".format(rec.SystemIdentity,rec.RecordType, rec.SwitchNum,rec.CallingIMSI,rec.CalledIMSI,rec.CalledNum,rec.CallPeriod,rec.ServiceType,rec.DateTime))
                time.sleep(1)
                ptTime = datetime.datetime.now()
                cdr=cdr+1
                if timeAdvancementPerSet < 1.0:
                    simulationTime = simulationTime + timedelta(minutes=timeAdvancementPerSet*60)
                else:
                    simulationTime = simulationTime+ timedelta(hours=timeAdvancementPerSet)
                    # print("below {}".format(simulationTime))
            else:
                break
            # // Advance Time
            # if timeAdvancementPerSet < 1.0:
            #     simulationTime = simulationTime + timedelta(minutes=timeAdvancementPerSet*60)
            # else:
            #     simulationTime = simulationTime+ timedelta(hours=timeAdvancementPerSet)
            #     print("below {}".format(simulationTime))







    
    def outputCDRRecs(self,r):
        pass


if __name__=="__main__":
    telcoGenerationEngine=TelcoGenerationEngine()
    telcoGenerationEngine.GenerateData("10 0.2 2")