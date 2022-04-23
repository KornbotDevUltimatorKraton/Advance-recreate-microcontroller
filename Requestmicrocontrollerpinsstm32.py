import requests 
r = requests.get("https://raw.githubusercontent.com/KornbotDevUltimatorKraton/mcusdata.github.io/main/STM32F103C8Tx.json")
status = r.status_code 
data = r.json()
Pins_label = {}
Pins_list = []
Sub_label = {}
Sub_label2 = {}
ref_sub = {}
#sprint(status,data)
get_pins = data.get('Mcu')
#print(get_pins)
print("Package_infos")
#for r in range(0,len(get_pins)):       
#        print(list(get_pins)[r])
#print(get_pins.get("Pin"))
mcu_name = ["STM32F103CBTX"]
for pins in range(0,len(get_pins.get("Pin"))):
       
          #print(list(get_pins.get("Pin"))[pins])
          Sub_label['label'] = list(get_pins.get("Pin"))[pins].get("@Name")             
          Sub_label2['type'] = list(get_pins.get("Pin"))[pins].get("@Type")
          if len(Sub_label) > 1: 
                 del Sub_label[next(iter(Sub_label))]
                 print(Sub_label) 
          if len(Sub_label2) > 1:
                 del Sub_label2[next(iter(Sub_label2))]  
                 print(Sub_label2)
          ref_sub[0] = eval(str(Sub_label)),eval(str(Sub_label2))
          Pins_list.append(ref_sub.get(0))
          Pins_label[mcu_name[0]] =  Pins_list
#print(Pins_list)
#Pins_label[mcu_name[0]] = Pins_list
print(Pins_label)
Pins_label.get(mcu_name[0])
for r in Pins_label.get(mcu_name[0]): 
        print(r)