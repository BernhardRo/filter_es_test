import numpy as np
import matplotlib.pyplot as plt
import csv

path = "D:\\Dokumente\\VisualStudioCode\\nightscout\\filter_es_test\\"
daten=np.loadtxt(path + "Daten.txt", dtype='unicode_')


werte=np.array(daten, dtype=int)


x=np.zeros_like(werte)
for i in range(len(x)):
    x[i]=i*5
print(werte,x)


#forecasting
p=0.2 #Parameter für Stärke des Filters
fc=[werte[0]]
for i in range(len(werte)-1):
    a=int(fc[i]+p*(werte[i]-fc[i]))
    fc.append(a)
    
#15 min average
av=[werte[0],werte[1]]
for i in range(len(werte)-2):
    a=int((werte[i]+werte[i+1]+werte[i+2])/3)
    av.append(a)

#exp + average (correction)
ev=[werte[0]]
ea=[werte[0]]
p=0.2
r=0.4
for i in range(len(werte)-1):
    value = werte[i+1]
    a=(ev[i]+p*(value-ev[i]))
    ev.append(a)
    a=a+r*((werte[i]-ev[i])+(value-a))/2 #gut1 mit p=0.7, r=0.6, stark gedämpft mit p=0,2, r = 0,4
    #a=a+(1-p)*(value-a) #gut2

    ea.append(int(a))

#ESEL implementation
#double smooth = this.value;

#double lastSmooth = SP.getInt("readingSmooth",last*1000)/1000;
#double factor = SP.getDouble("smooth_factor",0.3);
#double correction = SP.getDouble("correction_factor",0.5);
#int lastRaw = SP.getInt("lastReadingRaw", value);

#SP.putInt("lastReadingRaw", this.value);

#double a=lastSmooth+(factor*(this.value-lastSmooth));
#smooth=a+correction*((lastRaw-lastSmooth)+(this.value-a))/2;

#SP.putInt("readingSmooth",(int)Math.round(smooth*1000));

#if(this.value > SP.getInt("lower_limit",65)){
#      this.value = (int)Math.round(smooth);
#}

el=[werte[0]]
factor=0.3
correction=0.5

lastSmooth = werte[0]
lastRaw = werte[0]

for i in range(len(werte)-1):
    value = werte[i+1]
    a = lastSmooth + (factor * (value-lastSmooth))
    smooth=a+(correction*((lastRaw-lastSmooth)+(value-a))/2)
    lastSmooth = smooth
    lastRaw = value
    if value > 65:
        value = smooth
    el.append(int(value))
    
 
label=['origin','filtered, p=' + str(p),'15 min delta','exp (' + str(p)+ ') + corr (' + str(r)+ ')',"ESEL"]


#with open(path + 'out.csv', 'w') as csvfile:
#    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"',lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
#    csvwriter.writerow([label[0], label[1] , label[2], label[3]])
#    for i in range(len(werte)):
#        csvwriter.writerow([werte[i], fc[i] , av[i], ea[i]])


plt.plot(x,werte, linestyle='solid', marker='.', label=label[0])
#plt.plot(x,fc, linestyle='solid', marker='.', label=label[1])
#plt.plot(x,av, linestyle='solid', marker='.', label=label[2])
plt.plot(x,ea, linestyle='solid', marker='.', label=label[3])
plt.plot(x,el, linestyle='solid', marker='.', label=label[4])
plt.legend()
plt.show()
plt.show()
        