#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Equivalents in ounces
    #Ton = 35840   Metric ton = 32000
    #Stone = 224   kilogram = 35.274
    #pound = 16    gram = 28.3495
    #ounce = 1     milligram = 0.00003527

    #User inputs values
    TonS = (float(input("Enter number of tons:")))
    StoneS = (float(input("Enter number of stones:")))
    PoundS = (float(input("Enter number of pounds:")))
    OunceS = (float(input("Enter number of ounces:")))

    #Conversion calculations
    TotalOunces = float((35840*TonS)+(224*StoneS)+(16*PoundS+OunceS))          #<--I can't get the math right, everything runs but the math is wrong.

    TotalKilos = (int(TotalOunces/35.274))

    MetricTons = (int(TotalKilos/1000))
    #kilograms = (int(TotalKilos/100))

    GramS = (float(TotalKilos/1000))
    #grams2 = (float(GramS/100))
    grams = ('{0:.1f} grams'.format(GramS))

    #Outcome Output
    Outcome = "The Metric weight is: {0} metric tons, {1} kilos, and {2} ".format(MetricTons,(int(TotalKilos)),grams)

    print(Outcome)
    #print("The Metric weight is:{0} metric tons, {1} kilos, and {2} grams".format((MetricTons,TotalKilos,GramS)))      #<-- First attempts

    #print(int(MetricTons),"metric Tons,",end="")

    #print(int(TotalKilos),"kilos, and",end="")

    #print(float(GramS),'grams.{0:.2f}')
    #print(float(GramS),"grams.")
    # YOUR CODE ENDS HERE

main()